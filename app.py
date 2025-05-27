import streamlit as st
from sqlalchemy import (create_engine, Column, Integer, String,
                        Date, Float, ForeignKey)
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import datetime

# ─── DB SETUP ─────────────────────────────────────────────
engine = create_engine('sqlite:///tracker.db')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.date.today)
    juz = Column(Integer)
    quarter = Column(String)
    session_type = Column(String)
    duration = Column(Float)
    attention = Column(Integer)
    mistake_count = Column(Integer, default=0)
    notes = Column(String)
    mistakes = relationship("Mistake", back_populates="session")

class Mistake(Base):
    __tablename__ = 'mistakes'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    sura_ayah = Column(String)
    category = Column(String)
    description = Column(String)
    correction = Column(String)
    session = relationship("Session", back_populates="mistakes")

Base.metadata.create_all(engine)

# Migration to add mistake_count column if it doesn't exist
try:
    with engine.connect() as conn:
        # Check if column exists first
        from sqlalchemy import text
        result = conn.execute(text("PRAGMA table_info(sessions)"))
        columns = [row[1] for row in result.fetchall()]
        
        if 'mistake_count' not in columns:
            conn.execute(text("ALTER TABLE sessions ADD COLUMN mistake_count INTEGER DEFAULT 0"))
            conn.commit()
            print("Added mistake_count column to sessions table")
except Exception as e:
    print(f"Migration note: {e}")
    pass

# ─── STREAMLIT UI ─────────────────────────────────────────
st.title("Qur’ān Recitation Tracker")

db = SessionLocal()

# 1) SESSION FORM
st.subheader("📚 Record Practice Session")
with st.form("session_form"):
    col1, col2 = st.columns(2)
    session_date = col1.date_input("Date", value=datetime.date.today(), help="When did this practice session occur?")
    juz = col2.number_input("Juz", min_value=1, max_value=30, step=1, help="Which Juz (part) did you practice?")
    
    col3, col4 = st.columns(2)
    quarter = col3.selectbox("Quarter", ["Q1","Q2","Q3","Q4"], help="Which quarter of the Juz?")
    session_type = col4.selectbox("Type", ["Practice","Test"], help="Was this practice or a test?")
    
    col5, col6 = st.columns(2)
    duration = col5.number_input("Duration (min)", min_value=1.0, value=30.0, help="How long was your session?")
    mistake_count = col6.number_input("Number of Mistakes", min_value=0, value=0, step=1, help="How many mistakes did you make in total?")
    
    attention = st.slider("Attention Level (1-5)", 1, 5, 3, help="How focused were you? 1=Very distracted, 5=Fully focused")
    
    notes = st.text_area("Notes", placeholder="Any additional notes about this session...", help="Optional notes about your practice session")
    
    submit_s = st.form_submit_button("💾 Save Session")
    if submit_s:
        new_s = Session(
            date=session_date, juz=juz, quarter=quarter, session_type=session_type,
            duration=duration, attention=attention, mistake_count=mistake_count, notes=notes
        )
        db.add(new_s); db.commit()
        st.success(f"✅ Session #{new_s.id} saved successfully! You recorded {mistake_count} mistakes.")
        # Page will refresh automatically after form submission

# 2) MISTAKES FORM
st.subheader("📝 Log Mistakes")
sessions = db.query(Session).all()
if sessions:
    # Create a more user-friendly display for session selection
    session_options = {}
    for s in sessions:
        display_text = f"Session #{s.id} - Juz {s.juz} {s.quarter} ({s.session_type}) - {s.mistake_count} mistakes - {s.date}"
        session_options[display_text] = s.id
    
    selected_session = st.selectbox(
        "Link Mistakes to Session", 
        options=list(session_options.keys()),
        help="Select which practice session this mistake occurred in"
    )
    sid = session_options[selected_session]
    
    # Show progress for selected session
    selected_session_obj = db.query(Session).filter(Session.id == sid).first()
    logged_mistakes = db.query(Mistake).filter(Mistake.session_id == sid).count()
    remaining_mistakes = max(0, selected_session_obj.mistake_count - logged_mistakes)
    
    if selected_session_obj.mistake_count > 0:
        st.info(f"📊 Progress: {logged_mistakes}/{selected_session_obj.mistake_count} mistakes logged. {remaining_mistakes} remaining.")
    
    with st.form("mistake_form"):
        col1, col2 = st.columns(2)
        ayah = col1.text_input("Sūra:Ayah", placeholder="e.g. 2:142", help="Format: Sura number:Ayah number")
        category = col2.selectbox("Category", ["Hifz", "Tajweed", "Pronunciation", "Rhythm", "Pause"])
        desc = st.text_input("Description", placeholder="Describe the mistake...")
        corr = st.text_input("Correction / Comment", placeholder="How to fix this mistake...")
        submit_m = st.form_submit_button("Log Mistake")
        if submit_m and ayah and desc:  # Basic validation
            new_m = Mistake(
                session_id=sid, sura_ayah=ayah,
                category=category, description=desc, correction=corr
            )
            db.add(new_m); db.commit()
            st.success(f"Mistake logged for {ayah} in Session #{sid}")
        elif submit_m:
            st.error("Please fill in at least the Sūra:Ayah and Description fields")
else:
    st.info("💡 **Create a practice session first** to start logging individual mistake details. Use the form above to record your practice session and total mistake count.")

# 3) VIEW DATA
st.subheader("📊 View Your Data")
col1, col2 = st.columns(2)

with col1:
    if st.checkbox("📚 Show All Sessions"):
        sessions_data = db.query(Session).all()
        if sessions_data:
            # Convert to a more readable format
            session_list = []
            for s in sessions_data:
                session_list.append({
                    "ID": s.id,
                    "Date": s.date,
                    "Juz": s.juz,
                    "Quarter": s.quarter,
                    "Type": s.session_type,
                    "Duration (min)": s.duration,
                    "Mistakes": s.mistake_count,
                    "Attention": s.attention,
                    "Notes": s.notes[:50] + "..." if s.notes and len(s.notes) > 50 else s.notes
                })
            st.dataframe(session_list, use_container_width=True)
        else:
            st.info("No sessions recorded yet.")

with col2:
    if st.checkbox("❌ Show All Mistakes"):
        mistakes_data = db.query(Mistake).all()
        if mistakes_data:
            # Convert to a more readable format
            mistake_list = []
            for m in mistakes_data:
                mistake_list.append({
                    "Session ID": m.session_id,
                    "Sūra:Ayah": m.sura_ayah,
                    "Category": m.category,
                    "Description": m.description[:40] + "..." if m.description and len(m.description) > 40 else m.description,
                    "Correction": m.correction[:40] + "..." if m.correction and len(m.correction) > 40 else m.correction
                })
            st.dataframe(mistake_list, use_container_width=True)
        else:
            st.info("No mistakes logged yet.")

db.close()

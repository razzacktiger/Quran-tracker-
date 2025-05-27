# PLANNING.md - Qur'ān Recitation Tracker

## 🎯 Project Overview

### Vision
A comprehensive digital tool to help students of the Qur'ān track their recitation practice, identify patterns in mistakes, and monitor their progress in both memorization (Hifz) and proper recitation (Tajweed).

### Target Users
- Students memorizing the Qur'ān (Huffāz)
- Individuals improving their Tajweed
- Teachers tracking student progress
- Self-learners seeking structured practice tracking

## 🏗️ Architecture & Design

### Technology Stack
- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python with SQLAlchemy ORM
- **Database**: SQLite (for simplicity and portability)
- **Data Visualization**: Altair/Plotly (future implementation)
- **Deployment**: Local development, future cloud deployment

### Database Schema

#### Sessions Table
```sql
sessions:
- id (Primary Key)
- date (Date, default: today)
- juz (Integer, 1-30)
- quarter (String: Q1, Q2, Q3, Q4)
- session_type (String: Practice, Test)
- duration (Float, minutes)
- attention (Integer, 1-5 scale)
- notes (Text)
```

#### Mistakes Table
```sql
mistakes:
- id (Primary Key)
- session_id (Foreign Key → sessions.id)
- sura_ayah (String, format: "2:142")
- category (String: Hifz, Tajweed, etc.)
- description (Text)
- correction (Text)
```

### File Structure
```
Quran-tracker-/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── tracker.db            # SQLite database
├── README.md             # Project documentation
├── TASK.md               # Task tracking
├── PLANNING.md           # This file
├── .gitignore            # Git ignore rules
├── LICENSE               # Project license
└── venv/                 # Virtual environment
```

## 📋 Requirements & Features

### Core Requirements (MVP)
1. **Session Tracking**
   - Record practice sessions with metadata
   - Track juz, quarter, duration, attention level
   - Add session notes

2. **Mistake Logging**
   - Link mistakes to specific sessions
   - Categorize mistakes (Hifz vs Tajweed)
   - Record mistake details and corrections

3. **Data Persistence**
   - SQLite database for local storage
   - Maintain data integrity with foreign keys

### Functional Requirements

#### Session Management
- Create new practice sessions
- Record session metadata (juz, quarter, type, duration)
- Rate attention level (1-5 scale)
- Add free-form notes

#### Mistake Tracking
- Log mistakes with specific Sura:Ayah references
- Categorize mistakes by type
- Record detailed descriptions and corrections
- Link mistakes to specific sessions

#### Data Viewing
- Display all sessions in tabular format
- Display all mistakes with session context
- Basic data export capabilities

### Non-Functional Requirements

#### Performance
- Fast local database operations
- Responsive UI for data entry
- Quick data retrieval and display

#### Usability
- Intuitive form-based interface
- Clear navigation and organization
- Minimal learning curve

#### Reliability
- Data persistence across sessions
- Error handling for invalid inputs
- Database integrity maintenance

## 🎨 UI/UX Design Principles

### Layout Philosophy
- **Form-First Design**: Prioritize data entry efficiency
- **Progressive Disclosure**: Show relevant sections based on context
- **Minimal Cognitive Load**: Simple, clear interface elements

### User Flow
1. **Session Creation**: User starts by logging a practice session
2. **Mistake Logging**: After session exists, user can log mistakes
3. **Data Review**: User can view historical data and patterns

### Design Patterns
- **Single Page Application**: All functionality on one page
- **Form-Based Interaction**: Primary interaction through forms
- **Immediate Feedback**: Success messages for completed actions

## 🔧 Technical Decisions

### Why Streamlit?
- **Rapid Prototyping**: Quick development and iteration
- **Python Ecosystem**: Leverage existing Python libraries
- **Built-in Components**: Forms, charts, and data display
- **Easy Deployment**: Simple sharing and deployment options

### Why SQLite?
- **Simplicity**: No server setup required
- **Portability**: Single file database
- **Reliability**: ACID compliance
- **Performance**: Sufficient for single-user application

### Why SQLAlchemy?
- **ORM Benefits**: Object-relational mapping
- **Database Agnostic**: Easy migration to other databases
- **Relationship Management**: Handle foreign keys elegantly
- **Query Builder**: Pythonic database queries

## 📊 Data Model Considerations

### Qur'ān Structure
- **30 Juz (Parts)**: Each juz divided into quarters
- **114 Suras (Chapters)**: Variable lengths
- **6,236 Ayahs (Verses)**: Specific addressing system

### Mistake Categories
- **Hifz (Memorization)**: Forgotten words, sequence errors
- **Tajweed (Recitation Rules)**: Pronunciation, elongation, pauses
- **Future Categories**: Rhythm, melody, emotional expression

### Session Types
- **Practice**: Regular memorization/review sessions
- **Test**: Formal recitation assessments
- **Future Types**: Group sessions, teacher evaluations

## 🚀 Development Phases

### Phase 1: MVP (Current)
- Basic session and mistake tracking
- Simple data viewing
- Core database functionality

### Phase 2: Enhanced UX
- Improved form organization
- Better data visualization
- Input validation and error handling

### Phase 3: Analytics
- Progress charts and trends
- Mistake pattern analysis
- Performance insights

### Phase 4: Advanced Features
- Multi-user support
- Data export/import
- Integration with external tools

## 🔒 Security & Privacy

### Data Privacy
- Local data storage (no cloud by default)
- User controls their own data
- No external data transmission

### Data Integrity
- Foreign key constraints
- Input validation
- Transaction management

## 📈 Future Considerations

### Scalability
- Potential migration to PostgreSQL
- Multi-user architecture
- Cloud deployment options

### Integration
- Qur'ān text APIs
- Audio recording capabilities
- Mobile app development

### Analytics
- Machine learning for mistake prediction
- Personalized improvement recommendations
- Community features for shared learning

---

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use type hints where appropriate
- Document functions with docstrings
- Keep functions under 50 lines when possible

### Database Guidelines
- Use SQLAlchemy ORM for all database operations
- Implement proper error handling
- Use transactions for data consistency
- Regular database backups (future)

### UI Guidelines
- Consistent form layouts
- Clear labeling and instructions
- Responsive design principles
- Accessibility considerations 
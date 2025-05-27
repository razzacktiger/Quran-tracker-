# 🕌 Qur'ān Recitation Tracker

A comprehensive digital tool to help students of the Qur'ān track their recitation practice, identify patterns in mistakes, and monitor their progress in both memorization (Hifz) and proper recitation (Tajweed).

## ✨ Features

- **📚 Session Tracking**: Record practice sessions with detailed metadata (Juz, quarter, duration, attention level)
- **❌ Mistake Logging**: Log and categorize mistakes with specific Sura:Ayah references
- **📊 Data Visualization**: View your practice history and mistake patterns
- **🔗 Linked Data**: Connect mistakes to specific practice sessions for better context
- **💾 Local Storage**: All data stored locally using SQLite database

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd Quran-tracker-
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

## 📖 How to Use

### 1. Record a Practice Session
- Fill out the session form with your practice details
- Select the Juz (1-30) and quarter (Q1-Q4) you practiced
- Choose session type (Practice or Test)
- Set duration and attention level
- Add any notes about your session
- Click "💾 Save Session"

### 2. Log Mistakes
- After creating a session, the mistake form will appear
- Select which session the mistake occurred in
- Enter the Sura:Ayah reference (e.g., "2:142")
- Choose mistake category (Hifz, Tajweed, Pronunciation, etc.)
- Describe the mistake and how to correct it
- Click "Log Mistake"

### 3. View Your Progress
- Use the checkboxes to view all sessions and mistakes
- Data is displayed in user-friendly tables
- Track patterns in your practice and improvement areas

## 🏗️ Project Structure

```
Quran-tracker-/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── tracker.db            # SQLite database (created automatically)
├── README.md             # This file
├── TASK.md               # Task tracking and features
├── PLANNING.md           # Project architecture and planning
├── .gitignore            # Git ignore rules
├── LICENSE               # Project license
└── venv/                 # Virtual environment (created by you)
```

## 🔧 Technical Details

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python with SQLAlchemy ORM
- **Database**: SQLite (local file-based database)
- **Data Models**: Sessions and Mistakes with foreign key relationships

## 📊 Database Schema

### Sessions Table
- **id**: Primary key
- **date**: Session date (auto-generated)
- **juz**: Juz number (1-30)
- **quarter**: Quarter of Juz (Q1-Q4)
- **session_type**: Practice or Test
- **duration**: Session duration in minutes
- **attention**: Attention level (1-5 scale)
- **notes**: Optional session notes

### Mistakes Table
- **id**: Primary key
- **session_id**: Links to Sessions table
- **sura_ayah**: Sura:Ayah reference (e.g., "2:142")
- **category**: Mistake type (Hifz, Tajweed, etc.)
- **description**: Mistake description
- **correction**: How to fix the mistake

## 🐛 Troubleshooting

### Common Issues

1. **NumPy compatibility error**
   - Solution: The requirements.txt includes compatible versions
   - If issues persist, run: `pip install "numpy<2.0" --upgrade`

2. **Streamlit not found**
   - Ensure virtual environment is activated
   - Run: `pip install streamlit`

3. **Database errors**
   - Delete `tracker.db` file to reset database
   - Restart the application

### Getting Help

- Check the [TASK.md](TASK.md) file for known issues
- Review [PLANNING.md](PLANNING.md) for technical details
- Create an issue in the repository for bugs or feature requests

## 🤝 Contributing

1. Read [PLANNING.md](PLANNING.md) for architecture details
2. Check [TASK.md](TASK.md) for current tasks and features
3. Follow the development guidelines in PLANNING.md
4. Submit pull requests with clear descriptions

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Future Features

- Progress analytics and charts
- Mistake pattern analysis
- Data export functionality
- Mobile-responsive design
- Multi-user support

---

**May Allah make this tool beneficial for your Qur'ān studies! 🤲**


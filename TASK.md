# TASK.md - Qur'ān Recitation Tracker

## 📋 Current Tasks & Features

### ✅ Completed Tasks
- [x] **Basic Streamlit App Setup** (2025-05-26)
  - Created main app.py with Streamlit interface
  - Set up SQLAlchemy database models for Sessions and Mistakes
  - Implemented basic forms for session and mistake logging

- [x] **Database Schema** (2025-05-26)
  - Session model: juz, quarter, session_type, duration, attention, notes
  - Mistake model: sura_ayah, category, description, correction
  - Established foreign key relationship between sessions and mistakes

- [x] **Dependency Management** (2025-05-26)
  - Fixed NumPy 2.x compatibility issues
  - Resolved Altair version conflicts
  - Updated SQLAlchemy imports to remove deprecation warnings
  - Created requirements.txt with version constraints

- [x] **Basic UI Components** (2025-05-26)
  - Session form with juz, quarter, type, duration, attention, notes
  - Mistake form linked to existing sessions
  - Data viewing checkboxes for sessions and mistakes

### ✅ Completed Tasks (Continued)
- [x] **UX Improvements** (2025-05-26)
  - Fixed mistake form visibility with helpful guidance message
  - Added better form organization with columns and help text
  - Improved data display formatting with user-friendly tables
  - Added section headers and emojis for better navigation
  - Enhanced session selection with descriptive text
  - Added input validation and error messages

- [x] **Documentation** (2025-05-26)
  - Created comprehensive TASK.md for project tracking
  - Created detailed PLANNING.md with architecture and requirements
  - Updated README.md with setup instructions and usage guide

- [x] **Enhanced Session Tracking** (2025-05-26)
  - Added mistake count field to session recording
  - Updated database schema with mistake_count column
  - Added progress tracking for mistake logging
  - Improved session display to show mistake counts
  - Added database migration for existing installations
  - Added custom date input for sessions (defaults to today)

### 📝 Planned Features

#### High Priority
- [ ] **Enhanced Mistake Tracking**
  - Add more mistake categories (Pronunciation, Rhythm, Pause, etc.)
  - Implement mistake severity levels
  - Add quick mistake templates for common errors

- [ ] **Progress Analytics**
  - Weekly/monthly progress charts
  - Mistake frequency analysis by juz/sura
  - Attention level trends over time
  - Session duration statistics

- [ ] **Data Visualization**
  - Progress charts using Plotly/Altair
  - Heatmap of mistakes by Qur'ān sections
  - Attention level trends
  - Session frequency calendar view

#### Medium Priority
- [ ] **Session Management**
  - Edit/delete existing sessions
  - Session templates for different practice types
  - Bulk session import/export
  - Session notes with rich text formatting

- [ ] **Mistake Analysis**
  - Mistake pattern recognition
  - Recurring mistake alerts
  - Improvement suggestions based on patterns
  - Mistake correction tracking

- [ ] **User Experience**
  - Dark/light theme toggle
  - Responsive design for mobile
  - Keyboard shortcuts for quick entry
  - Auto-save functionality

#### Low Priority
- [ ] **Advanced Features**
  - Multiple user support
  - Data backup/restore functionality
  - Integration with Qur'ān apps
  - Audio recording links for mistakes
  - Tajweed rule reference integration

### 🐛 Known Issues
- [ ] Mistake form only appears after creating at least one session
- [ ] Data display could be more user-friendly (raw database output)
- [ ] No data validation for Sura:Ayah format
- [ ] No confirmation dialogs for data operations

### 🔍 Discovered During Work
- [ ] Need better error handling for database operations
- [ ] Consider adding data export functionality (CSV/JSON)
- [ ] Implement session search and filtering
- [ ] Add data validation for input fields
- [ ] Consider adding undo functionality for accidental deletions

### 📊 Technical Debt
- [ ] Add unit tests for database models
- [ ] Implement proper error handling
- [ ] Add input validation and sanitization
- [ ] Consider database migration strategy
- [ ] Add logging for debugging

---

## 📝 Notes
- Project uses SQLite for simplicity and portability
- Streamlit chosen for rapid prototyping and ease of use
- Focus on Qur'ān memorization (Hifz) and Tajweed improvement
- Target users: Students of Qur'ān recitation and memorization 
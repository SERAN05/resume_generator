# 🚀 AI-Powered Resume & Cover Letter Generator

A professional resume and cover letter generator built with Streamlit and Python. Create industry-ready resumes with just a few clicks!

## 🌟 Features

- **Professional Layout**: Clean and modern resume design
- **PDF Generation**: Generate downloadable PDF resumes
- **Cover Letter**: Automatic cover letter generation
- **User-Friendly Interface**: Intuitive web-based form
- **Real-time Preview**: See your resume as you build it
- **Character Encoding**: Handles special characters safely

## 🛠️ Installation

1. **Clone or download this project**

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run resume_generator.py
   ```

4. **Open your browser** and go to `http://localhost:8501`

## 📋 How to Use

1. **Fill Personal Information** (Required):
   - Full Name *
   - Email *
   - Phone Number *
   - LinkedIn (Optional)
   - GitHub (Optional)
   - Address (Optional)

2. **Complete Resume Sections**:
   - Career Objective/Summary
   - Skills
   - Education
   - Work Experience
   - Projects
   - Achievements & Certifications
   - References (Optional)

3. **Generate PDF**:
   - Click "Generate Resume PDF" button
   - Download your professional resume
   - Includes both resume and cover letter

## 📁 Files

- `resume_generator.py` - Main application file
- `requirements.txt` - Python dependencies
- `README.md` - This documentation file

## 🔧 Technical Details

- **Built with**: Streamlit (Web Framework) + FPDF (PDF Generation)
- **Python Version**: 3.7+
- **PDF Features**: Professional formatting, character encoding, error handling
- **File Management**: Temporary file handling for security

## 🚨 Troubleshooting

**Common Issues:**

1. **Module not found**: Run `pip install -r requirements.txt`
2. **PDF generation fails**: Check that all required fields are filled
3. **Special characters**: The app automatically handles special character encoding

**Error Messages:**
- "Please fill at least Name, Email, and Phone Number" - Required fields missing
- "Error generating PDF" - Check your input for invalid characters

## 💡 Tips for Best Results

1. **Be Specific**: Add detailed work experience and achievements
2. **Use Action Words**: Start bullet points with action verbs
3. **Quantify Results**: Include numbers and percentages when possible
4. **Keep it Concise**: 2-3 lines for summary, bullet points for details
5. **Proofread**: Review content before generating PDF

## 🔮 Future Enhancements

- Multiple resume templates
- LinkedIn integration
- AI-powered content suggestions
- Export to different formats
- Resume analysis and scoring

---

**Happy Job Hunting! 🎯**
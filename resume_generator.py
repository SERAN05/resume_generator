import streamlit as st
from fpdf import FPDF
import os
import tempfile
import sys

st.set_page_config(page_title="AI Resume Builder", layout="wide")

st.title("🚀 AI-Powered Resume & Cover Letter Generator")
st.write("Fill in your details and download a professional, industry-ready resume with cover letter.")

# Add instructions
st.info("💡 **Instructions:** Fill in the required fields (marked with *) and optional fields as needed. Click 'Generate Resume PDF' to create and download your professional resume.")

# Add encoding tip
st.warning("⚠️ **Character Notice:** If you copy text from Word or other sources, the app will automatically convert special characters (smart quotes, em-dashes, bullets, etc.) to PDF-compatible formats.")

# Add character conversion examples
with st.expander("🔄 Character Conversions (Click to expand)"):
    st.write("**The app automatically converts these characters:**")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**From (Word/Web):**")
        st.code("Smart quotes: " " → \" \"")
        st.code("En dash: – → -")
        st.code("Em dash: — → -")
        st.code("Bullets: • → *")
        st.code("Ellipsis: … → ...")
    with col2:
        st.write("**Symbols:**")
        st.code("Trademark: ™ → (TM)")
        st.code("Copyright: © → (C)")
        st.code("Euro: € → EUR")
        st.code("Pound: £ → GBP")
        st.code("Plus-minus: ± → +/-")

# ================= Sidebar =================
st.sidebar.header("👤 Personal Information")
st.sidebar.markdown("*Required fields")
name = st.sidebar.text_input("Full Name *")
email = st.sidebar.text_input("Email *")
phone = st.sidebar.text_input("Phone Number *")
linkedin = st.sidebar.text_input("LinkedIn (Optional)")
github = st.sidebar.text_input("GitHub (Optional)")
address = st.sidebar.text_area("Address (Optional)")

# ================= Resume Fields =================
st.subheader("🎯 Career Objective / Summary")
summary = st.text_area("Write 2–3 lines about your professional background and career goals", height=100)

st.subheader("🛠️ Skills")
skills = st.text_area("List your skills (comma separated)", height=80, 
                      placeholder="Python, Java, Machine Learning, Project Management")

st.subheader("🎓 Education")
education = st.text_area("Add your education details", height=120,
                         placeholder="Bachelor of Science in Computer Science\nXYZ University, 2020-2024\nGPA: 3.8/4.0")

st.subheader("💼 Work Experience")
experience = st.text_area("Add your work experience", height=150,
                          placeholder="Software Engineer\nABC Company, Jan 2024 - Present\n• Developed web applications using Python and Django\n• Collaborated with cross-functional teams")

st.subheader("📂 Projects")
projects = st.text_area("Add projects with short description", height=120,
                        placeholder="E-commerce Website\n• Built using React and Node.js\n• Implemented payment gateway integration")

st.subheader("🏆 Achievements & Certifications")
achievements = st.text_area("Awards, Certifications, Achievements", height=100,
                           placeholder="AWS Certified Solutions Architect\nDean's List 2023\nHackathon Winner")

st.subheader("🤝 References")
references = st.text_area("References (Optional)", height=80,
                          placeholder="Available upon request")

# ================= Generate PDF =================
if st.button("📄 Generate Resume PDF"):
    if not name or not email or not phone:
        st.warning("⚠️ Please fill at least Name, Email, and Phone Number.")
    else:
        try:
            pdf = FPDF()
            pdf.add_page()

            # Use built-in fonts to avoid font issues
            pdf.set_font("Arial", "B", 16)
            
            # Helper function to safely encode text
            def safe_encode(text):
                if not text:
                    return ""
                # Replace problematic Unicode characters with ASCII equivalents
                replacements = {
                    # Dashes
                    '—': '-',      # em dash
                    '–': '-',      # en dash (\u2013)
                    '−': '-',      # minus sign
                    # Quotes
                    ''': "'",      # left single quote
                    ''': "'",      # right single quote
                    '"': '"',      # left double quote
                    '"': '"',      # right double quote
                    '„': '"',      # double low-9 quote
                    # Bullets and symbols
                    '•': '*',      # bullet
                    '◦': '*',      # white bullet
                    '‣': '*',      # triangular bullet
                    '…': '...',    # ellipsis
                    '®': '(R)',    # registered symbol
                    '™': '(TM)',   # trademark symbol
                    '©': '(C)',    # copyright symbol
                    # Currency
                    '€': 'EUR',    # euro
                    '£': 'GBP',    # pound
                    # Math symbols
                    '≤': '<=',     # less than or equal
                    '≥': '>=',     # greater than or equal
                    '≠': '!=',     # not equal
                    '±': '+/-',    # plus-minus
                }
                
                # Apply replacements
                for old, new in replacements.items():
                    text = text.replace(old, new)
                
                # Convert remaining non-ASCII characters
                try:
                    # Try to encode as latin-1, replace problematic chars
                    text = text.encode('latin-1', 'replace').decode('latin-1')
                except:
                    # If that fails, use ASCII encoding
                    text = text.encode('ascii', 'replace').decode('ascii')
                
                return text

            # Header
            pdf.cell(0, 10, safe_encode(name), ln=True, align="C")
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 8, f"Email: {safe_encode(email)} | Phone: {safe_encode(phone)}", ln=True, align="C")
            if linkedin or github:
                pdf.cell(0, 8, f"LinkedIn: {safe_encode(linkedin)} | GitHub: {safe_encode(github)}", ln=True, align="C")
            if address:
                pdf.cell(0, 8, f"Address: {safe_encode(address)}", ln=True, align="C")

            # Function to add sections
            def add_section(title, content):
                if content and content.strip():
                    pdf.set_font("Arial", "B", 14)
                    pdf.ln(6)
                    pdf.cell(0, 8, safe_encode(title), ln=True)
                    pdf.set_font("Arial", "", 12)
                    # Split content into smaller chunks to avoid issues
                    content_safe = safe_encode(content)
                    
                    # Additional validation for problematic characters
                    try:
                        # Test if content can be encoded as latin-1
                        content_safe.encode('latin-1')
                        pdf.multi_cell(0, 6, content_safe)
                    except UnicodeEncodeError as e:
                        # If encoding fails, create a more aggressive replacement
                        content_cleaned = ''.join(char if ord(char) < 256 else '?' for char in content_safe)
                        pdf.multi_cell(0, 6, content_cleaned)

            add_section("Career Objective", summary)
            add_section("Skills", skills)
            add_section("Education", education)
            add_section("Work Experience", experience)
            add_section("Projects", projects)
            add_section("Achievements & Certifications", achievements)
            add_section("References", references)

            # Cover Letter
            if name:
                cover_letter_text = f"""Dear Hiring Manager,

I am writing to express my interest in the position at your organization. Based on my background and skills outlined in this resume, I believe I would be a valuable addition to your team.

My experience and qualifications align well with the requirements, and I am excited about the opportunity to contribute to your organization's success.

Thank you for considering my application. I look forward to hearing from you.

Best Regards,
{safe_encode(name)}"""
                add_section("Cover Letter", cover_letter_text)

            # Create temporary file for PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                pdf_path = tmp_file.name
            
            # Save PDF
            pdf.output(pdf_path, "F")

            # Read PDF and provide download
            with open(pdf_path, "rb") as f:
                pdf_data = f.read()
                st.download_button(
                    "⬇️ Download Resume PDF", 
                    pdf_data, 
                    file_name=f"{safe_encode(name)}_resume.pdf" if name else "resume.pdf",
                    mime="application/pdf"
                )
            
            # Clean up temporary file
            try:
                os.unlink(pdf_path)
            except:
                pass
                
            st.success("✅ Resume PDF generated successfully! Click the download button above.")
            
        except UnicodeEncodeError as e:
            st.error("❌ Character encoding error: Your text contains special characters that couldn't be processed.")
            st.error("💡 Try removing or replacing special characters like fancy quotes, dashes, or symbols.")
            st.error("Example: Replace '–' with '-', '•' with '*', or smart quotes with regular quotes")
        except Exception as e:
            st.error(f"❌ Error generating PDF: {str(e)}")
            st.error("Please check your input and try again.")

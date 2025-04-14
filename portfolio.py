import streamlit as st
from PIL import Image
import base64
import streamlit.components.v1 as components

# --- Page Config ---
st.set_page_config(page_title="Abhijit Sarkar | Portfolio", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

# --- Load Files ---
try:
    profile_image = Image.open("profile.jpg")
except FileNotFoundError:
    st.error("Profile image 'profile.jpg' not found. Please add it to the directory.")
    profile_image = None

def get_pdf_download_link(pdf_file_path):
    try:
        with open(pdf_file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        return f'<a href="data:application/pdf;base64,{base64_pdf}" download="Abhijit_Sarkar_Resume.pdf"><b>📄 Download Resume</b></a>'
    except FileNotFoundError:
        return "<p style='color: #E0E0E0;'>Resume file not found.</p>"

# --- Convert hd.jpg to base64 for reliable background loading ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error("Background image 'hd.jpg' not found. Please ensure it's in the same directory as this script.")
        return ""

# --- Sidebar ---
with st.sidebar:
    if profile_image:
        st.image(profile_image, width=150)
    st.markdown("<h2 style='color: #26A69A;'>Abhijit Sarkar</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #E0E0E0;'>📧 <i>abhijit.sarkar-26@bibs.co.in</i></p>", unsafe_allow_html=True)
    st.markdown("<p style='color: #E0E0E0;'>📞 <i>+91-9832533129</i></p>", unsafe_allow_html=True)
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/abhijit-sarkar-5b2612280/" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="30" style="margin-right: 10px;">
        </a>
        <a href="https://github.com/Abhi0823" style="text-decoration: none;">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30">
        </a>
        """,
        unsafe_allow_html=True
    )
    st.markdown(get_pdf_download_link("Abhijit_Sarkar_Resume.pdf"), unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)

# --- Main Content ---
st.markdown("<h1 style='color: #26A69A;'>👨‍💻 Portfolio</h1>", unsafe_allow_html=True)

st.markdown("---")

# --- Skills ---
st.header("🛠️ Skills")
st.markdown("""
- **Languages:** Python, SQL  
- **Technologies & Tools:** Excel, Power BI, Machine Learning, Statistics  
- **Libraries:** Pandas, Matplotlib, Plotly
""", unsafe_allow_html=True)

# --- Internship ---
st.header("💼 Internship")
st.subheader("Elite Tech Intern (Nov 2024 – Jan 2025)")
st.markdown("""
**Role:** Data Scientist Intern  
- Data exploration, visualisation, and ML  
- Analyzed cuisines using Power BI and Python  
- [📁 Internship Link](https://drive.google.com/drive/folders/1yDmeRUXheY-d5JErLJeG6La4Hlyt4tHe)
""")

# --- Education ---
st.header("🎓 Education")
col1, col2 = st.columns(2)
with col1:
    st.subheader("PGPBA & DS + MBA (2024 – 2026)")
    st.write("**Institute:** Bengal Institute of Business Studies")
with col2:
    st.subheader("B.Com (H) Accountancy (2021 – 2024)")
    st.write("**University:** Adamas University – 70%")

# --- Projects ---
st.header("📂 Project Work")
st.subheader("Unemployment Analysis with Python")
st.markdown("""
- Handled missing data  
- Visualized trends using Seaborn & Matplotlib  
- Analyzed unemployment rates
""")
st.subheader("📊 Embedded Power BI Report")
st.markdown("PowerBi report for Spotify")
try:
    st.image("bidash.jpg", width=1000)
except FileNotFoundError:
    st.error("Image 'bidash.jpg' not found.")

# --- Certifications ---
st.header("📜 Certifications")
st.markdown("""
- **Machine Learning with Python** – *IIT Kanpur*  
  - Supervised: Linear Regression, SVM, Decision Trees  
  - Unsupervised: Clustering, Dimensionality Reduction
""")

# --- Interests ---
st.header("🎸 Interests")
st.markdown("- Singing  \n- Gym  \n- Playing Guitar")

# --- Contact Form ---
st.header("📬 Contact Me")
contact_form = """
<form action="https://formsubmit.co/your_email@example.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="Name" placeholder="Your name" required><br><br>
    <input type="email" name="Email" placeholder="Your email" required><br><br>
    <textarea name="Message" placeholder="Your message here" required></textarea><br><br>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='color: #E0E0E0;'>Made with ❤️ using Streamlit by <b>Abhijit Sarkar</b></p>", unsafe_allow_html=True)

# --- Custom CSS for Styling ---
base64_bg = get_base64_image("hd.jpg")
st.markdown(f"""
<style>
.stApp {{
    background: url('data:image/jpg;base64,{base64_bg}') no-repeat center center fixed;
    background-size: cover;
}}
body {{
    color: #E0E0E0;
}}
h1, h2, h3, h4, h5, h6 {{
    color: #26A69A;
}}
input, textarea {{
    width: 100%;
    padding: 10px;
    border-radius: 5px;
    background-color: rgba(30, 30, 30, 0.8);
    color: #E0E0E0;
    border: 1px solid #26A69A;
}}
button {{
    padding: 10px 20px;
    background-color: #26A69A;
    color: #121212;
    border: none;
    border-radius: 5px;
    font-weight: bold;
}}
button:hover {{
    background-color: #4DB6AC;
}}
.stMarkdown a {{
    color: #26A69A;
    text-decoration: none;
}}
.stMarkdown a:hover {{
    color: #4DB6AC;
}}
</style>
""", unsafe_allow_html=True)
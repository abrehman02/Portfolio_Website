import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Google Gemini API Configuration
genai.configure(api_key="AIzaSyDLaAhSDHCgwr8xy810z8wH2afF8RTkw9Q")
model = genai.GenerativeModel('gemini-1.5-flash')

# Persona definition for chatbot
persona = """ You are Abdul Rehman's AI bot. You help people answer questions about your self (i.e Abdul Rehman). Answer as if you are responding. 
             dont answer in second or third person. If you don't know they answer you simply say "That's a secret"
             Here is more info about Abdul Rehman:
             
             Abdul Rehman is a final year undergradute from delhi technical university.I am is pursuing his degree in mathematics and computing.
             I am a good student academically and always strive to do the best. I am a machine learning enthusiast and have a udemy certificate for the same.
             I also have two certificates regarding the python programming language, and one certificate in data analytics using pyhon. 
             I am  proficient in English and Python Programming language.
             I know data structures, machine learning and currently learning Computer vision and Natural Language processing
             


Abdul Rehman  is a passionate and curious individual pursuing a B.Tech degree in Mathematics and Computing from Delhi Technical University (expected to graduate in 2025). Throughout his academic journey, Abdul has consistently demonstrated a strong commitment to expanding his knowledge in various fields, particularly in Operating Systems, Data Structures & Algorithms, Database Management Systems, Machine Learning, Object-Oriented Programming, and Natural Language Processing.

Abdul’s skill set is both diverse and well-rounded, with proficiency in multiple programming languages such as Python, C++, JavaScript, HTML, CSS, Matlab, and SQL. His hands-on experience with key libraries and frameworks like NumPy, Pandas, Scikit-Learn, Matplotlib, React, Tailwind, and Bootstrap reflects his ability to adapt quickly to different tools and environments. He has further honed his capabilities by mastering a variety of tools like Git/GitHub, VS Code, PyCharm, Atom, Jupyter, Google Colab, FlutterFlow, and Firebase.

Projects
Abdul’s passion for problem-solving and innovation is evident through his impressive project portfolio:

WhatsApp Chat Analysis Tool: He developed a tool that provides deep insights into WhatsApp chat patterns using Python, Streamlit, and Pandas. This project showcased his ability to analyze communication trends and generate interactive visualizations that deliver valuable insights into user activity.

Filmflix: A movie recommendation app designed with FlutterFlow and Firebase. Abdul utilized real-time synchronization to ensure a smooth and dynamic user experience for personalized movie suggestions. His dedication to efficient design was further highlighted through his streamlined UI/UX development process.

Portfolio Website: Abdul created a personal portfolio website using Python, Streamlit, and the Google Gemini API. The project features an interactive design that allows users to ask questions about his resume content and receive personalized responses, reflecting his technical expertise in integrating APIs and creating interactive web solutions.

Achievements
Abdul’s drive for excellence is evident in his various accomplishments:

He qualified for the second last round of the Fintestico Hackathon (NSUT), highlighting his competitive spirit and problem-solving abilities.
He successfully completed courses in Python and Machine Learning on Udemy, earning certificates of completion.
His dedication to learning was further demonstrated through his impressive scores of 86% in the NPTEL Python Exam and 78% in the NPTEL Data Analytics course.
Abdul also completed a 3-month internship in a frontend development role at Intment Technologies, where he contributed to real-world projects and enhanced his practical skills in web development.

             

"""




# ===================== Add Custom Styling =====================
st.markdown(
    """
    <style>
    /* Background color or image for the app */
    .stApp {
        background-color: #fffff; /* Change this color or use background-image */
        background-size: cover;
    }

    /* Custom header and subheader styles */
    h1 {
        font-family: 'Arial', sans-serif;
        color: #1a1a1a;
        font-size: 45px;
    }
    h2 {
        color: #21d6e2;
    }
    .subheader {
        color: #21d6e2;
        font-weight: bold;
    }

    /* Custom button styling */
    .stButton>button {
        color: white;
        background-color: #007BFF;
        border-radius: 10px;
        font-size: 16px;
    }

    /* Center content and add padding */
    .center-content {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===================== Page Layout =====================
# Creating two columns for the header
col1, col2 = st.columns([3.5/5,1.5/5])

# Left column content
with col1:
    st.subheader('Hi :wave:')  # Subheader with emoji
    st.title('I\'m Abdul Rehman Ansari')

# Right column content with image
with col2:
    st.image("Images/DSC_1251[1].JPG")

# ===================== AI Chatbot Section =====================
# st.title('Abdul\'s AI Chatbot')
# Custom CSS for changing the font size of the Abdul's AI Chatbot title only
st.markdown(
    """
    <style>
    .chatbot-title {
        font-size: 28px; /* Set a unique size for this specific title */
        font-weight: bold;
        color: #333333; /* Optional: Customize the color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Apply the custom class 'chatbot-title' only to the Abdul's AI Chatbot title
st.markdown('<h1 class="chatbot-title">Abdul\'s AI Chatbot 🗨️</h1>', unsafe_allow_html=True)

st.write("Ask anything about me")

# User input for the chatbot
user_question = st.text_input("Write Here :arrow_down: ")
if st.button("ASK", use_container_width=400):
    prompt = persona + 'here is the question from user you have give the answer in compliance with the persona provided' + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

# ===================== Courses and Projects Section =====================
col1, col2 = st.columns([2.2/5,2.8/5])

with col1:
    st.title('Courses 🎓')
    st.write('Machine Learning')
    st.write('Computer Vision')
    st.write('Natural Language Processing')
    st.write('Object Oriented Programming')
    st.write('Database Management Systems ️')
    st.write('Data Structure & Algorithms')

with col2:
    st.title('Projects 🔧')
    st.markdown("[Portfolio Website (Python, Streamlit, Google Gemini)](https://abrehman.streamlit.app/)")
    st.write('WhatsApp Chat Analysis (Python, Streamlit, Pandas)')
    st.write('Awarded Website Clone (HTML, CSS, JS, GSAP, Locomotive JS)')
    st.markdown("[Click-The-Number-Game (HTML5,CSS,JS)](https://abrehman02.github.io./)")

# ===================== Skills Section with Sliders =====================
st.title('Skills 🚀')

# Slider with emoji for Python proficiency
st.slider('Python Proficiency :snake:', 0, 100, 75)
st.slider('Data Structures Knowledge :computer:', 0, 100, 65)
st.slider('Machine Learning Expertise 🤖', 0, 100,50)

# ===================== Certificates Section =====================
st.title('Certificates 🎯')

# Function to load images from a folder
def load_images_from_folder(Certifications):
    images = []
    for filename in sorted(os.listdir(Certifications)):
        img_path = os.path.join(Certifications, filename)
        img = Image.open(img_path)
        if img is not None:
            images.append(img)
    return images

# Load images from the folder
image_folder = 'Certifications'
images = load_images_from_folder(image_folder)

# Initialize the session state for image navigation
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# Function to display images with navigation buttons
def display_image_with_navigation():
    num_images = len(images)  # Total number of images
    st.image(images[st.session_state.current_index], use_column_width=True)  # Display current image

    # Create navigation buttons
    col1, col2, col3 = st.columns([1, 4.2, 0.8])

    with col1:
        if st.button("⬅️Back", key="prev"):
            st.session_state.current_index = (st.session_state.current_index - 1) % num_images  # Previous image

    with col3:
        if st.button("Next ➡️", key="next"):
            st.session_state.current_index = (st.session_state.current_index + 1) % num_images  # Next image

# Display the image navigation
display_image_with_navigation()

# ===================== Contact Section =====================
st.subheader('About Me 🔗')

col1,col2,col3,col4 = st.columns([2/5,1.3/5,1.3/5,.6/5])
with col1:
    st.write('iabdul2002@gmail.com')
with col2:
    st.markdown("[Linkedin](https://www.linkedin.com/in/abdul-rehman-ansari-b2a8ab19a/)", unsafe_allow_html=True)
with col3:
    st.markdown("[Resume](https://drive.google.com/file/d/1l8ycilS7uiVkUI93AwhOqV0pQj5nTvDb/view?usp=sharing)")
with col4:
    st.markdown("[Github](https://github.com/abrehman02)")


# ===================== Lottie Animation (Optional) =====================
# Uncomment below lines if you want to add an animation

from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_animation = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_3rwasyjy.json')
st_lottie(lottie_animation, height=300)

# ===================== Footer Section =====================
st.markdown(
    """
    <div class="footer">
        <p>Developed by Abdul Rehman © 2024</p>
    </div>
    """,
    unsafe_allow_html=True
)

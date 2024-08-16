import streamlit as st
import os
from PIL import Image
import google.generativeai as genai


api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

persona = """ You are Abdul Rehman's AI bot. You help people answer questions about your self (i.e Abdul Rehman). Answer as if you are responding. 
             dont answer in second or third person. If you don't know they answer you simply say "That's a secret"
             Here is more info about Abdul Rehman:
             
             Abdul Rehman is a final year undergradute from delhi technical university.I am is pursuing his degree in mathematics and computing.
             I am a good student academically and always strive to do the best. I am a machine learning enthusiast and have a udemy certificate for the same.
             I also have two certificates regarding the python programming language, and one certificate in data analytics using pyhon. 
             I am  proficient in English and Python Programming language.
             I know data structures, machine learning and currently learning Computer vision and Natural Language processing"""





col1, col2 = st.columns(2)


with col1:
    st.subheader('Hi :wave:')
    st.title('I am Abdul Rehman Ansari')
    st.title('')


with col2:
    st.image("Images/ME.png")


st.title('Abdul\'s AI chatbot')
st.write("Ask anything about me")
user_question = st.text_input("Write Here :arrow_down: ")
if st.button("ASK", use_container_width=400):
    prompt = persona +  'here is the question from user you have give the answer in compliance with the persona provided'   +user_question
    response = model.generate_content(prompt)
    st.write(response.text)



col1 , col2 = st.columns(2)


with col1:
    st.title('Courses')
    st.write('Machine Learning')
    st.write('Computer Vision')
    st.write('Natural Language Processing')
    st.write('Data Structures')
    st.write('Object Oriented Programming')
    st.write('Database Management Systems')


with col2:
    st.title("Projects")
    st.write('1. Portfolio Website (Python, Streamlit ,Google Gemini')
    st.write('2. Whatsapp Chat Analysis (Python , Streamlit , Pandas')
    st.write('3.  Awarded website(clone)(HTML, CSS, Javascript, GSAP, Locomotive JS')
    st.write('4. ')


st.title('Skills')
st.slider('Python',0,100,75)
st.slider('Data Structures',0,100,50)
st.slider('Machine Learning',0,100,25)

st.title('Certificates')

# Function to load images from a directory

# Function to load images from a directory
def load_images_from_folder(Certifications):
    images = []
    for filename in sorted(os.listdir(Certifications)):
        img_path = os.path.join(Certifications, filename)
        img = Image.open(img_path)
        if img is not None:
            images.append(img)
    return images


# Load images from a folder
image_folder = 'Certifications'
images = load_images_from_folder(image_folder)

# Initialize the session state for the current image index
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0


# Function to display the image and navigation buttons
def display_image_with_navigation():
    # Get the total number of images
    num_images = len(images)

    # Display the current image
    st.image(images[st.session_state.current_index], use_column_width=True)

    # Create navigation buttons
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("⬅️ Previous", key="prev"):
            # Update the current index to show the previous image
            st.session_state.current_index = (st.session_state.current_index - 1) % num_images

    with col3:
        if st.button("Next ➡️", key="next"):
            # Update the current index to show the next image
            st.session_state.current_index = (st.session_state.current_index + 1) % num_images


# Display the image with navigation
display_image_with_navigation()


st.subheader('CONTACTS')
st.write('For any queries mail to :')
st.write('iabdul2002@gmail.com')



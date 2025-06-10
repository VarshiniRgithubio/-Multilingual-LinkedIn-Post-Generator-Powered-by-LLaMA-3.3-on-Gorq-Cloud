# importing the streamlit app
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from data.post_generator import generate_post
from data.few_shot import FewShotPosts
fs=FewShotPosts()
def main():
    st.title("Multilingual Linkdin Post Generator")

# multiple controlar in same row 
    col1, col2, col3 =st.columns(3)
    with col1:
        # processed post files that can be displed on this use the variable select tag someone click on it it will save into that variable
        selected_tag=st.selectbox("Title",options=fs.get_tags())
    # next box about the length
    with col2:
        selected_length=st.selectbox("Length",options=["Short","Medium","Long"])
    with col3:
        selected_language=st.selectbox("language",options=["English","Hindi+English=Hinglish","Kannada","Hindi","Telugu","korean","japanese","chinese"])

   
    if st.button("Generate"):
        post = generate_post(selected_length.lower(), selected_language, selected_tag)
        st.write(post)
            

if __name__ =="__main__":
    main()
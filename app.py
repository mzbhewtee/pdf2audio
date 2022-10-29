
from itertools import count


try:
    
    import requests
    # from streamlit_lottie import st_lottie
    import csv
    from backend import *
    import streamlit as st
    import pandas as pd
    import os
    from PyPDF2 import PdfFileReader

    st.set_page_config(page_title="PDF to Audio", page_icon=":music:", layout="wide")

    # def load_url(url):
    #     r = requests.get(url)
    #     if r.status_code != 200:
    #         return None
    #     return r.json()

    # def css(file_name):
    # with open(file_name) as f:
    #     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # css("style/style.css")

    # animation = load_url("https://assets9.lottiefiles.com/packages/lf20_49rdyysj.json")
    # animation2 = load_url("https://assets5.lottiefiles.com/packages/lf20_mbrocy0r.json")

    # image = Image.open("uploads/image.png")

    def save(uploadedfile):
        with open(os.path.join("uploads", uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer())
        return st.success("Running file :{} in uploads".format(uploadedfile.name))
    
    def pdf_to_text(pdf_path):
        # Open the file
        pdf = PdfFileReader(pdf_path)
        # Get the first page
        # with open('sample.txt', 'w', encoding='utf-8') as output:
            
            # # Loop through the pages
            # for page in range(pdf.getNumPages()):
            #     # Extract the text
            #     pageObj = pdf.getPage(page)

            #     try:
            #         texts = pageObj.extractText()
                    
            #     except:
            #         pass
            #     else:
            #         output.write(f'Page {0}\n:'.format(page + 1))
            #         output.write(texts)

        pdf = PdfFileReader(pdf_path)
        count = pdf.getNumPages()
        text = ""
        for i in range(count):
            page = pdf.getPage(i)
            text += page.extractText()
        # Return the text
            return text

    def main():
        st.title("PDF to Audio")
        st.header("Upload your pdf file here")
        data_file = st.file_uploader("uploads", type=["pdf"])
        if data_file is not None:
            file_details = {data_file.name, data_file.size}
            # st.write(file_details)
            text = pdf_to_text(data_file)
            text_to_speech_english(text)
            # x = translate_text(text)
            # st.write(x)
            # text_to_speech_french(text)

            with st.container():

                # left_column, right_column = st.columns(2)

                # with left_column:
                if st.button("Listen in English"):
                    st.audio("sample.mp3")
                    os.remove("sample.mp3")
                # with right_column:
                #     st.button("Listen in French")
                        # st.audio("sampleF.wav")
            
        
       
            # ----Short Note about the program, how it works---
        with st.container():
            st.write("---")
            
        with st.container():
            st.header("How this application works")
                
            st.write("This application converts your pdf file to an audio file. It uses the Microsoft Azure Cognitive Services to convert the text in the pdf file to speech. The application uses the Davis Neural voice to convert the text to speech. The application also uses the Streamlit library to create the web application. The application is hosted on Heroku. The application is still in development and will be updated with more features in the future.")


            
          
    main()
except Exception as e:
    print(e)

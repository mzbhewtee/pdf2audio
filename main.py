from distutils import text_file
from fileinput import filename
from urllib import request
import azure.cognitiveservices.speech as speech
from PyPDF2 import PdfFileReader
from pathlib import Path
# import pyttsx3
import requests, os, uuid, json
from dotenv import load_dotenv
import requests
 # from streamlit_lottie import st_lottie
import csv
    # from backend import *
import streamlit as st
import pandas as pd
import os
    # from PyPDF2 import PdfFileReader
load_dotenv()

def pdf_to_text(pdf_path):
        # Open the file
        pdf = PdfFileReader(pdf_path)
        # Get the first page
        with open('sample.txt', 'w', encoding='utf-8') as output:
            
            # Loop through the pages
            for page in range(pdf.getNumPages()):
                # Extract the text
                pageObj = pdf.getPage(page)

                try:
                    texts = pageObj.extractText()
                    
                except:
                    pass
                else:
                    output.write(f'Page {0}\n:'.format(page + 1))
                    output.write(texts)

        
        # Return the text
                return texts

def text_to_speech_english(texts):
        # Create an instance of a speech config with specified subscription key and service region.
        # Replace with your own subscription key and service region (e.g., "westus").
        speech_key, service_region = os.environ.get('apikey'), os.environ.get('location')
        speech_config = speech.SpeechConfig(subscription=speech_key, region=service_region)

        audio_config = speech.audio.AudioOutputConfig(use_default_speaker=True, filename='sample.mp3')

        speech_config.speech_synthesis_voice_name='en-US-DavisNeural'

        # Creates a speech synthesizer using the default speaker as audio output.
        speech_synthesizer = speech.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        # Receives a text from console input and synthesize it to speech.
        # The synthesized speech is expected to be heard on the speaker with this line executed.
        result = speech_synthesizer.speak_text_async(texts).get()

        # Checks result.
        if result.reason == speech.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized to speaker for text [{}]".format(texts))
        elif result.reason == speech.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speech.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
            print("Did you update the subscription info?")
            
        return result

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
                if st.button("Listen"):
                    st.audio("sample.mp3")
                    os.remove("sample.mp3")
                    # st.success("Finished Playing")
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
# except Exception as e:
#     print(e)
try:

    from distutils import text_file
    from fileinput import filename
    from urllib import request
    import azure.cognitiveservices.speech as speech
    from PyPDF2 import PdfFileReader
    from pathlib import Path
    # import pyttsx3
    import requests, os, uuid, json
    from dotenv import load_dotenv
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

    # def read_textfile():
    #     f = open('./sample.txt', 'rb')
    #     data = f.read().decode('utf8', 'ignore')
    #     return data


    # def text_to_speech(text):
    # text2speech = pyttsx3.init()

    # Get the voices
    # text2speech.say(content)
    # text2speech.setProperty('rate', 200)
    # text2speech.setProperty('volume', 0.9)
    # text2speech.runAndWait()

    # text_to_speech(content)
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

    def translate_text():
        # Add your subscription key and endpoint
        subscription_key = os.environ.get('translationkey')
        endpoint = os.environ.get('endpoint2')
        location = os.environ.get('location2')

        original_text = 'sample.txt'
        path = '/translate?api-version=3.0'
        params = '&to=fr'
        constructed_url = endpoint + path + params

        headers = {
            'Ocp-Apim-Subscription-Region': location,
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': original_text
        }]
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()

        

        translation = response[0]['translations'][0]['text']

        print(translation)
        return translation

    def text_to_speech_french(texts):
        # Create an instance of a speech config with specified subscription key and service region.
        # Replace with your own subscription key and service region (e.g., "westus").
        speech_key, service_region = os.environ.get('apikey'), os.environ.get('location')
        speech_config = speech.SpeechConfig(subscription=speech_key, region=service_region)

        audio_config = speech.audio.AudioOutputConfig(use_default_speaker=True, filename='sampleF.wav')

        speech_config.speech_synthesis_voice_name='fr-FR-JeromeNeural'

        # Creates a speech synthesizer using the default speaker as audio output.
        speech_synthesizer = speech.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        # Receives a text from console input and synthesize it to speech.
        # The synthesized speech is expected to be heard on the speaker with this line executed.
        result = speech_synthesizer.speak_text_async(translate_text(texts)).get()

        # Checks result.
        if result.reason == speech.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized to speaker for text [{}]".format(''))
        elif result.reason == speech.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speech.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
            print("Did you update the subscription info?")
            
        return result

    # x = (pdf_to_text('sample.pdf'))
    # # text_to_speech_french(x)
    # # # y = read_textfile()
    # # text_to_speech_english(x)
    # text_to_speech_french(translate_text())
  
    

except Exception as e:
    print(e)
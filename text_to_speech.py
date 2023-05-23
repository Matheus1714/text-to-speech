# Import required libraries
from google.cloud import texttospeech
from google.oauth2 import service_account

import os
import json

# Read credentials

file_name = 'alfa3-bd-b8b2ffe1ca15.json'
credentials = service_account.Credentials.from_service_account_file(file_name)
# with open(file_name, 'rb') as f:
#     credentials = json.load(f)

# Create a client instance of the Text-to-Speech API
client = texttospeech.TextToSpeechClient(credentials=credentials)

# Read text file
text = ''
with open('text.txt', 'rb') as f:
    text = f.read().decode('utf-8')
    text = text.replace('\r','')
    text = text.replace('\t','')

# Set the text input for synthesis
text_input = texttospeech.SynthesisInput(text=text)

# Set the voice parameters
voice = texttospeech.VoiceSelectionParams(
    language_code="pt-BR", ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

# Set the audio file format and audio encoding parameters
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech synthesis
response = client.synthesize_speech(
    input=text_input, 
    voice=voice, 
    audio_config=audio_config
)

# Write the audio file to disk
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

# Play the audio file
os.system("start output.mp3")
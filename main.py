import os
import requests
import json
import boto3
from pygame import mixer
import io
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API and AWS credentials
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_REGION = os.getenv('AWS_REGION')


def get_chatgpt_response(prompt):
    """
    Send a prompt to ChatGPT and get a response.
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }
    data = {
        'model': 'gpt-3.5-turbo',  # specify the model to use
        'messages': [
            {'role': 'system',
             'content': 'You are an ia that control a robot named Edog. You have been designed to compete in the Eurobot competition. Your code is fully open-source and has been developed using ROS2. You are equiped with a Raspberry Pi 4 and running an unbuntu OS. All your hardware is controlling using a Robot Operating System called ROS2. Your creator is a genius called Gaultier Lecaillon. Your responses will be sharp and short, never anwser with more than 10 words'},
            {'role': 'user', 'content': prompt},
        ]
    }
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers,
        data=json.dumps(data)
    )

    if response.status_code == 200:
        model_response = response.json()['choices'][0]['message']['content']
        return model_response.strip()
    else:
        raise ConnectionError("Request to ChatGPT API failed.")


def aws_polly_speak(text):
    """
    Convert text to speech using AWS Polly and play the generated speech.
    """
    polly_client = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    ).client('polly')

    try:
        response = polly_client.synthesize_speech(VoiceId='Joanna',
                                                  OutputFormat='mp3',
                                                  Text=text)
        soundfile = io.BytesIO(response['AudioStream'].read())
        mixer.init()
        mixer.music.load(soundfile)
        mixer.music.play()

        while mixer.music.get_busy() == True:
            pass
    except Exception as e:
        print(str(e))


def main():
    """
    Main function to run the chat loop.
    """
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting...")
                break
            else:
                gpt_response = get_chatgpt_response(user_input)
                print("ChatGPT: ", gpt_response)
                aws_polly_speak(gpt_response)
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()

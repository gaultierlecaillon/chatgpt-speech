# ChatGPT Audio Responder

A simple Python application that sends a user prompt to OpenAI's ChatGPT, retrieves the model's response, converts it into speech using AWS Polly, and plays the audio response.

## Requirements
- Python 3.6+
- [OpenAI API key](https://beta.openai.com/signup/)
- [AWS credentials](https://aws.amazon.com/)

## Dependencies
- requests
- boto3
- pygame
- python-dotenv

## Setup & Installation
1. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    
2. **Configure API Keys**
    - Create a `.env` file in the project root.
    - Add your API keys:
        ```plaintext
        OPENAI_API_KEY=your_openai_api_key
        AWS_ACCESS_KEY=your_aws_access_key
        AWS_SECRET_KEY=your_aws_secret_key
        AWS_REGION=your_aws_region
        ```

## Usage
1. **Run the Script**
    ```bash
    python main.py
    ```
2. **Interact with the Bot**
    - Enter your message when prompted.
    - Listen to the audio response from ChatGPT.
    - Type `exit` or `quit` to end the session.

## Disclaimer
Ensure that you handle your API keys securely and abide by the usage policies of OpenAI and AWS.

## License
MIT License. See [LICENSE](LICENSE) for more details.

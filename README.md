# VoiceGPT-Assistant

VoiceGPT-Assistant is an AI-powered voice assistant that allows users to interact with their computer through voice commands. It integrates speech recognition, text-to-speech, and web browsing capabilities. Additionally, the assistant can interface with Google's Generative AI for conversational responses and answer various queries intelligently.

## Features
- **Voice Command Recognition**: The assistant listens to your voice commands and performs actions such as opening websites, telling the time, and more.
- **Text-to-Speech**: The assistant speaks out the responses and actions.
- **AI-Powered Responses**: Using Google Generative AI (Gemini), the assistant provides intelligent answers.
- **Web Browsing**: Open common websites like YouTube and Google through voice commands.
- **Voice Assistant Interaction**: The assistant introduces itself as "Baymax" and responds to queries such as "What's your name?" or "What time is it?"

## Requirements

- Python 3.6 or above
- **Libraries**:
  - `pyttsx3` (for text-to-speech)
  - `speech_recognition` (for speech-to-text)
  - `webbrowser` (to open websites)
  - `datetime` (for time-related functionalities)
  - `google.generativeai` (for AI responses)
  - `re` (for regex filtering)
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Anirban96Roy/VoiceGPT-Assistant.git
   cd VoiceGPT-Assistant
2. Install the required Python packages:

   pip install pyttsx3 speechrecognition google-generativeai
3. Set up your Google Generative AI API key:

    Ensure you have an API key from Google Generative AI.
    Store it in an environment variable named API_KEY.
4.To stop the assistant, say "stop".

## Example Interaction:

    Baymax: Hello sir, I am Baymax. How can I help you?
    You: What's the time?
    Baymax: Sir, the time is 14:32.
    You: Open YouTube.
    Baymax: Opening YouTube sir.

## Future Enhancements
    Add more websites for quick access.
    Expand AI capabilities for more intelligent interactions.
    Add error handling and voice command customization.

## Thank you.

Buddybot: AI Chatbot using Mistral API
Overview
Buddybot is an AI chatbot built using the Mistral API. This project leverages the powerful capabilities of the Mistral large language model to provide intelligent and context-aware responses to user queries. The chatbot is built using Streamlit for an interactive and user-friendly interface. Users can input their questions, and Buddybot will respond with relevant answers.

Features
Intelligent Responses: The chatbot uses Mistral's large language model to generate contextually appropriate responses.
Easy-to-Use Interface: Built with Streamlit, Buddybot offers a simple and intuitive interface for users to interact with.
Real-time Interaction: Responses are generated in real-time to user queries, providing an engaging experience.
Technology Stack
Python: The core programming language used for building the chatbot.
Streamlit: Used for creating the web interface.
Mistral API: Utilized for natural language processing and response generation.
Getting Started
Prerequisites
Python 3.7 or higher
A Mistral API key (You can obtain one by signing up on the Mistral website)
Installation
Clone the repository:

sh

git clone https://github.com/yourusername/buddybot.git
cd buddybot
Install the required Python packages:

sh

pip install -r requirements.txt
Set up the Mistral API key in your environment:

sh

export MISTRAL_API_KEY="your_mistral_api_key"
Running the Chatbot
To start the chatbot, run the following command:

sh

streamlit run app.py
Open your web browser and go to http://localhost:8501 to interact with Buddybot.

Usage
Enter your question in the text input field labeled "Enter your question".
Click the "Submit" button to get a response.
The AI-generated response will appear in the text area labeled "Response".

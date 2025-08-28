*****************Conversational AI Health Agent*****************
This project is a sophisticated, web-based Conversational AI Health Agent designed to provide a preliminary analysis of health symptoms. The agent allows users to describe their symptoms in plain, natural language and receive a data-driven prediction with a confidence score.

The system has demonstrated high accuracy in identifying classic symptom clusters for critical conditions like Heart Attack (96.99% confidence) and Diabetes (100% confidence), while also responsibly handling ambiguous inputs. It serves as an intelligent, empathetic first point of contact, always guiding users toward seeking professional medical advice.


***Features***

    >>Natural Language Interface: Users can chat with the agent as they would with a person, describing symptoms freely.

    >>Agentic Workflow: Utilizes LangChain and Google Gemini to orchestrate a multi-step reasoning process, understanding user intent and using a "Smart Tool" to find answers.

    >>Deep Learning Core: The agent's tool is powered by a TensorFlow/Keras model trained to identify 41 diseases from 132 symptoms.

    >>Responsible AI Design: The agent never provides a final diagnosis. It always provides predictions with a confidence score and concludes by advising the user to consult a professional doctor.

    >>Cloud Deployed: The application is fully deployed and publicly accessible via Streamlit Community Cloud.


***Technology Stack***

    >  Frontend & Application Framework: Streamlit

    >  AI Agent Framework: LangChain

    >  Language Model (LLM): Google Gemini Pro (gemini-1.5-flash-latest)

    >  Machine Learning Model: TensorFlow (Keras)

    >  ML Libraries: Scikit-learn, NumPy, Joblib


***Local Setup and Installation***
To run this project on your local machine, follow these steps:

1. Clone the Repository

#git clone https://github.com/keshriaman231/Conversational-AI-Health-Agent.git
#cd Conversational-AI-Health-Agent

2. Install Dependencies

Create a requirements.txt file with the following content and run the installation command.
Plaintext

# requirements.txt
tensorflow-cpu 
scikit-learn
joblib
numpy
streamlit
requests
langchain
langchain-google-genai
google-generativeai

Then, install the packages:

#pip install -r requirements.txt





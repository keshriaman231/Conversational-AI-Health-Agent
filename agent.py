'''
# agent.py (Updated for Google Gemini)

import os
import requests
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import tool, AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate

# --- 1. SET YOUR GOOGLE API KEY ---
# Replace "YOUR_GOOGLE_API_KEY" with the key you got from Google AI Studio.
# For better security, it's recommended to set this as an environment variable.
os.environ["GOOGLE_API_KEY"] = "AIzaSyBAUx9QR3x69ZhHaqNjwKGZyJ1xfHEEpeA"

# --- 2. Define the Tool (NO CHANGE HERE) ---
# This function that calls your Flask API remains exactly the same.
@tool
def disease_prediction_tool(symptoms: list) -> str:
    """
    This tool is used to predict a disease based on a list of 132 binary (0 or 1)
    symptom values. It requires a complete list of 132 symptoms to function.
    """
    print("🤖 Calling the prediction tool with symptoms...")
    api_url = "http://127.0.0.1:5000/predict" # Your running Flask app
    payload = {"symptoms": symptoms}
    
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return f"Prediction successful. Disease: {result['prediction']}, Confidence: {result['confidence']}%."
        else:
            return f"API call failed with status code {response.status_code}. Error: {response.text}"
    except Exception as e:
        return f"An exception occurred while calling the API: {str(e)}"

# --- 3. Load the features list (Corrected Path) ---
# Construct the correct path to features.json inside the backend/model directory
features_path = os.path.join('backend', 'model', 'features.json')
with open(features_path, 'r') as f:
    FEATURES = json.load(f)

# --- 4. Create the Agent with Gemini (THIS IS THE UPDATED PART) ---
tools = [disease_prediction_tool]

# Initialize the Gemini model via LangChain
# We use "gemini-1.5-flash-latest", which is fast, capable, and great for chat agents.
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)

# The prompt template remains exactly the same!
prompt_template = """
You are an empathetic and helpful AI health assistant. Your primary goal is to have a conversation
with a user to determine which of the {num_features} symptoms they are experiencing.

Here is the complete list of symptoms you must ask about:
{symptom_list}

Your process is:
1. Greet the user and ask them about their symptoms in a friendly, conversational way.
2. Do NOT ask for all 132 symptoms at once. Ask them in logical groups or one by one.
3. You MUST determine a '1' (yes) or '0' (no) for EVERY symptom in the list.
4. Once you have collected all 132 symptom values, create a single list of these 0s and 1s.
5. Call the `disease_prediction_tool` with this complete list.
6. After getting the result, explain it to the user in a clear and caring manner.
7. CRITICAL: ALWAYS end your response by advising the user to consult a professional doctor
   for a real diagnosis, as you are only an AI assistant.

Begin the conversation.

User's message: {input}
Agent's thought process and actions: {agent_scratchpad}
"""

agent_prompt = PromptTemplate.from_template(prompt_template).partial(
    num_features=len(FEATURES),
    symptom_list=", ".join(FEATURES)
)

# The rest of the agent setup is the same
agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)'''






'''
# agent.py (Final version with all fixes)

import os
import requests
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import tool, AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate

# --- 1. SET YOUR GOOGLE API KEY ---
# Make sure your API key is set correctly here
os.environ["GOOGLE_API_KEY"] = "AIzaSyBAUx9QR3x69ZhHaqNjwKGZyJ1xfHEEpeA"

# --- 2. Define the Tool ---
@tool
def disease_prediction_tool(symptoms: list) -> str:
    """
    This tool is used to predict a disease based on a list of 132 binary (0 or 1)
    symptom values. It requires a complete list of 132 symptoms to function.
    """
    print("🤖 Calling the prediction tool with symptoms...")
    api_url = "http://127.0.0.1:5000/predict"
    payload = {"symptoms": symptoms}
    
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return f"Prediction successful. Disease: {result['prediction']}, Confidence: {result['confidence']}%."
        else:
            return f"API call failed with status code {response.status_code}. Error: {response.text}"
    except Exception as e:
        return f"An exception occurred while calling the API: {str(e)}"

# --- 3. Load the features list ---
features_path = os.path.join('backend', 'model', 'features.json')
with open(features_path, 'r') as f:
    FEATURES = json.load(f)

# --- 4. Create the Agent with Gemini ---
tools = [disease_prediction_tool]
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)

# THIS IS THE CORRECTED PROMPT TEMPLATE
prompt_template = """
You are an empathetic and helpful AI health assistant. Your primary goal is to have a conversation
with a user to determine which of the {num_features} symptoms they are experiencing.

Here is the complete list of symptoms you must ask about:
{symptom_list}

You have access to the following tool to get a prediction:
{tools}

To use the tool, you must use the following format:
Thought: Do I need to use a tool? Yes, I have collected all the symptom data.
Action: the action to take, should be one of [{tool_names}]
Action Input: A Python list of all 132 symptom values (0s or 1s).
Observation: the result of the tool.

Your process is:
1. Greet the user and ask them about their symptoms in a friendly, conversational way.
2. Do NOT ask for all 132 symptoms at once. Ask them in logical groups or one by one.
3. You MUST determine a '1' (yes) or '0' (no) for EVERY symptom in the list.
4. Once you have collected all 132 symptom values, you MUST use the 'disease_prediction_tool'.
5. After getting the result from the tool, provide a final answer to the user.
6. CRITICAL: ALWAYS end your final answer by advising the user to consult a professional doctor
   for a real diagnosis, as you are only an AI assistant.

Begin the conversation now.

User's message: {input}
Thought:{agent_scratchpad}
"""

agent_prompt = PromptTemplate.from_template(prompt_template).partial(
    num_features=len(FEATURES),
    symptom_list=", ".join(FEATURES)
)

agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)'''



'''
# ******agent.py (Final version with all fixes) - run succesfully *********

import os
import requests
import json
import re
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import tool, AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate

# --- 1. SET YOUR GOOGLE API KEY ---
# Make sure your API key is set correctly here
os.environ["GOOGLE_API_KEY"] = "AIzaSyBAUx9QR3x69ZhHaqNjwKGZyJ1xfHEEpeA"

# --- 2. Load the features list ---
features_path = os.path.join('backend', 'model', 'features.json')
with open(features_path, 'r') as f:
    FEATURES = json.load(f)

# --- 3. Initialize the LLM ---
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)

# --- 4. Define the NEW, SMARTER Tool ---
@tool
def disease_prediction_tool(natural_language_symptoms: str) -> str:
    """
    This is the primary tool. Use it when a user describes their health symptoms in natural language.
    This tool will convert the sentence into a full symptom list and get a prediction.
    The input should be the user's description of their symptoms as a single string.
    """
    print(f"🤖 Tool received natural language input: '{natural_language_symptoms}'")
    
    # --- Internal Step A: Use the LLM to convert the sentence to a list ---
    symptom_converter_prompt = PromptTemplate.from_template(
        """
        You are a highly specialized function. Your ONLY job is to convert a user's symptom description into a binary list.
        Given the user's symptoms: "{user_symptoms}"
        And the complete list of 132 possible features: {all_features}

        Analyze the user's symptoms. For each feature in the complete list, output a 1 if the user's description mentions it (or a synonym), and a 0 otherwise.
        The final output MUST be ONLY the Python list itself (e.g., [0, 1, 0, ..., 1, 0]) and absolutely nothing else.
        """
    )
    
    symptom_chain = symptom_converter_prompt | llm
    
    print("🧠 Converting sentence to symptom list...")
    list_string = symptom_chain.invoke({
        "user_symptoms": natural_language_symptoms,
        "all_features": ", ".join(FEATURES)
    }).content

    print(f"⚙️ LLM returned list string: {list_string}")

    # --- Internal Step B: Clean up and validate the list ---
    try:
        match = re.search(r'\[(.*?)\]', list_string)
        if not match:
            return "Error: The AI failed to generate a valid symptom list. Please try rephrasing your symptoms."
            
        symptoms_list = json.loads(f"[{match.group(1)}]")

        if len(symptoms_list) != 132:
            return f"Error: The AI generated a list with {len(symptoms_list)} items instead of 132. Please try again."

    except (json.JSONDecodeError, ValueError) as e:
        return f"Error: Could not parse the symptom list generated by the AI. Details: {e}"

    # --- Internal Step C: Call your backend API with the generated list ---
    print(f"📞 Calling the backend API with the list...")
    api_url = "http://127.0.0.1:5000/predict"
    payload = {"symptoms": symptoms_list}
    
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return f"Prediction successful. Predicted Disease: {result['prediction']}, Confidence: {result['confidence']}%."
        else:
            return f"API call failed with status code {response.status_code}. Error: {response.text}"
    except Exception as e:
        return f"An exception occurred while calling the API: {str(e)}"

# --- 5. Create the Final Agent (WITH THE CORRECTED PROMPT) ---
tools = [disease_prediction_tool]

# THIS IS THE CORRECTED PROMPT. It now includes {tool_names}.
agent_prompt = PromptTemplate.from_template(
    """
    You are a helpful AI health assistant. Your job is to understand the user's symptoms and use a tool to analyze them.

    You have access to the following tools:
    {tools}

    To use a tool, you must use the following format:

    Thought: Do I need to use a tool? Yes. The user has described their symptoms.
    Action: The action to take, which should be one of [{tool_names}]
    Action Input: The user's original, natural language description of their symptoms.
    Observation: The result of the action.

    After using the tool and getting an observation, you will have the final answer.
    CRITICAL: ALWAYS end your final answer by advising the user to consult a professional doctor for a real diagnosis.

    Begin!

    User's message: {input}
    Thought:{agent_scratchpad}
    """
)

agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)'''





#result optimization

# agent.py (Definitive Final Version)

import os
import requests
import json
import re
import ast # Import the 'ast' library
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import tool, AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate

# --- 1. SET YOUR GOOGLE API KEY ---
# Make sure your API key is set correctly here
os.environ["GOOGLE_API_KEY"] = "AIzaSyBNyAdwvlPq2D8fvHGA-r3n3a8qGBEB4iM"

# --- 2. Load the features list ---
features_path = os.path.join('backend', 'model', 'features.json')
with open(features_path, 'r') as f:
    FEATURES = json.load(f)

# --- 3. Initialize the LLM ---
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)

# --- 4. Define the FINAL, MOST ROBUST Tool ---
@tool
def disease_prediction_tool(natural_language_symptoms: str) -> str:
    """
    This is the primary tool. Use it when a user describes their health symptoms in natural language.
    This tool will convert the sentence into a full symptom list and get a prediction.
    The input should be the user's description of their symptoms as a single string.
    """
    print(f"🤖 Tool received natural language input: '{natural_language_symptoms}'")
    
    symptom_extractor_prompt = PromptTemplate.from_template(
        """
        You are a highly specialized function. Your ONLY job is to identify which symptoms a user has based on their description.
        Given the user's symptoms: "{user_symptoms}"
        And the complete list of 132 possible features: {all_features}

        Return a Python list of strings containing ONLY the names of the features the user mentioned.
        For example: ["headache", "cough", "high_fever"]
        The final output MUST be ONLY the Python list of strings and absolutely nothing else.
        """
    )
    
    symptom_chain = symptom_extractor_prompt | llm
    
    print("🧠 Extracting symptom names from the sentence...")
    list_of_names_str = symptom_chain.invoke({
        "user_symptoms": natural_language_symptoms,
        "all_features": ", ".join(FEATURES)
    }).content

    print(f"⚙️ LLM returned symptom names: {list_of_names_str}")

    # --- THIS IS THE CORRECTED PARSING LOGIC ---
    try:
        # Use a more robust method to find the list in the string
        cleaned_str_match = re.search(r'\[.*\]', list_of_names_str, re.DOTALL)
        if not cleaned_str_match:
             return "Error: The AI failed to generate a recognizable symptom list format."
        cleaned_str = cleaned_str_match.group(0)

        # Use ast.literal_eval instead of json.loads to handle single quotes
        symptoms_present = ast.literal_eval(cleaned_str)

        symptoms_list = [0] * 132
        for i, feature in enumerate(FEATURES):
            if feature in symptoms_present:
                symptoms_list[i] = 1
        
        print(f"✅ Successfully built binary list. Found {sum(symptoms_list)} symptoms.")

    except Exception as e:
        return f"Error: Could not parse the symptom names generated by the AI. Details: {e}"

    # --- Internal Step C: Call your backend API with the generated list ---
    print(f"📞 Calling the backend API...")
    api_url = "http://127.0.0.1:5000/predict"
    payload = {"symptoms": symptoms_list}
    
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return f"Prediction successful. Predicted Disease: {result['prediction']}, Confidence: {result['confidence']}%."
        else:
            return f"API call failed with status code {response.status_code}. Error: {response.text}"
    except Exception as e:
        return f"An exception occurred while calling the API: {str(e)}"

# --- 5. Create the Final Agent ---
tools = [disease_prediction_tool]

agent_prompt = PromptTemplate.from_template(
    """
    You are a helpful AI health assistant. Your job is to understand the user's symptoms and use a tool to analyze them.

    You have access to the following tools:
    {tools}

    To use a tool, you must use the following format:

    Thought: Do I need to use a tool? Yes. The user has described their symptoms.
    Action: The action to take, which should be one of [{tool_names}]
    Action Input: The user's original, natural language description of their symptoms.
    Observation: The result of the action.

    After using the tool and getting an observation, you will have the final answer.
    CRITICAL: ALWAYS end your final answer by advising the user to consult a professional doctor for a real diagnosis.

    Begin!

    User's message: {input}
    Thought:{agent_scratchpad}
    """
)

agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
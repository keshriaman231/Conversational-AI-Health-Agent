🩺 Conversational AI Health Agent 🤖💬

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![AI Agent](https://img.shields.io/badge/Agent-LangChain-purple.svg)](https://www.langchain.com/)
[![LLM](https://img.shields.io/badge/LLM-Google%20Gemini-blue.svg)](https://deepmind.google/technologies/gemini/)
[![ML Library](https://img.shields.io/badge/ML-TensorFlow-orange.svg)](https://www.tensorflow.org/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit%20App-brightgreen)](https://pathosense.streamlit.app/)

---

## 🌟 Overview

The **Conversational AI Health Agent** is a web-based intelligent system that lets users **chat naturally about their symptoms** 🗣️ and receive **AI-driven predictions** ⚡ with confidence scores.

✨ It combines the **power of LLMs (Google Gemini Pro)**, **LangChain orchestration**, and a **deep learning disease prediction model** to act as an empathetic, first-point health assistant.

✔️ Identifies **41 diseases** from **132 symptoms**
✔️ Provides **confidence scores** for predictions
✔️ Always concludes with **responsible medical guidance** 🙏

---

## 🔑 Key Features

💬 **Natural Language Interface** – Describe symptoms in plain English.
🧩 **Agentic Workflow** – Powered by **LangChain** + **Google Gemini**, enabling stepwise reasoning.
🧠 **Deep Learning Core** – A TensorFlow/Keras MLP trained on 132 symptoms → 41 diseases.
🛡️ **Responsible AI Design** – Never a final diagnosis; always encourages professional consultation.
☁️ **Cloud Deployed** – Accessible via **Streamlit Community Cloud** 🌍.

---

## 🛠️ Technology Stack

* 🎨 **Frontend & App Framework**: Streamlit
* 🧩 **AI Agent Framework**: LangChain
* 🧠 **Language Model (LLM)**: Google Gemini Pro *(gemini-1.5-flash-latest)*
* 📊 **Machine Learning Model**: TensorFlow (Keras)
* 📚 **ML Libraries**: Scikit-learn, NumPy, Joblib

---

🏗️ System Architecture

## Flow Diagram 

![Conversational AI Health Agent Architecture](./conversational_ai_health_agent_architecture.png)


📌 Workflow Explanation

🧑 User – Describes symptoms in natural language.

💻 Frontend (Streamlit) – Provides chat interface for user interaction.

🧩 LangChain Agent + Google Gemini Pro – Interprets intent, orchestrates reasoning.

🤖 Disease Prediction Model (TensorFlow/Keras) – Processes symptoms → predicts disease & confidence.

📊 Output – User sees prediction + guidance to consult a doctor.

---

## ⚙️ Local Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/keshriaman231/Conversational-AI-Health-Agent.git
cd Conversational-AI-Health-Agent
```

### 2️⃣ Install Dependencies

Create a `requirements.txt` with the following:

```txt
tensorflow-cpu 
scikit-learn
joblib
numpy
streamlit
requests
langchain
langchain-google-genai
google-generativeai
```

Install with:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Backend & Frontend

```bash
# In backend directory
cd backend
python app.py
```

```bash
# In main directory
streamlit run streamlit_chat_app.py
```

🚀 The application will now be running on your **localhost**.

---

## 🧪 Example Prompts & Responses

📝 **Prompt 1:**

> I have been feeling irregular sugar levels, blurred and distorted vision, constipation, weight loss and fatigue.

✅ **AI Response:**
*The disease prediction tool suggests **Diabetes (100% confidence)**.
⚠️ Please consult a professional doctor for a proper diagnosis.*

---

📝 **Prompt 2:**

> I have been feeling chest pain, palpitations, dizziness, sweating and shortness of breath.

✅ **AI Response:**
*The tool suggests a **high probability (98.73%) of a Heart Attack**.
🚨 Seek **immediate medical attention** – call emergency services or visit the ER.*

---

## 🔮 Future Enhancements

* 🤝 Integration with **Electronic Health Records (EHRs)**
* 📱 Mobile-friendly UI for patients & doctors
* 🌐 Multilingual support for wider accessibility
* ☁️ Cloud scaling for enterprise-grade deployments

---

## 🙌 Contribution

Contributions are welcome! 💡
Fork the repo, open issues, or submit PRs to enhance this health agent.

---

⚡ *Disclaimer: This tool provides preliminary predictions and is **not a substitute for professional medical advice**. Always consult a qualified doctor for diagnosis and treatment.*

---

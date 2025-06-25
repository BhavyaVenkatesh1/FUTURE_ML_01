# 🤖 Task 3: SkyAssist AI Chatbot

## 📘 Project Overview
**SkyAssist AI Chatbot** is a virtual assistant designed to help airline passengers get quick, 24/7 answers to common questions — such as baggage, transit, food, check-ins, and more.  
Built with **Streamlit** and **NLP**, it simulates real-time customer support with a smooth, professional UI.

---

## ✨ Features
- Ask questions directly or choose from popular samples
- Responses are generated based on a cleaned FAQ dataset
- Fully responsive, styled Streamlit web interface
- Customizable and domain-specific (currently: airline)

---

## 🛠️ Tech Stack
- **Python 3**
- **Streamlit** – UI interface
- **Pandas**, **scikit-learn**, or **sentence-transformers** – for NLP
- **CSV Dataset** – `chat_data_clean.csv`
- Modular Python backend (`chatbot_utils.py`)

---

## 📁 Folder Structure

Task3_AI_Chatbot/
├── chatbot_model/ # Trained models and NLP pipeline
├── data/ # Intent data or training corpus
│ └── intents.json
├── src/
│ ├── train_chatbot.py # Training script
│ ├── chatbot_core.py # Chatbot engine
│ └── app.py # Flask/Streamlit GUI
├── README.md
├── requirements.txt
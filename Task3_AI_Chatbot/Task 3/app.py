import streamlit as st
from chatbot_utils import load_faq_data, get_answer

st.set_page_config(page_title="SkyAssist AI Chat", layout="centered")

# Load data
faq_data = load_faq_data("chat_data_clean.csv")

# Debug: Show if data loaded correctly
if faq_data is None or faq_data.empty:
    st.error("❌ FAQ data not loaded. Please check 'chat_data_clean.csv'.")
    st.stop()

# Optional: Preview data while testing
# st.write(faq_data.head())

# CSS styling
st.markdown("""
    <style>
        .main {
            padding-top: 10px !important;
        }
        .stTextInput>div>div>input {
            padding: 0.75rem;
            font-size: 16px;
        }
        .response-bubble {
            background-color: #1e293b;
            color: #f8fafc;
            padding: 1rem;
            border-radius: 12px;
            margin-top: 1rem;
            font-size: 16px;
        }
        .sky-title {
            text-align: center;
            margin-bottom: 0.2rem;
        }
        .sky-subtitle {
            text-align: center;
            margin-bottom: 1rem;
            font-size: 14px;
            color: #444;
        }
        .stSelectbox > div[data-baseweb="select"] {
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<h1 class="sky-title">SkyAssist AI Chat</h1>', unsafe_allow_html=True)
st.markdown('<div class="sky-subtitle">Your airline support assistant — fast, friendly & 24/7</div>', unsafe_allow_html=True)

# Sample FAQ questions
sample_questions = [
    "What are the meal options available?",
    "Can I change my seat after booking?",
    "Do I need to reclaim luggage at stopovers?",
    "Can I use the transit hotel?",
    "Why is my name merged on the ticket?"
]

# Ask Section
st.markdown("**✈️ Ask something:**")
selected = st.selectbox("Choose a sample question or ask your own:", [""] + sample_questions, key="sample_question")
user_input = st.text_input("Your question:", value=selected if selected else "", key="user_input")

# Button + Answer
if st.button("Ask"):
    if user_input:
        response = get_answer(faq_data, user_input)

        # Optional debug print inside app
        st.markdown(f'<div class="response-bubble">🤖 {response}</div>', unsafe_allow_html=True)

    else:
        st.warning("Please enter a question.")

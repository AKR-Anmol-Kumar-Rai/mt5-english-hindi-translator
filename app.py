
import streamlit as st
from model_loader import load_model
from utils import translate_text

# page config
st.set_page_config(
    page_title="English to Hindi Translator",
    page_icon="🌍",
    layout="centered"
)

# custom styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0F172A, #1E293B, #312E81);
        color: white;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: white;
        letter-spacing: 1px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #CBD5E1;
        margin-bottom: 30px;
    }

    .stTextArea textarea {
        background-color: rgba(255,255,255,0.08) !important;
        color: white !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        border-radius: 15px !important;
        font-size: 18px !important;
        backdrop-filter: blur(10px);
    }

    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #3B82F6, #8B5CF6);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
    }

    div.stButton > button:hover {
        transform: scale(1.02);
        transition: 0.2s;
    }

    .translation-box {
        background: rgba(255,255,255,0.08);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.15);
        color: white;
        font-size: 20px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: #94A3B8;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# load model
@st.cache_resource
def get_model():
    return load_model()

model, tokenizer, device = get_model()

# title
st.markdown('<p class="title">🌍 English → Hindi Translator</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Powered by mT5 Transformer Model 🚀</p>',
    unsafe_allow_html=True
)

# input
user_input = st.text_area(
    "Enter English text",
    placeholder="Type your sentence here..."
)

# translate button
col1, col2, col3 = st.columns([1,2,1])

with col2:
    translate_btn = st.button("Translate ⚡", use_container_width=True)

# output
if translate_btn:
    if user_input.strip():
        with st.spinner("Translating..."):
            output = translate_text(
                user_input,
                model,
                tokenizer,
                device
            )

        st.success("Translation completed!")

        st.markdown("### Hindi Translation 🇮🇳")
        st.code(output, language=None)

    else:
        st.warning("Please enter some text.")

# footer
st.markdown(
    '<p class="footer">Built with ❤️ using Hugging Face Transformers & Streamlit</p>',
    unsafe_allow_html=True
)
import streamlit as st
from model_loader import load_model
from utils import translate_text

# page config
st.set_page_config(
    page_title="English to Hindi Translator",
    page_icon="🌍",
    layout="centered"
)

# custom styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0F172A, #1E293B, #312E81);
        color: white;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: white;
        letter-spacing: 1px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #CBD5E1;
        margin-bottom: 30px;
    }

    .stTextArea textarea {
        background-color: rgba(255,255,255,0.08) !important;
        color: white !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        border-radius: 15px !important;
        font-size: 18px !important;
        backdrop-filter: blur(10px);
    }

    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #3B82F6, #8B5CF6);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
    }

    div.stButton > button:hover {
        transform: scale(1.02);
        transition: 0.2s;
    }

    .translation-box {
        background: rgba(255,255,255,0.08);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.15);
        color: white;
        font-size: 20px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: #94A3B8;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# load model
@st.cache_resource
def get_model():
    return load_model()

model, tokenizer, device = get_model()

# title
st.markdown('<p class="title">🌍 English → Hindi Translator</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Powered by mT5 Transformer Model 🚀</p>',
    unsafe_allow_html=True
)

# input
user_input = st.text_area(
    "Enter English text",
    placeholder="Type your sentence here..."
)

# translate button
col1, col2, col3 = st.columns([1,2,1])

with col2:
    translate_btn = st.button("Translate ⚡", use_container_width=True)

# output
if translate_btn:
    if user_input.strip():
        with st.spinner("Translating..."):
            output = translate_text(
                user_input,
                model,
                tokenizer,
                device
            )

        st.success("Translation completed!")

        st.markdown("### Hindi Translation 🇮🇳")
        st.code(output, language=None)

    else:
        st.warning("Please enter some text.")

# footer
st.markdown(
    '<p class="footer">Built with ❤️ using Hugging Face Transformers & Streamlit</p>',
    unsafe_allow_html=True
)
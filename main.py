import json
import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="English Quotes Gallery", layout="wide")

def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&w=1740&q=80");
            background-size: cover;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
set_background()

st.markdown("<h1 style='text-align: center; color: grey; margin-bottom: 40px;'>✨ Inspiring English Quotes ✨</h1>", unsafe_allow_html=True)

with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)

if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0

def change_quote():
    st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes)

quote = quotes[st.session_state.quote_index]

st.markdown(
    f"""
    <div style='
        font-size: 24px; 
        font-style: italic; 
        text-align: center; 
        max-width: 800px; 
        margin: auto; 
        background-color: rgba(255,255,255,0.8);
        padding: 25px 40px;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
        line-height: 1.5;
    '>
        “{quote['text']}”<br>
        <span style='font-weight: 600; font-style: normal; color: #555;'>— {quote['author']}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <p style='
        text-align: center;
        color: #888;
        font-size: 14px;
        margin-top: 12px;
        font-family: "Microsoft YaHei", sans-serif;
    '>{quote['translation']}</p>
    """,
    unsafe_allow_html=True,
)

# 放在页面底部右下角的按钮
st.markdown(
    """
    <style>
    /* 定位按钮固定在右下角 */
    div.stButton > button:first-child {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: grey !important;
        border: 2px solid grey !important;
        border-radius: 25px !important;
        padding: 12px 28px !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        box-shadow: 0 0 10px rgba(128,128,128,0.2) !important;
        user-select: none !important;
        backdrop-filter: blur(6px) !important;
        transition: background-color 0.3s ease, color 0.3s ease !important;
        z-index: 9999 !important;
    }
    div.stButton > button:first-child:hover {
        background-color: rgba(255, 255, 255, 0.25) !important;
        color: #444 !important;
        border-color: #444 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.button("Next Quote"):
    change_quote()

rain(emoji="✨", font_size=20, falling_speed=5, animation_length="infinite")

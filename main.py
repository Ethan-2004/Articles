import json
import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="English Quotes Gallery", layout="wide")

# 设置背景
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&w=1740&q=80");
            background-size: cover;
            background-attachment: fixed;
            color: #333;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
set_background()

# 载入句子数据
def load_quotes():
    try:
        with open("quotes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_quotes(quotes):
    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=2)

quotes = load_quotes()

# 主页：展示句子
st.markdown("<h1 style='text-align: center; color: #555; margin-bottom: 40px;'>✨ Inspiring English Quotes ✨</h1>", unsafe_allow_html=True)

if not quotes:
    st.info("还没有添加任何句子，快去添加你的第一条句子吧！")
else:
    if "quote_index" not in st.session_state:
        st.session_state.quote_index = 0

    def change_quote():
        st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes)

    quote = quotes[st.session_state.quote_index]

    st.markdown(
        f"""
        <div style='
            font-size: 26px; 
            font-style: italic; 
            text-align: center; 
            max-width: 800px; 
            margin: auto; 
            background-color: rgba(255,255,255,0.85);
            padding: 30px 50px;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            line-height: 1.6;
            font-family: "Georgia", serif;
        '>
            “{quote['text']}”<br>
            <span style='font-weight: 700; font-style: normal; color: #666;'>— {quote['author']}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if 'translation' in quote and quote['translation']:
        st.markdown(
            f"""
            <p style='
                text-align: center;
                color: #777;
                font-size: 16px;
                margin-top: 18px;
                font-family: "Microsoft YaHei", sans-serif;
                text-shadow: 0 0 6px #bbb, 0 0 12px #ddd;
            '>{quote['translation']}</p>
            """,
            unsafe_allow_html=True,
        )


    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: rgba(128, 128, 128, 0.3) !important; /* 浅灰色背景 */
            color: grey !important; /* 深灰文字 */
            border: 2px solid #888888 !important; /* 中灰边框 */
            border-radius: 30px !important;
            padding: 14px 36px !important;
            font-size: 20px !important;
            font-weight: 700 !important;
            cursor: pointer !important;
            box-shadow: none !important; /* 默认无阴影 */
            user-select: none !important;
            backdrop-filter: blur(8px) !important;
            transition: background-color 0.3s ease, color 0.3s ease, box-shadow 0.3s ease !important;
            z-index: 9999 !important;
        }
        div.stButton > button:first-child:hover {
            background-color: rgba(255, 255, 255, 0.9) !important; /* 悬停白色背景 */
            color: grey !important; /* 白色文字 */
            border-color: #ffffff !important; /* 白色边框 */
            box-shadow: 0 0 15px 5px rgba(255, 255, 255, 0.8) !important; /* 白色发光 */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    if st.button("Next Quote"):
        change_quote()

    rain(emoji="✨", font_size=22, falling_speed=5, animation_length="infinite")


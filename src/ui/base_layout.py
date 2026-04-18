import streamlit as st 


def style_background_home():
    st.markdown("""
    <style>
        .stApp {
            background: #5865f2 !important;
        }

        div[data-testid="column"] {
            background-color: #E0E3FF !important;
            padding: 2.5rem 2rem !important;
            border-radius: 2.5rem !important;
            text-align: center;
        }
    
        div[data-testid="stImage"] {
            padding: 0 !important;
            margin: 0 auto !important;
        }

        div[data-testid="stImage"] > div {
            width: 100% !important;
            display: flex !important;
            justify-content: center !important;
        }
        div[data-testid="stImage"] img {
            display: block !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }

        div.stButton {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }

    </style>
    """, unsafe_allow_html=True)
def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@100..900&display=swap');

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }
            h2{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif;
            }

            button {
                border-radius: 1.5rem !important;
                background: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                background: #EB459E !important;
            }

            button[kind="tertiary"] {
                background: black !important;
            }

            button:hover {
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)
import streamlit as st
import logging


PAGE_TITLE = "Page 2"
PAGE_ICON = "💹"

logger = logging.getLogger('mylogger')

def configure_page():
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="wide", 
        initial_sidebar_state="expanded"
    )

    st.markdown("# 🎈 Stock forecast dashboard 📈")
    st.sidebar.markdown("# Main page 🎈")
    st.title('')

def app():
    configure_page()
    logger.error('page 2')

app()

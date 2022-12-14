import streamlit as st
import logging

from middleware.services.logging import logger_config

PAGE_TITLE = "Stock App!"
PAGE_ICON = "📈"

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


if __name__ == "__main__":
    logger_config.setup_logger()

app()

logger.debug('This is a debug-level message')
logger.info('This is an info-level message')
logger.warning('This is a warning-level message')
logger.error('This is an error-level message')
logger.critical('This is a critical-level message')


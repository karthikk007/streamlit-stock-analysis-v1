import datetime
import logging
import time

import streamlit as st

from dateutil.relativedelta import relativedelta

from middleware.stock_engine import StockEngine
from middleware.services.logging import logger_config

PAGE_TITLE = "Stock App!"
PAGE_ICON = "📈"

logger = logging.getLogger('mylogger')
engine = StockEngine.instance()

change_container = None

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

    st.sidebar.success("Select ticker to display chart.")

    show_ticker_selector()
    show_date_picker()

    show_change_container()

    show_progress_bar()

    # app_state = engine.app_state_data_source

    # app_state.update(PAGE_TITLE, {'kk': '2525'})
    # app_state.update('kk', {'kk': '2525'})

    # app_state.clear(PAGE_TITLE)
    # app_state.clear_all()


def show_ticker_selector():
    selected = get_app_state('_select_ticker')
    tickers = get_tickers()

    select_index = 0
    if selected:
        select_index = tickers.index(selected)
    
    demo_name = st.sidebar.selectbox("Choose ticker:", tickers, key='_select_ticker', index=select_index, on_change=did_change_ticker)


def show_progress_bar():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    for i in range(1, 101):
        progress_bar.progress(i)
        status_text.text("%i%% Complete" % i)
        time.sleep(0.001)

    # progress_bar.empty()


def show_change_container():
    change_container = st.sidebar.container()
    with change_container:
        st.write('change %')

def did_change_ticker():
    selected = st.session_state['_select_ticker']
    logger.info('Selected ticker = {}'.format(selected))

    dict = { '_select_ticker': selected}
    update_app_state(dict)

def did_change_date_range():
    val = st.session_state['range_picker']
    logger.info('Selected range = {}'.format(val))

def did_change_date_picker():
    print("did_change_date_picker")

def show_date_picker():
    with st.sidebar.container():
        st.markdown("## Insights") # add a title to the sidebar container
        con1 = st.sidebar.container()
        show_date_range(con1)

        con2 = st.sidebar.container()

        col1, col2 = con2.columns(2)

        end_date = datetime.datetime.today()
        start_date = end_date - relativedelta(years=1)
        min_date = end_date - relativedelta(years=20)

        col1.date_input('From', start_date, min_date, end_date, key='from_date_picker', on_change=did_change_date_picker)
        col2.date_input('To', end_date, min_date, end_date, key='to_date_picker', on_change=did_change_date_picker)


def show_date_range(container):
    periods = [
        "1d", 
        "5d",
        "1mo",
        "3mo",
        "6mo",
        "1y",
        "2y",
        "5y",
        "10y",
        "ytd",
        "max",
    ]
    container.selectbox('Range', ('-', '3 Months', '6 Months', '1 Year', '2 Years', '3 Years', '4 Years', '5 Years', '10 Years', 'Max'), index=3, key='range_picker', on_change=did_change_date_range)


def get_app_state(key):
    app_state = engine.app_state_data_source

    dict = app_state.get(PAGE_TITLE)
    return dict.get(key)


def update_app_state(state_dict):
    app_state = engine.app_state_data_source

    app_state.update(PAGE_TITLE, state_dict)


def get_tickers():
    # List of tickers
    TICKERS = ['TCS', 'ITC', 'RELIANCE', 'COALINDIA', 'VINATIORGA', 'PAGEIND', 'DEEPAKNTR', 'ZOMATO', 'AMARAJABAT']

    TICKERS = sorted(TICKERS)
    return TICKERS


if __name__ == "__main__":
    logger_config.setup_logger()

app()

# logger.debug('This is a debug-level message')
# logger.info('This is an info-level message')
# logger.warning('This is a warning-level message')
# logger.error('This is an error-level message')
# logger.critical('This is a critical-level message')


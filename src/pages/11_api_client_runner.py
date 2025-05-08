# api_client_runner.py
# import yaml

import streamlit as st

APP_TITLE = "API Client Runner"


def init_st_session_state():
    pass


def sidebar():
    pass


def main():
    st.page_link("main.py", label="Back to Home", icon="🏠")
    st.title(f"🏃 {APP_TITLE}")


if __name__ == "__main__":
    init_st_session_state()

    sidebar()
    main()

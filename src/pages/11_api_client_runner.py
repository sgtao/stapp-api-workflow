# api_client_runner.py
import requests

# import yaml

import streamlit as st

from components.SideMenus import SideMenus
from functions.AppLogger import AppLogger

APP_TITLE = "API Client Runner"


def init_st_session_state():
    if "api_configs" not in st.session_state:
        st.session_state.api_configs = []


def sidebar():
    side_menus = SideMenus()
    side_menus.render_api_client_menu()


def main():
    st.page_link("main.py", label="Back to Home", icon="🏠")
    st.title(f"🏃 {APP_TITLE}")

    endpoint_hostname = st.text_input(
        label="API Endpoint Hostname", value="localhost:3000"
    )
    endpoint_path = "api/v0/configs"
    if st.button("Get API configs"):
        endpoint = f"http://{endpoint_hostname}/{endpoint_path}"
        st.session_state.api_configs = requests.get(endpoint).json()
        st.json(
            st.session_state.api_configs,
            expanded=True,
        )

    if "result" not in st.session_state.api_configs:
        st.info("Please click the button to get API configs. ")
    else:
        # if "result" in st.session_state.api_configs:
        api_config_list = st.session_state.api_configs["result"]
        config = st.selectbox(
            label="Select a config",
            options=api_config_list,
        )

        st.write("##### Config states")
        with st.expander(
            label="##### Config states",
            expanded=False,
            icon="📝",
        ):
            st.write(config)

        if st.button("Request POST with config"):
            endpoint_path = "api/v0/service"
            endpoint = f"http://{endpoint_hostname}/{endpoint_path}"
            request_body = {
                "config_file": "assets/001_get_simple_api_test.yaml",
                # "num_user_inputs": st.session_state.num_inputs,
                "num_user_inputs": 0,
                "user_inputs": {},
            }

            response = requests.post(
                endpoint,
                json=request_body,
            )
            st.json(
                response.json(),
                expanded=True,
            )


if __name__ == "__main__":
    app_logger = AppLogger(APP_TITLE)
    app_logger.app_start()

    init_st_session_state()

    sidebar()
    main()

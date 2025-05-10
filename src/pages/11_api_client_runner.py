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
    app_logger = AppLogger(APP_TITLE)
    app_logger.app_start()

    st.page_link("main.py", label="Back to Home", icon="🏠")
    st.title(f"🏃 {APP_TITLE}")

    endpoint_hostname = st.text_input(
        label="API Endpoint Hostname", value="localhost:3000"
    )
    endpoint_path = "api/v0/configs"
    if st.button("Get API configs"):
        endpoint = f"http://{endpoint_hostname}/{endpoint_path}"
        st.session_state.api_configs = requests.get(endpoint).json()
        with st.expander(
            label="##### Response oconfig",
            expanded=False,
            icon="📝",
        ):
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
                "config_file": config,
                "num_user_inputs": st.session_state.num_inputs,
                "user_inputs": {},
            }
            for i in range(st.session_state.num_inputs):
                user_key = f"user_input_{i}"
                if user_key in st.session_state:
                    value = st.session_state[user_key]
                    # ここで特別なエスケープやreplaceは不要
                    request_body["user_inputs"][user_key] = value
                else:
                    st.warning(f"Session state key '{user_key}' not found.")

            try:
                app_logger.api_start_log(
                    url=endpoint,
                    method="POST",
                    body=request_body,
                )
                response = requests.post(
                    endpoint,
                    json=request_body,
                )

                st.json(
                    response.json(),
                    expanded=True,
                )
                app_logger.api_success_log(response)

            except Exception as e:
                app_logger.error_log(f"Error: {e}")
                st.error(f"Error: {e}")


if __name__ == "__main__":
    init_st_session_state()

    sidebar()
    main()

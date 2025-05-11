# api_client_runner.py
import requests

# import yaml

import streamlit as st

from components.ActionsViewer import ActionsViewer
from components.ResponseViewer import ResponseViewer
from components.SideMenus import SideMenus
from functions.AppLogger import AppLogger

APP_TITLE = "API Client Runner"


def init_st_session_state():
    if "api_configs" not in st.session_state:
        st.session_state.api_configs = []
    if "selected_config" not in st.session_state:
        st.session_state.selected_config = ""
    if "response" not in st.session_state:
        st.session_state.response = {}


def sidebar():
    side_menus = SideMenus()
    side_menus.render_api_client_menu()


def main():
    app_logger = AppLogger(APP_TITLE)
    app_logger.app_start()

    st.page_link("main.py", label="Back to Home", icon="🏠")
    st.title(f"🏃 {APP_TITLE}")

    response_viewer = ResponseViewer()
    actions_viewer = ActionsViewer()

    endpoint_hostname = st.text_input(
        label="API Endpoint Hostname", value="localhost:3000"
    )
    endpoint_path = "api/v0/configs"
    if st.button("Get API configs"):
        endpoint = f"http://{endpoint_hostname}/{endpoint_path}"
        st.session_state.api_configs = requests.get(endpoint).json()
        with st.expander(
            label="##### Response config",
            expanded=False,
            icon="📝",
        ):
            st.json(
                st.session_state.api_configs,
                expanded=True,
            )

    if "result" not in st.session_state.api_configs:
        st.warning("Please click the button to get API configs. ")
    else:
        # if "result" in st.session_state.api_configs:
        api_config_list = st.session_state.api_configs["result"]
        st.session_state.selected_config = st.selectbox(
            label="Select a config",
            options=api_config_list,
        )

        if st.button("Request POST with config", type="primary"):
            endpoint_path = "api/v0/service"
            endpoint = f"http://{endpoint_hostname}/{endpoint_path}"
            request_body = {
                "config_file": st.session_state.selected_config,
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
                st.session_state.response = requests.post(
                    endpoint,
                    json=request_body,
                )

                if st.session_state.response:
                    st.subheader("レスポンス")
                    response_viewer.render_viewer(st.session_state.response)
                    app_logger.api_success_log(st.session_state.response)

                    # APIアクションをセッションステートに追加
                    actions_viewer.add_action(
                        endpoint=endpoint,
                        method="POST",
                        request_body=request_body,
                        response_path=st.session_state.user_property_path,
                    )
                    st.success("Action added successfully.")

            except Exception as e:
                app_logger.error_log(f"Error: {e}")
                st.error(f"Error: {e}")

    # APIアクションの表示
    actions_viewer.render_actions()


if __name__ == "__main__":
    init_st_session_state()

    sidebar()
    main()

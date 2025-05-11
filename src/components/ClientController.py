# ClientController.py
from datetime import datetime
import time
import yaml

import streamlit as st


class ClientController:
    def __init__(self) -> None:
        if "api_running" not in st.session_state:
            st.session_state.api_running = False

    @st.dialog("Setting Info.")
    def modal(self, type):
        st.write(f"Modal for {type}:")
        if type == "save_api_actions":
            self.save_api_actions()
            self._modal_closer()
        else:
            st.write("No Definition.")

    def _modal_closer(self):
        if st.button(label="Close Modal"):
            st.info("モーダルを閉じます...")
            time.sleep(1)
            st.rerun()

    # 『保存』モーダル：
    def save_api_actions(self):
        with st.expander("Save Session State ?", expanded=False):
            pad = "stappApiRunnerActions.yaml"
            time_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            file_name = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}_{pad}"
            # セッション状態からパラメータを取得
            save_data = {
                "time_stamp": time_stamp,
                "api_acctions": st.session_state.api_actions,
            }

            # YAMLに変換
            yaml_str = yaml.dump(
                save_data, allow_unicode=True, default_flow_style=False
            )

            # ダウンロードボタンを表示
            st.download_button(
                label="Download as YAML",
                data=yaml_str,
                file_name=file_name,
                mime="text/yaml",
            )

    def _clear_states(self):
        st.session_state.api_running = False
        st.session_state.api_actions = []

    def render_buttons(self):
        st.write("##### Runner Ctrl.")
        (
            col1,
            col2,
            col3,
            col4,
            col5,
        ) = st.columns(5)
        with col1:
            if st.button(
                help="Stop Running",
                label="⏹️",
                disabled=(st.session_state.api_running is False),
            ):
                st.session_state.api_running = False
                st.rerun()
        with col2:
            if st.button(
                help="Save Helium States",
                label="📥",
                disabled=st.session_state.api_running,
            ):
                self.modal("save_api_actions")
        with col3:
            if st.button(
                help="Clear Helium States",
                label="🔄",
                disabled=st.session_state.api_running,
            ):
                self._clear_states()
                st.rerun()
        with col4:
            pass
        with col5:
            pass

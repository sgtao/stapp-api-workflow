# ActionsViewer.py
import time
from datetime import datetime

import streamlit as st


class ActionsViewer:
    def __init__(self):
        # セッションステートの初期化
        if "api_actions" not in st.session_state:
            st.session_state.api_actions = []

    def add_action(
        self,
        endpoint="http://xxx",
        method="POST",
        request_body=None,
        response_path="",
        response=None,
    ):
        # APIアクションをセッションステートに追加
        name = f"action_{len(st.session_state.api_actions) + 1:02d}_"
        if "config_file" in request_body:
            name = name + request_body["config_file"]
        else:
            # タイムスタンプをYYYY-MM-DD_hh:mm:ss形式に変換
            timestamp = time.time()
            formatted_time = datetime.fromtimestamp(timestamp).strftime(
                "%Y-%m-%d_%H:%M:%S"
            )
            name = name + formatted_time  # フォーマット済み文字列を使用

        action_info = {
            "endpoint": endpoint,
            "method": method,
        }
        if request_body is not None:
            action_info["request_body"] = request_body
        if response_path != "":
            action_info["response_path"] = response_path
        if response is not None:
            action_info["response"] = response

        st.session_state.api_actions.append(
            {
                "key": name,
                "value": action_info,
            }
        )

    def render_action_item(self, action):
        st.write(action)

    def render_actions(self):
        # st.session_state.hl_runner の内容を表示
        if len(st.session_state.api_actions) == 0:
            st.info("Action情報がありません。")
            return

        st.info("Registerd Action Info:")

        # 削除対象のアイテムを格納するリスト
        items_to_delete = []

        for i, item in enumerate(st.session_state.api_actions):
            variable_name = item["key"]
            action_info = item["value"]

            with st.expander(f"変数名: {variable_name}:", expanded=False):
                # チェックボックスを追加
                delete_checkbox = st.checkbox(
                    f"削除: {variable_name}", key=f"delete_{i}"
                )
                if delete_checkbox:
                    items_to_delete.append(i)
                # Actionデータの表示
                self.render_action_item(action_info)

        # 削除ボタンを追加
        if st.button("選択したアイテムを削除"):
            # 削除対象のアイテムをセッションステートから削除 (逆順に削除)
            for i in sorted(items_to_delete, reverse=True):
                del st.session_state.api_actions[i]

            st.success("選択したアイテムを削除しました。")
            st.rerun()  # アプリを再実行して表示を更新

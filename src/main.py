import streamlit as st

st.write(
    """
    ## Welcome to API Client Runner [Streamlit](https://streamlit.io/) App!
    """
)

# サイドバーのページに移動
# st.page_link("pages/example_app.py", label="Go to Example App")
st.page_link(
    "pages/11_api_client_runner.py",
    label="Go to API Client Runner Page",
    icon="🏃",
)
st.page_link(
    "pages/21_logs_viewer.py", label="Go to Log Viewer Page", icon="📄"
)

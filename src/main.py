import streamlit as st

st.write(
    """
    ## Welcome to API Client Runner [Streamlit](https://streamlit.io/) App!
    """
)

# サイドバーのページに移動
# st.page_link("pages/example_app.py", label="Go to Example App")
st.page_link(
    "pages/11_api_config_client.py",
    label="Go to API Config Client Page",
    icon="🔧",
)
st.page_link(
    "pages/21_logs_viewer.py", label="Go to Log Viewer Page", icon="📄"
)

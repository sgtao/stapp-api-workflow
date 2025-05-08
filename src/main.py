import streamlit as st

st.write(
    """
    # Welcome to [Streamlit](https://streamlit.io/)!
    Edit `/src` to customize this app to your heart's desire :heart:.
    """
)

# サイドバーのページに移動
# st.page_link("pages/example_app.py", label="Go to Example App")
st.page_link(
    "pages/11_api_client_runner.py", label="Go to Example App", icon="🏃"
)

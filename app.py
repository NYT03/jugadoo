import streamlit as st
from streamlit_extras.colored_header import colored_header

# Set up the page configuration
st.set_page_config(
    page_title="Jugadoo",
    page_icon="🎭",
    layout="centered",
)

# Get the current page from query parameters
page = st.experimental_get_query_params().get("page", ["home"])[0]

# Add a colored header for a modern look
colored_header(
    label="Welcome to Jugadoo!",
    color_name="blue-70",
    description="Where ideas come to life!",
)

# Add an image or logo (optional)
st.image(
    "./Jugadoo.png",  # Replace with your image URL or local file path
    use_container_width=True,
)

# Navigation buttons
if page == "home":
    st.markdown(
        """
        ---
        *Powered by Jugadoo Labs* 💡
        """
    )
elif page == "analysis":
    st.title("Text Insights Page")
    # Your analysis code here

elif page == "visual":
    st.title("Visual Analysis Page")
    # Your visual analysis code here

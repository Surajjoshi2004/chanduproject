import streamlit as st
import google.generativeai as genai
import random

# Set your Gemini API key
genai.configure(api_key="AIzaSyBSiY9Mi1db3LMDj8Py2YYBAsG_IHmIRwY")  # Replace with your API key

model = genai.GenerativeModel("gemini-1.5-pro")

# App Config
st.set_page_config(page_title="Recycling Buddy ♻️", page_icon="♻️")

# Custom CSS for light theme
st.markdown(
    """
    <style>
    .main {
        background-color: #ffffff;
    }
    h1, h2 {
        color: #00A878;
    }
    .stButton>button {
        background-color: #00A878;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ♻️ Banner Image
st.image(
    "https://images.unsplash.com/photo-1581579185169-b5fc4f3a635b",  # You can change this URL
    caption="Recycle Today for a Greener Tomorrow 🌍",
    use_column_width=True
)

# Title and intro
st.title("♻️ Recycling Buddy")
st.markdown("### Ask anything about recycling, waste sorting, or sustainable living!")

# User Input
user_input = st.text_input("🧠 What would you like to know?")

if user_input:
    with st.spinner("Thinking..."):
        try:
            prompt = f"You are a helpful recycling expert. Answer clearly and simply. {user_input}"
            response = model.generate_content(prompt)
            st.success("🤖 " + response.text)
        except Exception as e:
            st.error(f"⚠️ Something went wrong: {e}")

# 🌱 Divider
st.markdown("---")
st.subheader("🌱 Daily Eco Challenge")

eco_challenges = [
    "🚯 Avoid single-use plastic today!",
    "♻️ Reuse a glass jar instead of throwing it away.",
    "💧 Save water by turning off the tap while brushing.",
    "🛍️ Carry a cloth bag when you go out.",
    "🔋 Collect used batteries to recycle them responsibly."
]

if st.button("Give me a challenge!"):
    st.info(random.choice(eco_challenges))

# Footer Image
st.markdown("----")
st.image(
    "https://images.unsplash.com/photo-1565374399586-13c36c71d79e",
    caption="🌎 Every small step counts!",
    use_column_width=True
)

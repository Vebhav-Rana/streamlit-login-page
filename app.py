import streamlit as st

st.set_page_config(
    page_title="Student Login Portal",
    page_icon="🔐",
    layout="centered"
)

# Header
st.title("🔐 Student Login Portal")
st.subheader("Streamlit Lab 6 - User Authentication Demo")

st.markdown("---")

# User Details
username = st.text_input("👤 Username")
email = st.text_input("📧 Email Address")
password = st.text_input("🔑 Password", type="password")

course = st.selectbox(
    "📚 Select Course",
    ["BCA", "BSc CS", "BTech", "MCA"]
)

year = st.radio(
    "🎓 Year",
    ["1st Year", "2nd Year", "3rd Year"]
)

remember = st.checkbox("Remember Me")

st.markdown("---")

if st.button("Login"):

    if username == "" or email == "" or password == "":
        st.error("Please fill all fields")

    else:
        st.success("Login Successful!")

        st.write("### User Details")
        st.write(f"**Username:** {username}")
        st.write(f"**Email:** {email}")
        st.write(f"**Course:** {course}")
        st.write(f"**Year:** {year}")

        if remember:
            st.info("Remember Me Enabled")

# Sidebar
st.sidebar.header("About")
st.sidebar.write(
    "This application demonstrates a "
    "simple login interface built using Streamlit."
)

# Footer
st.markdown("---")
st.caption("Created for Streamlit Lab 6")
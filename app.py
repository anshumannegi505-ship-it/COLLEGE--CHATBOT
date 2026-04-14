import streamlit as st
import time

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Graphic Era Smart Chatbot",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

h1 {
    text-align: center;
    color: #4CAF50;
}

[data-testid="stChatMessage"] {
    border-radius: 15px;
    padding: 12px;
    margin: 8px;
    background-color: #1e293b;
}

[data-testid="stChatMessage"] p {
    color: white !important;
    font-weight: bold;
    font-size: 16px;
}

section[data-testid="stSidebar"] {
    background-color: #020617;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown("""
<h1>🎓 Graphic Era Smart Assistant</h1>
<p style='text-align:center;'>Your 24/7 College Help Partner 🤖</p>
""", unsafe_allow_html=True)

# -------------------------------
# Welcome Message
# -------------------------------
if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = True
    st.info("👋 Welcome! Ask me anything about Graphic Era University.")

# -------------------------------
# College Data
# -------------------------------
college_data = {
    "about": """LOCATION: Dehradun, Uttarakhand
ESTABLISHED: 1997
Founder: Prof. (Dr.) Kamal Ghanshala
Type: Private Deemed University
Accreditation: NAAC A+ Grade
Approved by: UGC, AICTE""",

    "courses": "B.Tech, BCA, MBA, BBA, B.Com, MCA (100+ courses including UG, PG, PhD, Diploma)",

    "fees": "B.Tech: ₹2.5–3.5 LPA | BCA: ₹1.2–1.5 LPA per year",

    "placement": "Highest: ₹65+ LPA | Average: ₹5–8 LPA",

    "hostel": """Hostels:
- Chandra Shekhar Azad Hostel
- Sardar Patel Hostel
- Netaji Subhash Chandra Hostel
- Sai Hostel

Hostel Fees: Approx ₹1,60,000/year (may vary)""",

    "faculty": "600+ Faculty members | Many are PhD holders"
}

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📌 Quick Menu")

option = st.sidebar.selectbox(
    "Select Option",
    ["Chat Mode", "About", "Courses", "Fees", "Placement", "Hostel", "Faculty"]
)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# -------------------------------
# Session State
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Sidebar Output
# -------------------------------
if option != "Chat Mode":
    st.success(college_data.get(option.lower(), "Data not available"))

# -------------------------------
# Chat Input
# -------------------------------
user_input = st.chat_input("Ask something...")

# -------------------------------
# Chatbot Logic
# -------------------------------
def get_response(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["fee", "cost", "price"]):
        return college_data["fees"]

    elif any(word in user_input for word in ["course", "study", "program"]):
        return college_data["courses"]

    elif "hostel" in user_input:
        return college_data["hostel"]

    elif any(word in user_input for word in ["placement", "job"]):
        return college_data["placement"]

    elif "faculty" in user_input:
        return college_data["faculty"]

    elif any(word in user_input for word in ["about", "college", "university"]):
        return college_data["about"]

    elif any(word in user_input for word in ["hi", "hello", "hey"]):
        return "👋 Hello! How can I help you today?"

    else:
        return "❗ Please ask something related to fees, courses, placement, hostel, etc."

# -------------------------------
# Typing Effect
# -------------------------------
def type_effect(text):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f"**{typed_text}**")
        time.sleep(0.005)

# -------------------------------
# Show Previous Messages
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f"**{msg['content']}**")

# -------------------------------
# Handle New Message
# -------------------------------
if user_input:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(f"**{user_input}**")

    # Generate response
    response = get_response(user_input)

    # Store response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Display response
    with st.chat_message("assistant"):
        type_effect(response)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Made by Anshuman & Mayank 🚀</p>",
    unsafe_allow_html=True
)



     
    
   
  
    


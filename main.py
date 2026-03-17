import streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email

st.set_page_config(page_title="MailMate – Think Less, Send Smart", layout="wide")
st.title("📧 MailMate – Think Less, Send Smart")
st.markdown("AI-powered email responder — paste an email, pick a tone, and let MailMate do the rest.")
st.divider()

# --- Sender Credentials ---
st.subheader("🔐 Your Sender Credentials")
col1, col2 = st.columns(2)
with col1:
    sender_email = st.text_input("Your Gmail Address", placeholder="you@gmail.com")
with col2:
    sender_password = st.text_input(
        "Your Gmail App Password",
        type="password",
        placeholder="16-character app password",
        help="Generate at myaccount.google.com/apppasswords (requires 2FA)"
    )

st.divider()

# --- Email Content ---
st.subheader("✉️ Email to Reply To")
email_text = st.text_area("Paste the email content you received:", height=250)

st.divider()

# --- Response Settings ---
st.subheader("⚙️ Response Settings")
col3, col4 = st.columns(2)
with col3:
    recipient_email = st.text_input("Recipient Email Address", placeholder="recipient@example.com")
with col4:
    tone = st.selectbox("Select response tone", ["Professional", "Friendly", "Apologetic", "Persuasive"])

st.divider()

if st.button("🚀 Generate & Send Email", use_container_width=True):
    if not sender_email or not sender_password:
        st.warning("⚠️ Please enter your Gmail address and App Password.")
    elif not recipient_email:
        st.warning("⚠️ Please enter the recipient's email address.")
    elif not email_text:
        st.warning("⚠️ Please paste the email content you want to reply to.")
    else:
        with st.spinner("✨ Generating smart reply and sending..."):
            response = generate_email_response(email_text, tone)
            send_status = send_email(
                recipient=recipient_email,
                body=response,
                sender_email=sender_email,
                sender_password=sender_password
            )
            st.subheader("📨 Generated Reply")
            st.markdown(response)
            if send_status:
                st.success(f"✅ Email sent successfully to {recipient_email}!")
            else:
                st.error("❌ Failed to send email. Check your Gmail address and App Password.")

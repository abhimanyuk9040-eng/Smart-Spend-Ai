import smtplib
from email.mime.text import MIMEText
import streamlit as st


def send_email(to_address, subject, body):
    try:
        gmail_address = st.secrets["GMAIL_ADDRESS"]
        gmail_password = st.secrets["GMAIL_APP_PASSWORD"]

        message = MIMEText(body)

        message["Subject"] = subject
        message["From"] = gmail_address
        message["To"] = to_address

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_address, gmail_password)
            server.send_message(message)

        return True

    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False
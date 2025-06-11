import smtplib
from email.message import EmailMessage

# User input for security (you could also use environment variables)
sender_email = input("Enter your Gmail address: ")
app_password = input("Enter your app password: ")
recipient_email = input("Enter recipient email: ")
subject = input("Enter subject: ")
body = input("Enter your message: ")

# Compose the email
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.set_content(body)

# Send the email using Gmail SMTP server
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Failed to send email: {e}")

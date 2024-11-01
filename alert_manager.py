import smtplib
from config import smtp_email, smtp_password, smtp_port, smtp_server

def send_email_alert(drift_details, to_email):
    subject = "Dependency Drift Detected"
    body = f"Drift Details:\n{drift_details}"
    message = f"Subject: {subject}\n\n{body}"
  
    with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
        server.starttls()
        server.login(smtp_email, smtp_password)
        server.sendmail(smtp_email, to_email, message)


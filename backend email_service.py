from sendgrid.helpers.mail import Mail
import sendgrid
import os

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

def send_followup_email(email, name, stage):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    
    subject = "Let's Move Forward" if stage == "Negotiation" else "Checking in!"
    message_content = f"<p>Hi {name},<br><br>Just checking in as you're in the {stage} stage. Let me know if you have any questions!</p>"

    message = Mail(
        from_email="sales@zafo.ai",
        to_emails=email,
        subject=subject,
        html_content=message_content
    )
    response = sg.send(message)
    return response.status_code

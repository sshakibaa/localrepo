import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "sadmansakib25350@gmail.com"
receiver_email = "abdullah0303815@gmail.com"
password = "wkeketosguhfuidj"  # Use app password or environment variable for security

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email"

body = "This is a test email sent using Python by Shadman!\nkire baincod tor dud boro hoice ni?"
message.attach(MIMEText(body, "plain"))

try:
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    server.ehlo()        # Identify to server
    server.starttls()    # Encrypt connection
    server.ehlo()        # Identify again after encryption
    
    # Login and send
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    
    print("Email sent successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    
finally:
    server.quit()  # Close connection


"""
## Visual Flow
```
1. Connect to server (port 587)
   ↓
2. server.ehlo() → "Hello, I'm a client"
   ↓
3. server.starttls() → "Let's encrypt our conversation"
   ↓
4. server.ehlo() → "Hello again (now encrypted)"
   ↓
5. server.login() → Send credentials (safely encrypted)
   ↓
6. server.sendmail() → Send the email
   ↓
7. server.quit() → Close connection

"""

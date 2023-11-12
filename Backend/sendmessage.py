from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
user_phone_number = 'user_phone_number'  # Replace with the user's actual phone number

client = Client(account_sid, auth_token)

def send_sms(message):
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=user_phone_number
    )
    return message.sid

def predict_and_notify(file_path):
    result = predict(file_path)
    print(result)

    # Check if the predicted class is not healthy
    if result['class'] not in ['Potato___healthy', 'Tomato_healthy', 'Pepper__bell___healthy']:
        message = f"Alert: Unhealthy plant detected - Class: {result['class']}, Confidence: {result['confidence']}"
        send_sms(message)
        print("SMS Sent!")
    else:
        print("No action needed.")

if __name__ == "__main__":
    image_file_path = "potato_exl.jpeg"  # Replace with the path to your image file
    predict_and_notify(image_file_path)

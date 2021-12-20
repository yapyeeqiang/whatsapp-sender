# Whatsapp Sender

Whatsapp Sender automates sending of messages via Whatsapp Web. The tool allows
you to send whatsapp messages in bulk. This program reads the list of contacts
you provide and send a predefined message to each number in the list.

# Requirements

-   Python 3.x
-   Chrome v79

# Setup

1. Install python - v3.x
2. Run `pip install -r requirements.txt`

# Steps

1. Enter the message you want to send inside `message.txt` file.
2. Enter the list of numbers line-separated in `contacts.txt` file.
3. Run `python app.py`.
4. Once the program starts, you'll see the message in message.txt and count of
   contact in the contacts.txt file.
5. After a while, Chrome should pop-up and open web.whatsapp.com.
6. Scan the QR code to login into whatsapp.
7. Press `Enter` to start sending out messages.
8. Magic!

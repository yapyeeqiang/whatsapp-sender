from urllib.parse import quote
from time import sleep
from .file import write_file, clean_file
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

cwd = os.path.abspath(os.getcwd())

WHATSAPP_WEB_URL = 'https://web.whatsapp.com'
DELAY = 50


def print_empty_lines(n):
    for i in range(n):
        print('\n')


def generate_link(contact, message, web=False):
    message = quote(message)

    if web:
        return f"https://web.whatsapp.com/send?phone={contact}&text={message}"
    else:
        return f"https://wa.me/{contact}&text={message}"


def send_message(driver, contacts, message):
    print_empty_lines(2)
    print(f"Once your browser opens up, sign in to WhatsApp Web...")
    print("Wait for your chats to be visible so you don't have to sign in again.")
    print_empty_lines(1)

    driver.get(WHATSAPP_WEB_URL)

    # Wait for chats to be visible
    start = False

    try:
        while not start:
            element = driver.find_element_by_tag_name('progress')

            if not element:
                start = True
    except Exception as e:
        pass
    
    
    contacts = [x for x in contacts if x]

    clean_file(f"{cwd}/assets/invalid_contacts.txt")

    for index, contact in enumerate(contacts):

        sending_index = index + 1
        total_contacts = len(contacts)


        if contact == "":
            continue

        print(f"{sending_index}/{total_contacts} => Sending message to {contact}.")

        try:
            whatsapp_url = generate_link(contact, message, web=True)
            message_sent = False

            if not message_sent:
                driver.get(whatsapp_url)

                try:
                    send_button = WebDriverWait(driver, DELAY).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))
                except Exception as e:
                    print(f"Something went wrong...")
                    print(f"Failed to send message to this contact: {contact}.")

                    print_empty_lines(1)

                    write_file(f"{cwd}/assets/invalid_contacts.txt", contact)

                    continue
            else:
                sleep(1)

                print('hehe')

                send_button.click()
                message_sent = True

                sleep(3)

                print(f"Message sent to: {contact}")
                print_empty_lines(1)

        except Exception as e:
            print(f"Failed to send message to {contact}: {str(e)}")

from urllib.parse import quote
from time import sleep
from .phone_number import is_phone_valid
from .file import write_file, clean_file
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
# from termcolor import colored

cwd = os.path.abspath(os.getcwd())

WHATSAPP_WEB_URL = 'https://web.whatsapp.com'
DELAY = 30


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

    input("Press any key to start...")

    contacts = [x for x in contacts if x]

    clean_file(f"{cwd}/assets/invalid_contacts.txt")

    for index, contact in enumerate(contacts):
        isPhoneValid = is_phone_valid(contact)

        sending_index = index + 1
        total_contacts = len(contacts)

        # if not isPhoneValid:
        #     print(f"{sending_index}/{total_contacts} => Phone number is invalid.")
        #     print_empty_lines(1)

        #     write_file(f"{cwd}/assets/invalid_contacts.txt", contact)

        #     continue

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
                    # print(f"Failed to send message to this contact: {contact}, retry ({sending_index}/3)")
                    # print_empty_lines(1)
                    # print("Make sure your phone and computer are connected to the internet.")
                    # print("If there is an alert, please dismiss it.")
                    # print_empty_lines(1)
                    # input("Press any key to continue...")
                else:
                    sleep(1)

                    send_button.click()
                    message_sent = True

                    sleep(3)

                    print(f"Message sent to: {contact}")
                    print_empty_lines(1)

        except Exception as e:
            print(f"Failed to send message to {contact}: {str(e)}")

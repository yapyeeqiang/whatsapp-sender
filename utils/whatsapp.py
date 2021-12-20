from urllib.parse import quote
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import colored

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
    print(f"Once your browser opens up, sign in to {colored('WhatsApp Web', 'green')}...")
    print("Wait for your chats to be visible so you don't have to sign in again.")
    print_empty_lines(1)

    driver.get(WHATSAPP_WEB_URL)

    input("Press any key to start...")

    contacts = [x for x in contacts if x]

    for index, contact in enumerate(contacts):
        sending_index = index + 1
        total_contacts = len(contacts)

        if contact == "":
            continue

        print(
            f"{sending_index}/{total_contacts} => {colored('Sending message', 'yellow')} to {colored(contact, 'cyan')}.")

        try:
            whatsapp_url = generate_link(contact, message, web=True)
            message_sent = False

            for i in range(3):
                if not message_sent:
                    driver.get(whatsapp_url)

                    try:
                        send_button = WebDriverWait(driver, DELAY).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))
                    except Exception as e:
                        print(f"{colored('Something went wrong', 'red')}...")
                        print(f"{colored('Failed to send message', 'red')} to this contact: {colored(contact, 'cyan')}, retry ({sending_index}/3)")
                        print_empty_lines(1)
                        print("Make sure your phone and computer are connected to the internet.")
                        print("If there is an alert, please dismiss it.")
                        print_empty_lines(1)
                        input("Press any key to continue...")
                    else:
                        sleep(1)

                        send_button.click()
                        message_sent = True

                        sleep(3)

                        print(f"{colored('Message sent', 'green')} to: {contact}")
                        print_empty_lines(1)

        except Exception as e:
            print(f"Failed to send message to {colored(contact, 'cyan')}: {str(e)}")

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from urllib.parse import quote
from utils import read_file

# Get messages
message = read_file("message.txt")
message = quote(message)

# Get all contacts
contacts = read_file("contacts.txt", arr=True)

# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)

# print('Once your browser opens up sign in to web whatsapp')
# driver.get('https://web.whatsapp.com')
# input("Press ENTER after login into Whatsapp Web and your chats are visible.")

# for index, number in enumerate(contacts):
# 	sending_index = index + 1
# 	total_contacts = len(contacts)
# 	number = number.strip()

# 	if number == "":
# 		continue

# 	print(f'{sending_index}/{total_contacts} => Sending message to {number}.')

# 	try:
# 		url = f'https://web.whatsapp.com/send?phone={number}&text={message}'
# 		sent = False

# 		for i in range(3):
# 			if not sent:
# 				driver.get(url)
# 				try:
# 					send_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME , '_4sWnG')))
# 				except Exception as e:
# 					print(f"Something went wrong..\n Failed to send message to: {number}, retry ({sending_index}/3)")
# 					print("Make sure your phone and computer is connected to the internet.")
# 					print("If there is an alert, please dismiss it.")
# 					input("Press enter to continue")
# 				else:
# 					sleep(1)
# 					send_button.click()
# 					sent = True
# 					sleep(3)
# 					print(f'Message sent to: {number}')
# 	except Exception as e:
# 		print(f'Failed to send message to {number}: {str(e)}')

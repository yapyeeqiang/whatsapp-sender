from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.file import read_file
from utils.whatsapp import send_message
import os

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument(r"user-data-dir=./driver/cache")
chrome_options.add_argument( "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36")
chrome_options.add_argument("remote-debugging-port=3333")

cwd = os.path.abspath(os.getcwd())

# Get messages
message = read_file(f"{cwd}/assets/message.txt")

# Get all contacts
contacts = read_file(f"{cwd}/assets/contacts.txt", array=True)

# Initialize Chrome Driver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

# Send WhatsApp Message
send_message(driver=driver, contacts=contacts, message=message)
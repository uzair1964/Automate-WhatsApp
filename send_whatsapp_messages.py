import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_chat(driver, contact, retries: int = 3) -> bool:
    """Search for a contact and open the chat.

    Parameters
    ----------
    driver: webdriver
        Selenium webdriver instance.
    contact: str
        Phone number or contact name to search.
    retries: int
        Number of attempts before giving up.
    """
    for attempt in range(retries):
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
                )
            )
            search_box.clear()
            search_box.send_keys(str(contact))
            time.sleep(2)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)
            return True
        except Exception as exc:  # pragma: no cover - runtime environment
            print(f"Attempt {attempt + 1} to open chat with {contact} failed: {exc}")
            time.sleep(5)
    print(f"Failed to open chat with {contact}. Skipping.")
    return False


def main():
    options = Options()
    # options.add_argument("--headless")  # Uncomment to run Chrome without a window

    # Update the path to your ChromeDriver executable
    service = Service(executable_path="chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://web.whatsapp.com/")
    print("Scan the QR code and wait for the page to load...")

    try:
        WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.XPATH, '//span[@data-icon="chat"]'))
        )
        print("WhatsApp Web is working!")
    except Exception as exc:  # pragma: no cover - runtime environment
        print("Failed to load WhatsApp Web:", exc)
        driver.quit()
        return

    # Load contacts from Excel
    df = pd.read_excel("contacts.xlsx")  # Expects a column named 'Phone Number'

    # Example attachments list (replace with your file paths)
    attachments: list[str] = []

    message = "Hello, this is a test message with attachments."

    for _, row in df.iterrows():
        contact = row["Phone Number"]

        if not open_chat(driver, contact):
            continue

        # Send attachments
        for file_path in attachments:
            try:
                attach_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@title="Attach"]'))
                )
                attach_button.click()

                file_input = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
                )
                file_input.send_keys(file_path)
                time.sleep(2)

                send_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
                )
                send_button.click()
                print(f"Attachment {file_path} sent to {contact}")
                time.sleep(2)
            except Exception as exc:  # pragma: no cover - runtime environment
                print(f"Error while sending attachment {file_path} to {contact}: {exc}")

        # Send text message
        try:
            message_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
                )
            )
            message_box.send_keys(message)
            message_box.send_keys(Keys.RETURN)
            print(f"Message sent to {contact}")
        except Exception as exc:  # pragma: no cover - runtime environment
            print(f"Error while sending message to {contact}: {exc}")

        time.sleep(3)

    driver.quit()
    print("All messages with attachments have been sent!")


if __name__ == "__main__":  # pragma: no cover - script entry point
    main()

<!-- Logo (put your file at assets/logo.png) -->
<p align="center">
  <img src="assets/logo.png" alt="Automate WhatsApp Logo" width="240">
</p>

<h1 align="center">Automate WhatsApp</h1>

<p align="center">
  Automate WhatsApp Web to send personalized bulk messages from a spreadsheet using Python, Selenium, and Pandas.
</p>

<p align="center">
  <!-- Tech Badges -->
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Selenium-%20-brightgreen?logo=selenium&logoColor=white" alt="Selenium">
  <img src="https://img.shields.io/badge/Pandas-%20-black?logo=pandas&labelColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Status-Educational%20use%20only-informational" alt="Status">
</p>

---

## Overview
This project uses **Python + Selenium + Pandas** to automate common WhatsApp Web tasks like opening chats and sending personalized messages read from a file (e.g., Excel/CSV). It runs locally in your browser and requires a one-time QR scan to authenticate your WhatsApp Web session. :contentReference[oaicite:0]{index=0}

---

## Why this project?
- **Bulk messages without saving contacts:** Sending many messages manually or by saving numbers is slow and error-prone; this automates the flow for controlled, one-by-one delivery. :contentReference[oaicite:1]{index=1}  
- **Learning automation stack:** Practical example of browser automation (**Selenium**) plus tabular data handling (**Pandas**) and simple orchestration in Python/Jupyter. :contentReference[oaicite:2]{index=2}  
- **Reproducible outreach:** Read recipients and messages from a spreadsheet to keep runs auditable and repeatable.  
- **Local control:** Runs on your machine in a regular browser session; you decide timing, content, and recipients.

> ⚠️ **Important:** Automating WhatsApp may violate WhatsApp’s Terms of Service. This repository is for **educational purposes** only. Use responsibly, obtain consent from recipients, and follow local regulations. :contentReference[oaicite:3]{index=3}

---

## Features
- Send personalized text messages to a list of numbers from an Excel/CSV (e.g., `Phone Number`, optional `Message`).  
- Drive WhatsApp Web via Chrome/Chromedriver using Selenium after a QR code scan. :contentReference[oaicite:4]{index=4}

---

## Requirements
- **Python 3.x**, **Selenium**, **Pandas**  
- **Google Chrome** + matching **ChromeDriver** version  
- (Optional) **Jupyter Notebook** for exploration/experiments  
Install Python deps:
```bash
pip install selenium pandas

python send_whatsapp_messages.py
```
Scan the QR code in the browser window and let the automation send the messages.

## Disclaimer
This code is provided for learning purposes. Use it responsibly and comply with WhatsApp's terms and local laws.

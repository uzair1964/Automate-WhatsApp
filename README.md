# 📱 WhatsApp Automation

[![Python](https://img.shields.io/badge/Python-3.x-3776AB)]()
[![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A)]()
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Frames-150458)]()
[![Status](https://img.shields.io/badge/Project-Notebook-000000)]()

## Overview
This project uses **Python + Selenium + Pandas** to automate **WhatsApp Web** tasks like opening chats, sending messages, and handling data for analysis.

## Motivation
I built this to **send bulk messages without saving contacts**.
When attempted manually, WhatsApp temporarily **blocked** me for **multiple forwards** (not officially allowed).
Automating the flow in a controlled way lets me handle messaging programmatically for learning and experimentation.

> ⚠️ **Important:** Automating WhatsApp may violate WhatsApp’s **Terms of Service**. This project is for **educational purposes only**. Use at your own risk and respect recipient consent and local regulations.

## Requirements
- Python **3.x**
- **Selenium**
- **Pandas**
- **Chrome WebDriver** (version must match your Chrome)

## Setup
1) Install dependencies:
```bash
pip install selenium pandas
```
2) Download the ChromeDriver that matches your browser and update the script with its path.
3) Prepare an Excel file `contacts.xlsx` with a column `Phone Number`. Optional columns such as `Message` can be added.
4) Run the script:
```bash
python send_whatsapp_messages.py
```
Scan the QR code in the browser window and let the automation send the messages.

## Disclaimer
This code is provided for learning purposes. Use it responsibly and comply with WhatsApp's terms and local laws.

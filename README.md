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
## 🧭 Introduction
**Automate-WhatsApp** is a local Python automation that drives **WhatsApp Web** in your browser to send **personalized messages** from a spreadsheet (CSV/Excel).  
It uses **Selenium** to open chats and **pandas** to read rows, helping you run controlled, one-by-one outreach without saving every number to contacts.

> ⚠️ **Important:** Automating WhatsApp may violate WhatsApp’s Terms of Service. This project is for **educational purposes** only. Obtain consent, avoid spam, and follow local laws. The code does **not** bypass WhatsApp policies or limits.

## 🛠️ Project Type
Backend (local browser automation with Python + Selenium)

## 🚀 Deployed App
- Frontend: Not applicable  
- Backend: Python script / Jupyter notebook  
- Browser: Google Chrome + WhatsApp Web  
- Driver: ChromeDriver (matching your Chrome version)

## 📁 Directory Structure
```Automate-WhatsApp/
├─ README.md
├─ send_whatsapp_messages.py # main automation script
├─ whatsapp.ipynb # optional exploratory notebook
├─ contacts.xlsx # example: Phone Number, Message
└─ assets/
└─ logo.png (optional)
```
## Overview
This project uses **Python + Selenium + Pandas** to automate common WhatsApp Web tasks like opening chats and sending personalized messages read from a file (e.g., Excel/CSV). It runs locally in your browser and requires a one-time QR scan to authenticate your WhatsApp Web session. :contentReference[oaicite:0]{index=0}

---

## Why this project?
- **Bulk messages without saving contacts:** Sending many messages manually or by saving numbers is slow and error-prone; this automates the flow for controlled, one-by-one delivery. :contentReference[oaicite:1]{index=1}  
- **Learning automation stack:** Practical example of browser automation (**Selenium**) plus tabular data handling (**Pandas**) and simple orchestration in Python/Jupyter. :contentReference[oaicite:2]{index=2}  
- **Reproducible outreach:** Read recipients and messages from a spreadsheet to keep runs auditable and repeatable.  
- **Local control:** Runs on your machine in a regular browser session; you decide timing, content, and recipients.

>
## ✨ Features
- **Spreadsheet-driven**: read recipients & messages from CSV/Excel  
- **Personalized text**: use a message column per row (e.g., includes customer name)  
- **Local & visible**: runs in your Chrome session after **QR login**  
- **Console logs**: see progress/success/failure while sending

## 🎯 Design Decisions & Assumptions
- Uses **WhatsApp Web**; requires manual QR authentication
- Chrome + **ChromeDriver** is assumed (or use `webdriver-manager` to auto-manage)
- Input file has columns like **`Phone Number`** and **`Message`** (sample below)
- Intent is controlled, consent-based messaging—**no bulk spam**

## 🧪 Installation & Getting Started
```bash
# Clone your repo
git clone https://github.com/uzair1964/Automate-WhatsApp
cd Automate-WhatsApp

# (Optional) create a virtual environment
# python -m venv .venv && source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate                                 # Windows

# Install dependencies (Option A: if requirements.txt exists)
pip install -r requirements.txt

# Or Option B: install key packages directly
pip install selenium pandas openpyxl webdriver-manager
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


-Python 3.x
-Selenium (browser automation)
-pandas / openpyxl (spreadsheet I/O)
Jupyter Notebook (optional exploration)
## Disclaimer
This code is provided for learning purposes. Use it responsibly and comply with WhatsApp's terms and local laws.

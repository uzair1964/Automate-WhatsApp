📱 WhatsApp Automation
Overview

This project uses Python + Selenium + Pandas to automate WhatsApp Web tasks such as opening chats, extracting messages, and handling data for analysis.

Requirements

Python 3.x

Selenium

Pandas

Chrome WebDriver

Setup

Install dependencies:

pip install selenium pandas


Download and install ChromeDriver matching your Chrome version.

Open the notebook whatsapp.ipynb in Jupyter.

Usage

Run the first cell to import libraries and set up Selenium.

Launch WhatsApp Web in the automated Chrome window.

Scan the QR code with your mobile to log in.

Run the next cell to extract chats/messages into Pandas for analysis.

Features

Automates WhatsApp Web login (via QR scan).

Reads chats and messages using Selenium.

Saves extracted data into Pandas DataFrames.

Note

This project is for educational purposes only. Automating WhatsApp may violate WhatsApp’s Terms of Service.

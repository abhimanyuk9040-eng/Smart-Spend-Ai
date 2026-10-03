💰 SmartSpend AI
AI-Powered Receipt Analysis & Expense Management

SmartSpend AI is a Python-based web application that uses Google Gemini Vision to understand receipts and bills from images. It extracts important expense information such as items, prices, taxes, discounts, total amount, payment method, and expense category.

The application also provides a bill-splitting feature and allows users to send their expense summary through email.

🎯 1. Project Objective

The main objective of SmartSpend AI is to make expense management easier.

Instead of manually entering every item from a bill, the user can simply:

Take / Upload Receipt
        ↓
AI Reads Receipt
        ↓
Expense Information Extracted
        ↓
View Spending Details
        ↓
Split Bill
        ↓
Send Summary

This reduces manual work and makes bill analysis faster.

🧠 2. How Our Project Works

The project follows a simple AI-based workflow.

Step 1 — User Uploads a Receipt

The user uploads a:

JPG
JPEG
PNG

image of a receipt or bill.

Step 2 — Image Goes to Gemini

The uploaded image is sent to Google Gemini along with instructions explaining what information needs to be extracted.

Step 3 — Gemini Understands the Receipt

Gemini analyzes the image and identifies information such as:

Item
Quantity
Price
Subtotal
Tax
Discount
Total
Payment Method
Category
Step 4 — Application Displays the Result

The extracted information is shown inside the Streamlit application.

Step 5 — Bill Splitting

The user enters the number of people sharing the bill.

For example:

Total Bill = ₹609
People = 3

₹609 ÷ 3 = ₹203
Step 6 — Email Summary

The user can enter an email address and send the expense information as a summary.

🛠️ 3. Technologies Used
Technology	Use in Project
Python	Application development
Streamlit	Web interface
Google Gemini	AI receipt understanding
Pillow	Processing uploaded images
Gmail SMTP	Sending email
Git	Version control
GitHub	Project repository
📁 4. Project Structure
SmartSpend-AI/
│
├── .streamlit/
│   └── secrets.toml   ← local only, not uploaded to GitHub
│
├── app.py
├── prompts.py
├── action_tool.py
├── requirements.txt
├── .gitignore
└── README.md
File Purpose

app.py
Main application. It contains the Streamlit interface, receipt upload, Gemini analysis, bill splitting, and email functionality.

prompts.py
Contains instructions that define how SmartSpend AI should understand and respond to receipt information.

action_tool.py
Handles email delivery using Gmail SMTP.

requirements.txt
Contains the Python libraries required by the project.

.streamlit/secrets.toml
Stores private API keys and Gmail credentials.

.gitignore
Prevents private files such as secrets.toml and the virtual environment from being uploaded to GitHub.

🚀 5. Development Steps

We developed SmartSpend AI in the following stages.

Phase 1 — Project Setup

Created the project folder and Python virtual environment.

python -m venv venv

Activated it:

.\venv\Scripts\activate
Phase 2 — Install Dependencies

Installed the required libraries:

pip install streamlit
pip install google-genai
pip install pillow
Phase 3 — Create the Streamlit Interface

Created the basic application containing:

Project title
Receipt uploader
Analyze button
Expense analysis section
Bill splitter
Email section

* Main Features
📸 Receipt Analysis

Upload a receipt and allow AI to extract the expense details.

🧾 Item-Level Information

Displays individual items, quantities, and prices.

💰 Total Detection

Automatically identifies the final bill amount.

🏷️ Expense Categorization

Attempts to classify the expense into categories such as:

Food
Shopping
Travel
Bills
Entertainment
Other
👥 Bill Splitting

Calculates the amount each person needs to pay.

📧 Email Summary

Sends the analyzed expense information to an email address.

⚠️ Unclear Receipt Handling

If information cannot be read properly, the AI is instructed not to invent values.

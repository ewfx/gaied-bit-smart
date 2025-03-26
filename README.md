# 🚀 AI Email Orchestrator & Triage System

## 📌 Table of Contents
- [Introduction](#introduction)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
---

## 🎯 Introduction
This project implements an AI-powered solution for automating the classification, data extraction, and routing of emails in a commercial bank's lending service team. The system processes incoming emails and attachments, extracts key information, classifies the emails into predefined request types, and routes them to appropriate teams.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/gaied-bit-smart.git
   ```
2. Install dependencies  
   ```sh
   Create a virtual environment and install required dependencies:

   bash
   Copy code
   python3 -m venv venv
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   Set Up OpenAI API Key
   To use OpenAI's GPT for classification, you need to set your API key. You can get the API key from OpenAI's platform.
   Create a .env file and add your API key like this:
   ini
   Copy code
   OPENAI_API_KEY=your-openai-api-key
   Alternatively, you can set the environment variable directly:
   bash
   Copy code
   export OPENAI_API_KEY=your-openai-api-key
   ```
3. Run the project  
   ```sh
   npm start  # or python app.py
   ```

## 🏗️ Tech Stack
- OpenAI GPT API for email classification and data extraction.
- Tesseract OCR for Optical Character Recognition (OCR) on attachments.
- Flask for creating the HTTP API.
- Google Cloud (Functions/Run/Compute Engine) for deployment.
- pandas, scikit-learn, and other Python libraries for data processing and duplicate detection.

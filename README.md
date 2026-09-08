# NewsPulse

## Overview

NewsPulse is a Python application that fetches the latest news articles using NewsAPI, categorizes them into different topics, generates a news digest, and delivers it via email.

## Features

* Fetches real-time news articles from NewsAPI
* Categorizes news into different topics
* Generates a categorized news digest
* Delivers the news digest through email
* Uses environment variables to securely store API keys and email credentials

## Technologies Used

* Python
* Requests
* SMTP
* NewsAPI
* Python Dotenv

## Project Structure

newspulse/

├── app.py

├── fetcher.py

├── analyzer.py

├── email_sender.py

├── config.py

├── requirements.txt

├── .gitignore

├── .env.example

└── README.md

## Installation

1. Clone the repository

git clone https://github.com/sakshi-dhakne/NewsPulse.git

2. Navigate to the project directory

cd NewsPulse

3. Install dependencies

pip install -r requirements.txt

4. Create a .env file and add your credentials

NEWS_API_KEY=your_api_key

EMAIL=[your_email@gmail.com](mailto:your_email@gmail.com)

EMAIL_PASSWORD=your_app_password

RECEIVER_EMAIL=[receiver@gmail.com](mailto:receiver@gmail.com)

## Usage

Run the application:

python app.py

The application will:

1. Fetch the latest news articles.
2. Categorize the articles.
3. Create a news digest.
4. Send the digest to the configured email address.

## Future Improvements

* Support multiple news sources
* Add AI-based news summarization
* Generate HTML email reports
* Schedule automatic daily email delivery
* Build a web dashboard

## Author

Developed as a Python learning project to practice API integration, data processing, and email automation.

# Stock News Alert

## Description

This project monitors the stock price of a specified company. If the stock price changes by a significant percentage between yesterday and the day before, it fetches the latest news about the company and sends you an SMS notification with the price change and the top 3 news headlines.

This project utilizes the following APIs:
*   [Alpha Vantage API](https://www.alphavantage.co/) for stock data.
*   [News API](https://newsapi.org/) for news articles.
*   [Twilio API](https://www.twilio.com/) for sending SMS notifications.

## Setup

To get this project running, follow these steps.

### Prerequisites

*   Python 3.x
*   pip

### Installation

1.  **Environment Variables**

    Create a file named `.env` in the root of the project and add your API keys and credentials. You will need to sign up for the services mentioned above to get them.

    ```
    STOCK_API="YOUR_ALPHA_VANTAGE_API_KEY"
    NEWS_API="YOUR_NEWS_API_KEY"
    TWILIO_ACC_SID="YOUR_TWILIO_ACCOUNT_SID"
    TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
    ```

2.  **Dependencies**

    Install the required Python packages using the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Before running the script, you may want to configure the following variables directly in `main.py`:

*   `STOCK`: The stock symbol to track (e.g., `"TSLA"`).
*   `COMPANY_NAME`: The company name for news searches (e.g., `"Tesla Inc"`).
*   **Twilio Phone Numbers**: Update the `from_` and `to` phone numbers in the `client.messages.create()` function call to your Twilio number and your verified recipient number.

## Usage

To run the script, execute the following command in your terminal from the project's root directory:

```bash
python main.py
import requests
from dotenv import load_dotenv
import os
from datetime import  datetime
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
load_dotenv()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


news_api = os.getenv("NEWS_API")
url= "https://newsapi.org/v2/top-headlines?"
current_date = datetime.now().date()
parameters = {"q" : "elon musk ",
            "country" : "us" ,
            "sortBy": "popularity",
            "from": current_date,
            "to" : current_date,
            "apiKey" : news_api

            }
response = requests.get(url=url , params=parameters )
response.raise_for_status()
data = response.json()
print(data)



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


import requests
from dotenv import load_dotenv
import os
from datetime import  datetime , timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
load_dotenv()

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

today = datetime.now()
yesterday  = today - timedelta(days=1)
yesterday = str(yesterday.date())
yesterday = yesterday + " 19:00:00"
day_before_yesterday = today - timedelta(days=2)
day_before_yesterday = str(day_before_yesterday.date())
day_before_yesterday = day_before_yesterday + " 19:00:00"



stock_api  =  os.getenv("STOCK_API")
stock_url = "https://www.alphavantage.co/query?"
parameters = {"function" : "TIME_SERIES_INTRADAY" ,
              "symbol" : "IBM" ,
              "interval" : "60min",
              "apikey" : stock_api}

response  = requests.get(url = stock_url , params=parameters)
data = response.json()
# print(data)

yesterday_data  = data["Time Series (60min)"][yesterday]
day_before_yesterday_data = data["Time Series (60min)"][day_before_yesterday]

print("day before yesterday points "+day_before_yesterday_data["4. close"])
print("\n\n")
print("yesterday points "+yesterday_data["4. close"])

yesterday_closinig = float(yesterday_data["4. close"])
day_before_yesterday_closing = float(day_before_yesterday_data["4. close"])
difference  = day_before_yesterday_closing - yesterday_closinig
difference =  difference
percentage = (difference / day_before_yesterday_closing) * 100
print(f"difference between points : {difference} which {percentage}%")



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#
# news_api = os.getenv("NEWS_API")
# url= "https://newsapi.org/v2/top-headlines?"
# current_date = datetime.now().date()
# parameters = {"q" : "trump",
#             "country" : "us" ,
#             "sortBy": "relevancy",
#             "from": current_date,
#             "to" : current_date,
#             "apiKey" : news_api,
#             "language" : "en"
#             }
# response = requests.get(url=url , params=parameters )
# # response.raise_for_status()
# data = response.json()
# # print(len(data))
# title = data["articles"][2]["title"]
# description = data["articles"][2]["description"]


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


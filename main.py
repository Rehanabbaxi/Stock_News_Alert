import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Trump Inc "

load_dotenv()
stock_api  =  os.getenv("STOCK_API")
stock_endpoint = "https://www.alphavantage.co/query?"
news_api = os.getenv("NEWS_API")
news_endpoint  = "https://newsapi.org/v2/top-headlines?"
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_sid = os.getenv("TWILIO_ACC_SID")



stock_parameters = {"function" : "TIME_SERIES_DAILY" ,
              "symbol" : STOCK ,
              "apikey" : stock_api,
             }

response  = requests.get(url = stock_endpoint , params=stock_parameters)
data = response.json()
data = data["Time Series (Daily)"]
data = [values for (keys , values) in data.items()]
yesterday_data = data[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"yesterday closing price : {yesterday_closing_price}")
daybefore_yesterday_data = data[1]
daybefore_yesterday_closing_price = daybefore_yesterday_data["4. close"]
print(f"day before yestaerday closing price : {daybefore_yesterday_closing_price}")

difference = float(yesterday_closing_price) - float(daybefore_yesterday_closing_price)
up_down = None
if difference < 0 :
    up_down = "⬆️"
else:
    up_down = "⬇️"

difference_perc = round((difference / float(yesterday_closing_price)) * 100)



if abs(difference_perc) > 2 :
    news_parameters = {"q" : COMPANY_NAME,
                      # "country" : "us" ,
                      # "sortBy": "relevancy",
                      # "from": current_date,
                      # "to" : current_date,
                      "apiKey": news_api,
                      # "language": "en"
                      }
    response = requests.get(url=news_endpoint, params=news_parameters)
    data = response.json()
    articles = data["articles"]
    three_articles = articles[:3]
    # print(three_articles)

    formatted_articles = [f"{STOCK} {difference_perc}% {up_down}\nHeadline: {article['title']} . \nBrief : {article['description']}" for article in three_articles]
    client = Client(twilio_sid , twilio_auth_token)
    for article in formatted_articles:
        message =  client.messages.create(
            body=article,
            from_="+14708767821",
            to="+92 315 5504532",
        )
        print(message.status)



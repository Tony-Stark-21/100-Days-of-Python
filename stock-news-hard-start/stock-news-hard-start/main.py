import os
import requests
# import requests_cache
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import smtplib

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY,
}
STOCK_URL = "https://www.alphavantage.co/query"

news_parameters = {
    "q" : "tesla",
    "apiKey":NEWS_API_KEY,
}
NEWS_URL = "https://newsapi.org/v2/everything?"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price.
stock_response = requests.get(STOCK_URL, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
stock_daily = stock_data["Time Series (Daily)"]
stock_list = list(stock_daily.values())

yesterday_closing = float(stock_list[0]["4. close"])
day_before_closing = float(stock_list[1]["4. close"])

calc = yesterday_closing - day_before_closing
calc = abs(calc)

five_percent = 0.05 * day_before_closing

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
news_response = requests.get(NEWS_URL, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
news_step = news_data["articles"]
news_articles = news_step[:3]

# Assuming 'three_articles' is your sliced list from news_data["articles"][:3]
structured_news_list = []

# This gives you: [{"title": "...", "description": "..."}, {...}, {...}]
print(structured_news_list)

message_block = f"{STOCK} Alert Update:\n"
message_block += "==================================================\n\n"

# 2. Iterate through your custom structured list of dictionaries

if calc >= five_percent :
    for article in news_articles:
        simplified_dict = {
            "source": article["source"]["name"],
            "title": article["title"],
            "description": article["description"],
        }
        structured_news_list.append(simplified_dict)
    for article in structured_news_list:
        message_block += f"Headline: {article['title']}\n"
        message_block += f"Brief: {article['description']}\n"
        message_block += "--------------------------------------------------\n\n"
    # Check direction before formatting the mail string
    up_down_emoji = "🔺" if (yesterday_closing - day_before_closing) > 0 else "🔻"

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=os.environ.get("EMAIL_ADDRESS"), password=os.environ.get("EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.environ.get("EMAIL_ADDRESS"),
            to_addrs=os.environ.get("RECIPIENT_EMAIL"),
            msg=f"{STOCK} {up_down_emoji} Movement Alert!\n\n {message_block}"
        )

# 1. Initialize a string baseline (you can add your stock tracking header here)


# 3. Test printing the output to see the complete unified text chunk


# Optional: Format the SMS message like this:


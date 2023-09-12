import requests
import smtplib

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

MY_EMAIL = "your_email@gmail.com"
TO_EMAIL = "another_email@gmail.com"
PASSWORD = "your_password"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}
response = requests.get(STOCK_ENDPOINT, params = stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "UP "
else:
    up_down = "DOWN "

diff_percent = round((difference / float(yesterday_closing_price)), 2) * 100

if abs(diff_percent) > 0.5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    print(articles)
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}\nURL: {article['url']}\n\n" for article in three_articles]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:{STOCK_NAME} {up_down}{diff_percent}%: {COMPANY_NAME} News Alert\n\n{''.join(formatted_articles)}"
        )


import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("vmvWDivnn4cUFkcqCj6ITOWSD", "HmcIEX0jShzTXojzbktJMFDBKz7TgySyrly0RIg4jWP4Afnqnc")#comnsumer_key, consumer_secret
auth.set_access_token("3430467803-CsdR29ABFMA2MEjVLjudbelUyXvtmLvB3WsEK7w", "TWPzjdKaVJD6ObAvBsqFgCuirpoQTrdsOCGnb8FnB9v6p")#access token, acess_token_sececret

# Create API object


# Create a tweet

api = tweepy.API(auth, wait_on_rate_limit=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

trends_result = api.get_place_trends(1)
print(trends_result)
for trend in trends_result[0]["trends"]:
    print(trend["name"],trend["url"])

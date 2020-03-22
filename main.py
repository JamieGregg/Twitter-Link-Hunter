import tweepy
from keys import returnkeys

consumer_key = returnkeys()[0]
consumer_secret = returnkeys()[1]
access_token = returnkeys()[2]
access_token_secret = returnkeys()[3]

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)

# Creating the API object while passing in auth information
api = tweepy.API(auth)

print("Keyword search: ")
keywordInput = input()

query = keywordInput
language = "en"

resultsPage1 = api.search(query, language, 100, 1)
resultsPage2 = api.search(query, language, 100, 2)
resultsPage3 = api.search(query, language, 100, 3)
results = resultsPage1 + resultsPage2 + resultsPage3

linkStart = 0
linkEnd = 0
tweetData = ""
twitterUser = ""
listOfTweets = []

# Foreach through all tweets pulled
for tweet in results:
    tweetData = tweet.text
    if tweetData.find("https:") == -1:
        continue
    else:
        linkStart = tweetData.find("https:")
        linkEnd = linkStart + 23
        listOfTweets.append("@" + tweet.user.screen_name + ": " + tweetData[linkStart:linkEnd])

# removing the duplicates
res = []
for i in listOfTweets:
    if i not in res and i[0] == "@":
        res.append(i)

print("We found " + str(len(res)) + " unique links on Twitter")

for i in res:
    print(i)




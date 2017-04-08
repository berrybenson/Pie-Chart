from functools import reduce

cals = .038

examplearrayOfTweets = [
    {
        "tweet" : "tweet",
    },
    {
        "tweet" : "tweet2",
    },
    {
        "tweet" : "tweet3",
    }

]

def hashtagCals(hashtag):
    tweetAmt = len(hashtag)
    totalCals = tweetAmt * cals

    return totalCals

def add_cals_to_tweet(tweet):
    calsForTweet = hashtagCals(tweet["tweet"])
    return {
        "calories": calsForTweet,
        "tweet": tweet["tweet"]
    }

def tweetToCals(tweet):
    calsForTweet = hashtagCals(tweet["tweet"])
    return calsForTweet

tweetsWithCalories = map(add_cals_to_tweet, examplearrayOfTweets)
calories = map(tweetToCals, examplearrayOfTweets)
sum = reduce((lambda x, y: x + y), calories)

print(sum)



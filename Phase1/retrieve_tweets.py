
# Author - Tian Tan
import tweepy
import json

# Twitter API credentials
consumer_key = "KOlNFUrSqwL8J12axz87zt7nJ"
consumer_secret = "8O8i504wy6M6pi8OA0LdvqGjJlqp97qPUMSk1NLo2N9CMGfvs1"
access_key = "1441839170465386505-ymY2TI1HIH0RCpaXugCcdoi7cF8yd4"
access_secret = "mp34DPsleTD347EYWrKKTy7dUnoo5WDlz9lSWSsc72Vyc"
# consumer_key = "Yours"
# consumer_secret = "Yours"
# access_key = "Yours"
# access_secret = "Yours"

def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=10)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if (len(alltweets) > 15):
            break
        print
        "...%s tweets downloaded so far" % (len(alltweets))

    # write tweet objects to JSON
    file = open('tweet.json', 'w')
    print
    "Writing tweet objects to JSON please wait..."
    for status in alltweets:
        json.dump(status._json, file, sort_keys=True, indent=4)

    # close the file
    print
    "Done"
    file.close()


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("@Tian_Mayu")
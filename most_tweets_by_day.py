import json

tweets_json = []
with open('data/farmers-protest-tweets-2021-03-5.json', 'r') as json_file:
    for line in json_file:
        tweets_json.append(json.loads(line))


def most_tweets_by_day(tweets):
    days = {}
    for tweet in tweets:
        date = tweet['date'].split('T')[0]
        if date not in days.keys():
            days[date] = 1
        else:
            days[date] += 1
    sorted_days = sorted(days.items(), key=lambda x: x[1], reverse=True)
    return sorted_days[:10]

print(most_tweets_by_day(tweets_json))
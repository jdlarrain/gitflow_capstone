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

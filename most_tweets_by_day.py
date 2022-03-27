def most_tweets_by_day(tweets):
    days = {}
    for tweet in tweets:
        date = tweet['date'].split('T')[0]
        if date not in days.keys():
            days[date] = 1
        else:
            days[date] += 1
    sorted_days = sorted(days.items(), key=lambda x: x[1], reverse=True)
    
    print('10 dias con mas tweets:')
    for day in sorted_days[:10]: 
        print(f'{day[0]} con {day[1]} tweets')

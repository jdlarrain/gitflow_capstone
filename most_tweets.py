def more_tweets(tweets):
    users = {}
    for tweet in tweets:
        if tweet['user']['username'] not in users.keys():
            users[tweet['user'] ['username']] = 1
        else:
            users[tweet['user']['username']] += 1

    sorted_users = sorted(users.items(), key=lambda x: x[1], reverse=True)
    return sorted_users[:10]

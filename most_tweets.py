def more_tweets(tweets):
    users = {}
    for tweet in tweets:
        if tweet['user']['username'] not in users.keys():
            users[tweet['user'] ['username']] = 1
        else:
            users[tweet['user']['username']] += 1

    sorted_users = sorted(users.items(), key=lambda x: x[1], reverse=True)
    
    print('10 usuarios con mas tweets:')
    for user in sorted_users[:10]: 
        print(f'{user[0]} con {user[1]} tweets')

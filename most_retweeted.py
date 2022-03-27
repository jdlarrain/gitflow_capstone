def top_ten_retweeted(tweets):
    top = [['', 0], ['', 0], ['', 0], ['', 0], ['', 0], ['', 0], ['', 0], ['', 0], ['', 0], ['', 0]]    
    for tweet in tweets:
        for index in range(10): 
            if int(tweet['retweetCount']) > top[index][1]:
                top = top[:index] + [[tweet['content'], int(tweet['retweetCount'])]] + top[index:9]
                break

    print('10 tweets mas retwiteados:') 
    for tweet in top:
        print(f'{tweet[0]} con {tweet[1]} retweets')

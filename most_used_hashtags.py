def most_used_hashtags(tweets):
    hashtags = {}
    for tweet in tweets:
        for word in tweet['content'].split(' '):
            if word.startswith('#'):
                if word not in hashtags.keys():
                    hashtags[word] = 1
                else:
                    hashtags[word] += 1


    sorted_hashtags = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
    
    print('10 hashtags mas usados:')
    for hashtag in sorted_hashtags[:10]: 
        print(f'{hashtag[0]} con {hashtag[1]} hashtags')

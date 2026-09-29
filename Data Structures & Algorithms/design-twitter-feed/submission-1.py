class Twitter:

    def __init__(self):
        # keep track of who is following who in a dictionary --> make sure to include user themself
        # need a data structure to store tweet ids along with who posted it - list of tuples?
        self.follow_dict = defaultdict(set)
        self.tweets = []


    def postTweet(self, userId: int, tweetId: int) -> None:
        # add to data structure the user id and tweet id
        self.tweets.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # iterate through this ordered list and check for the first 10 that are made 
        # by people that this user follows
        feed = []
        for i in range(len(self.tweets) - 1, -1, -1):
            if self.tweets[i][0] in self.follow_dict[userId] or self.tweets[i][0] == userId:
                feed.append(self.tweets[i][1])
                if len(feed) >= 10:
                    break
        
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # add followee to the follower's entry in dictionary
        self.follow_dict[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followee from follower's entry in the dictionary
        if followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)
        

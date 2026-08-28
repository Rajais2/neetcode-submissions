class Twitter {
public:
    // Making a struct to better represent a user's tweets
    struct TweetNode {
        int time;       // Global time
        int tweetId;    // The tweet's ID
        int userId;     // The user's ID
        int index;      // The node's index
    };

    // Making a compare struct to sort tweets
    struct Compare {
            bool operator()(const TweetNode& a, const TweetNode& b) {
            // Newer tweets need higher priority 
            // If A is older than B, A goes down
            return a.time < b.time;
        }
    };

    // Using a map to map tweets to their specific users
    unordered_map<int, vector<pair<int, int>>> tweets;

    // Using another map to map followees of users
    unordered_map<int, unordered_set<int>> followMap;

    // Utilizing a global timer for most recent tweets
    int time;

    Twitter() {
        // Intialize the time to zero
        time = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        // Increment the global timestamp as it is shared
        time++;

        // Add that tweet to that specific user
        tweets[userId].push_back({time, tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        // Ensuring the user follows themselves
        followMap[userId].insert(userId);
        
        // Making a priority queue
        priority_queue<TweetNode, vector<TweetNode>, Compare> pq;

        // Looping through each followees of the user
        for (int followee : followMap[userId]) {
            if (tweets[followee].empty()) {
                continue;
            }

            // Extracting all the necessary information for each user's last tweet
            int index = tweets[followee].size() - 1;
            auto [time, tweetId] = tweets[followee][index];

            // Making a new node and adding it onto the priority queue
            TweetNode node = {time, tweetId, followee, index};
            pq.push(node);
        }

        // Creating a vector to hold the final result
        vector<int> result;

        while (result.size() < 10 && !pq.empty()) {
            // Get the top node and remove it
            auto node = pq.top();
            pq.pop();

            // Push that tweet we popped into our final result container
            result.push_back(node.tweetId);

            if (node.index - 1 >= 0) {
                pq.push({tweets[node.userId][node.index - 1].first,
                tweets[node.userId][node.index - 1].second,
                node.userId,
                node.index - 1});
            }
        }

        // Returning the final resulting tweets
        return result;
    }
    
    void follow(int followerId, int followeeId) {
        // Simply insert the new follower at the followee's bucket 
        followMap[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) {
            // Do nothing if the IDs are the same
        } else {
            // Simply remove the account the followee unfollowed from
            followMap[followerId].erase(followeeId);
        }
    }
};

from threading import Thread
import time
import tweepy

from models.Tweet import Tweet


class WorkerThread(Thread):
    def __init__(self, account, api_key, api_key_secret, access_token, access_token_secret):
        self._running = True
        self._account = account
        self._api_key = api_key
        self._api_key_secret = api_key_secret
        self._access_token = access_token
        self._access_token_secret = access_token_secret
        super().__init__()

    # timeout is minute
    def delay(self, timeout: int):
        # convert minutes to seconds
        max = timeout * 60 
        start = time.time()
        while self._running:
            time.sleep(0.1)
            if max + start - time.time() <= 0:
                break

    def stop(self):
        self._running = False

    def run(self):
        auth = tweepy.OAuthHandler(self._api_key, self._api_key_secret)
        auth.set_access_token(self._access_token, self._access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        
        total_tweets = {}
        
        # for i in range(5):
        while self._running:
            new_tweets = {}
            try:
                # assume monitored account tweet at most in 10 minutes
                for tweet in api.user_timeline(id=self._account, count=20):
                    t = Tweet(
                        tweet._json.get('id'),
                        tweet._json.get('created_at'),
                        tweet._json.get('text')
                    )
                    if not total_tweets.get(t.id, None):
                        total_tweets.update({t.id: (t.created_at, t.text)})
                        new_tweets.update({t.id: (t.created_at, t.text)})
            except BaseException as e:
                print(f"Error: failed on_status, str(e)")

            if len(new_tweets.keys()) == 0:
                print("No new tweet in last 10 minutes")
            else:
                for key, value in new_tweets.items():
                    print(f"tweet id is {key}, create time is {value[0]} and text is {value[1]}")
            # delay 10 minutes
            self.delay(10)

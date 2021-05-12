from psaw import PushshiftAPI
import datetime as dt 
import pandas as pd


api = PushshiftAPI()

start_epoch = int(dt.datetime(2020, 1, 1).timestamp())
end_epoch = int(dt.datetime(2020, 12, 31).timestamp())

submissions = list(api.search_submissions(
                            after=start_epoch,
                            before=end_epoch,
                            subreddit='wallstreetbets',
                            q='tsla',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=2000
                            ))

# count = 0
# for submission in submissions:
#     print(submission.title)
#     print(dt.datetime.fromtimestamp(submission.created_utc))
#     print()
#     count = count + 1

# print(count)

print(len(submissions))

df = pd.DataFrame([obj.d_ for obj in submissions])

df = df[['created_utc', 'title', 'subreddit']]

df.to_csv('2020_TSLA_wsb.csv', index=False)

print(df.head())
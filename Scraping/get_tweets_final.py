import twint
import datetime


current_date = datetime.datetime(2020,1,1)
# current_date = datetime.datetime(2020,1,1)
current_end_date = current_date + datetime.timedelta(days=1)
# end_date = datetime.datetime(2020,12,31)
end_date = datetime.datetime(2020,12,31)

while (current_date != end_date):
    c = twint.Config()
    c.Limit = 500
    c.Search = "$SPY"
    c.Min_likes = 2
    c.Count = True
    # c.Lang = 'en'

    c.Store_csv = True
    c.Output = '2020_SPY_tweets.csv'

    c.Since = current_date.strftime("%Y-%m-%d")
    c.Until = current_end_date.strftime("%Y-%m-%d")

    c.Hide_output = True

    twint.run.Search(c)

    current_date = current_end_date
    current_end_date += datetime.timedelta(days=1)
    
    print(current_date)
    print()
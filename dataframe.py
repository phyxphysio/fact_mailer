import pandas as pd
import datetime as dt

# Convert text file into dataframe, then change Date column to datetime type
df = pd.read_csv('SMTP Project/daily_facts.txt', delimiter=': ', header=None)
df.columns = ['Date', 'Fact']
df['Date'] = pd.to_datetime(df['Date'], format='%B %d')

current_day = dt.datetime.now().day
current_month = dt.datetime.now().month

# Fileter dataframe for correct date
filtered_df = df[df['Date'].dt.day == current_day]

if not filtered_df.empty:
    fact_of_the_day = filtered_df['Fact'].values[0]
    print(fact_of_the_day)
else:
    fact_of_the_day = 'No fact found for today'
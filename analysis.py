import pandas as pd
from textblob import TextBlob

df = pd.read_csv("kindle_reviews.csv", encoding="latin1", nrows=1000)

print(df.columns)

df = df[["reviewText"]]

df.dropna(inplace=True)

df["reviewText"] = df["reviewText"].astype(str).str.lower()

def get_sentiment(text):
    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        return "Positive"

    elif analysis.sentiment.polarity < 0:
        return "Negative"

    else:
        return "Neutral"

df["Sentiment"] = df["reviewText"].apply(get_sentiment)

print(df.head())

df.to_csv("Sentiment_Output.csv", index=False)
print("Analysis Completed Successfully")
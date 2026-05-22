# TASK 4 - SENTIMENT ANALYSIS USING VADER

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create analyzer
analyzer = SentimentIntensityAnalyzer()

# User input
text = input("Enter a sentence: ")

# PREPROCESSING
text = text.lower()
text = text.strip()

# Analyze sentiment
score = analyzer.polarity_scores(text)

print("\nSentiment Scores:")
print(score)

# Compound score
compound = score['compound']

# Decide sentiment
if compound >= 0.05:
    print("Sentiment: Positive 😊")

elif compound <= -0.05:
    print("Sentiment: Negative 😠")

else:
    print("Sentiment: Neutral 😐")
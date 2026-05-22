# TASK 4 - SENTIMENT ANALYSIS

# Import TextBlob
from textblob import TextBlob

# Input sentence
text = input("Enter a sentence: ")

# PREPROCESSING
text = text.lower()
text = text.strip()

# Analyze sentiment
analysis = TextBlob(text)

# Get polarity
polarity = analysis.sentiment.polarity

# Print polarity score
print("\nPolarity Score:", polarity)

# Check sentiment
if polarity > 0:
    print("Sentiment: Positive 😊")

elif polarity < 0:
    print("Sentiment: Negative 😠")

else:
    print("Sentiment: Neutral 😐")
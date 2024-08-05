import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import re
from textblob import TextBlob


# Load the input data
input_file = r"C:\Users\Aditya PC\PycharmProjects\URL_Text_Analysis\Input.xlsx"
input_df = pd.read_excel(input_file)

# Display the first few rows of the dataframe to understand its structure
print(input_df.head())


def extract_article_text(url_1, url_id_1):
    response = requests.get(url_1)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming the article text is within <article> tags or similar (adjust according to actual structure)
    title = soup.find('title').get_text()
    article_text = soup.find('article').get_text()

    return title + '\n' + article_text


# Positive, Negative, Polarity, Subjectivity Scores
def sentiment_scores(text):
    blob = TextBlob(text)
    positive_score = sum([word.sentiment.polarity for word in blob.sentences if word.sentiment.polarity > 0])
    negative_score = sum([word.sentiment.polarity for word in blob.sentences if word.sentiment.polarity < 0])
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    return positive_score, negative_score, polarity_score, subjectivity_score


# Additional metrics
def additional_metrics(text):
    sentences = re.split(r'[.!?]', text)
    words = re.findall(r'\w+', text)

    avg_sentence_length = len(words) / len(sentences)
    complex_words = [word for word in words if syllable_count(word) > 2]
    percentage_complex_words = len(complex_words) / len(words) * 100
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_words_per_sentence = len(words) / len(sentences)
    complex_word_count = len(complex_words)
    word_count = len(words)
    syllables_per_word = sum([syllable_count(word) for word in words]) / len(words)
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
    avg_word_length = sum([len(word) for word in words]) / len(words)

    return (avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence,
            complex_word_count, word_count, syllables_per_word, personal_pronouns, avg_word_length)


# Helper function to count syllables in a word
def syllable_count(word):
    word = word.lower()
    vowels = "aeiou"
    count = 0
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count


output_data = []

for index, row in input_df.iterrows():
    url = row['URL']
    url_id = row['URL_ID']
    text = extract_article_text(url, url_id)

    positive_score, negative_score, polarity_score, subjectivity_score = sentiment_scores(text)
    metrics = additional_metrics(text)

    output_row = [row[col] for col in input_df.columns] + [positive_score, negative_score, polarity_score,
                                                           subjectivity_score] + list(metrics)
    output_data.append(output_row)
    print(f"Finished row {index}... \n ...")


output_df = pd.DataFrame(output_data, columns=list(input_df.columns) + [
    'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
    'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX',
    'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT',
    'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH'
])

# Save the results to an Excel file
output_file = r'C:\Users\Aditya PC\PycharmProjects\BlackCoffer_assignment\Output2.xlsx'
output_df.to_excel(output_file, index=False)

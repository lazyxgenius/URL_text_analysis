import pandas as pd
from data_loading import extract_article_text
from data_loading import input_df
from functions import sentiment_scores
from functions import additional_metrics

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
output_file = r'C:\Users\Aditya PC\PycharmProjects\BlackCoffer_assignment\Output.xlsx'
output_df.to_excel(output_file, index=False)

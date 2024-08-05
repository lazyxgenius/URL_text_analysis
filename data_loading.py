import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

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

    # Save the text to a file named by the URL_ID
    # file_name = f'{url_id_1}.txt'
    # with open(file_name, 'w', encoding='utf-8') as file:
    #     file.write(title + '\n' + article_text)

    return title + '\n' + article_text


# Test the function with one URL from the input dataframe
# url = input_df.loc[0, 'URL']
# url_id = input_df.loc[0, 'URL_ID']
# extract_article_text(url, url_id)

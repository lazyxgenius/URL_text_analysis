Instructions

Explanation of Approach

1. Data Extraction:
    - The script reads the URLs from the `Input.xlsx` file.
    - For each URL, it extracts the article title and text using the BeautifulSoup library.
    - The article text is processed directly without saving it to individual text files.

2. Text Analysis:
    - Sentiment scores (positive, negative, polarity, subjectivity) are calculated using the TextBlob library.
    - Additional metrics (average sentence length, percentage of complex words, fog index, average number of words per sentence, complex word count, word count, syllables per word, personal pronouns, average word length) are computed using custom functions.

3. Output Generation:
    - The results for each URL are stored in a DataFrame.
    - The DataFrame is then saved to an Excel file (`Output.xlsx`) in the specified directory.

How to Run the .py File

1. Install Required Libraries:
    
    pip install pandas requests beautifulsoup4 textblob openpyxl
   

2. Ensure File Placement:
    - Place the script (`full_code.py`), `Input.xlsx`, in the same directory.
	(or write the paths carefully in the code while loading dataframe.)

3. Run the Script:
    

4. Output:
    - The output will be saved as `Output.xlsx` in the specified directory.

Dependencies Required

- pandas
- requests
- beautifulsoup4
- textblob
- openpyxl

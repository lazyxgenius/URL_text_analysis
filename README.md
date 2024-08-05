
# Document Extraction and Analysis Project

This project is designed to extract text content from web pages provided in an Excel file and analyze the content using various natural language processing (NLP) techniques. The analysis includes calculating sentiment scores, readability metrics, and other linguistic features. The results are then compiled into an output format for further use.

## Project Overview

This project extracts article text from URLs listed in an Excel file, analyzes the content for sentiment and readability metrics, and outputs the results in a structured format. The project is useful for sentiment analysis, content evaluation, and generating reports based on the analyzed data.

## Features

- Extract text content from web pages using URLs.
- Calculate sentiment scores including positive, negative, polarity, and subjectivity.
- Analyze readability metrics like average sentence length, complex word percentage, Gunning Fog Index, and more.
- Identify linguistic features such as personal pronoun usage and syllable count.


## Usage

1. **Prepare Input Data:**
   - Place the Excel file containing the URLs and associated data in the project's directory. Ensure the Excel file has columns for `URL` and `URL_ID`.
   - Modify the `input_file` path in the script to point to your Excel file.

2. **Run the Script:**
   - Execute the Python script to start the extraction and analysis process.
   ```bash
   python full_code.py
   ```

3. **View Output:**
   - The script will process each URL, extract the text, perform analysis, and store the results in an output file or print them to the console.

## Output

The output data will include:
- **Sentiment Scores:**
  - Positive Score
  - Negative Score
  - Polarity Score
  - Subjectivity Score
- **Readability Metrics:**
  - Average Sentence Length
  - Percentage of Complex Words
  - Gunning Fog Index
  - Average Words per Sentence
  - Complex Word Count
  - Total Word Count
  - Syllables per Word
  - Personal Pronouns Count
  - Average Word Length

The processed data can be exported to an Excel file or displayed in the console, depending on your configuration.

## Dependencies

The following Python libraries are required to run this project:
- `pandas`
- `requests`
- `beautifulsoup4`
- `textblob`

You can install these dependencies using:
```bash
pip install pandas requests beautifulsoup4 textblob
```

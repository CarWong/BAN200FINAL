# A Sentiment Analysis of Canadian Mobile Banking Apps: Trends, Pain Points, and Switching Signals

## Overview

This is the final project to be submitted for the Business Analytics course (BAN 200) at Seneca Polytechnic. It analyzes customer reviews and sentiment for major Canadian banking mobile applications from the Google Play Store. The analysis focuses on understanding user satisfaction, identifying common issues, and detecting customer switching intentions across five major Canadian banks: CIBC, RBC, TD, Scotiabank, and BMO.

## Project Structure

```
BAN200FINAL/
├── data/
│   ├── reviews/           # Individual bank review JSON files
│   ├── banking_apps_details.json
│   └── all_reviews.csv    # Consolidated review dataset
├── plots/                 # Generated visualization files
│   ├── sentiment_rating_analysis.png
│   ├── switching_keywords_chart.png
│   └── bank_mention_heatmap.png
├── get_app_reviews.py     # Data collection script
├── FINALBAN200.ipynb     # Main analysis notebook
└── README.md
```

## Banks Analyzed

1. **BMO** (`com.bmo.mobile`)
2. **CIBC** (`com.cibc.android.mobi`)
3. **RBC** (`com.rbc.mobile.android`)
4. **Scotiabank** (`com.scotiabank.banking`)
5. **TD** (`com.td`)

## Features

### Data Collection
- **Automated Review Scraping**: Uses `google_play_scraper` to collect reviews from Google Play Store
- **Multi-Bank Coverage**: Analyzes reviews from 5 major Canadian banks
- **Structured Data**: Organizes reviews with metadata including ratings, dates, and user information

### Analysis Capabilities
- **Sentiment Analysis**: Uses TextBlob for sentiment scoring of review text
- **NLP Processing**: Implements text preprocessing including:
  - Tokenization and lemmatization
  - Stop word removal
  - Emoji and contraction handling
  - Text cleaning and normalization
- **Switching Intention Detection**: Identifies customers likely to switch banks based on review content
- **Topic Modeling**: Uses LDA (Latent Dirichlet Allocation) for topic discovery
- **Keyword Analysis**: Extracts and analyzes switching-related keywords

### Visualizations
- **Sentiment vs Rating Analysis**: Correlation between sentiment scores and star ratings
- **Switching Keywords Chart**: Most common keywords indicating switching intention
- **Bank Mention Heatmap**: Cross-bank mention patterns

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip

### Dependencies
```bash
pip install pandas numpy nltk textblob matplotlib scikit-learn google-play-scraper beautifulsoup4 contractions emoji
```

### NLTK Data Download
The notebook automatically downloads required NLTK data:
- punkt (tokenizer)
- stopwords
- wordnet (lemmatizer)

## Usage

### Data Collection
```bash
python get_app_reviews.py
```

This script will:
- Scrape reviews for all 5 banking apps
- Save individual JSON files in `data/reviews/`
- Generate app details in `data/banking_apps_details.json`

### Analysis
Open `FINALBAN200.ipynb` in Jupyter Notebook to run the complete analysis pipeline:

1. **Data Loading & Preprocessing**
   - Loads individual bank review files
   - Combines into consolidated dataset
   - Cleans and preprocesses text data

2. **NLP Analysis**
   - Text preprocessing and normalization
   - Sentiment analysis
   - Keyword extraction

3. **Switching Analysis**
   - Identifies high-intention switching samples
   - Analyzes switching keywords
   - Generates switching patterns

4. **Visualization**
   - Creates sentiment analysis plots
   - Generates switching keyword charts
   - Produces bank mention heatmaps

## Technical Details

### Libraries Used
- **Data Processing**: pandas, numpy
- **NLP**: nltk, textblob, beautifulsoup4
- **Text Processing**: contractions, emoji
- **Machine Learning**: scikit-learn
- **Visualization**: matplotlib
- **Data Collection**: google-play-scraper

### Analysis Methods
- **Sentiment Analysis**: TextBlob polarity scoring
- **Topic Modeling**: LDA (Latent Dirichlet Allocation)
- **Text Preprocessing**: Tokenization, lemmatization, stop word removal
- **Keyword Extraction**: TF-IDF vectorization

## Contributing

This is a final project for BAN200. For academic or research purposes, please ensure proper attribution and follow ethical guidelines for data collection and analysis.

For questions about this analysis, please refer to the course instructor (Roya Barzegar) or one of the following students:
 - Taher Ghaleb
 - Carolyn Wong
 - Farid Gasimov
 - Ogechi Ozigbu
 - Subhankar Gon

## License

This project is for educational and research purposes. Please respect the terms of service of the Google Play Store and ensure responsible data usage.



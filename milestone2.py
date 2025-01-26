# -*- coding: utf-8 -*-
"""Milestone2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z6gArT2P0wrhIxePzjqwua9rc2D6CjkL

# Product : TOMATO

### Try to fetch information about tomatos supply chain management using news api
"""

import requests
import pandas as pd

API_KEY = "f77ec218c74644348641d36d500f126a"
API_URL = "https://newsapi.org/v2/everything"

# Function to fetch news
def news_fetch(query="tomato supply chain", page_size=50, language="en"):
    parameters = {
        "q": query,
        "pageSize": page_size,  # Number of articles per request
        "language": language,
        "apiKey": API_KEY,
    }
    response = requests.get(API_URL, params=parameters) #Sends a GET request to the NewsAPI with the specified parameters
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        print(f"Error: {response.status_code}")
        return []

# Main function
if __name__ == "__main__":
    # Fetch news articles
    articles = news_fetch()
    if articles:
        print("SUCCESSFUL !\n")

        # Collect relevant fields and create a DataFrame
        news_data = [
            {
                "Title": article["title"],
                "Description": article["description"],
                "Source": article["source"]["name"],
                "URL": article["url"],
            }
            for article in articles
        ]
        news_df = pd.DataFrame(news_data)

        news_df.to_csv("Tomato_supply_chain_news.csv", index=True) # Save to CSV

        # Print in the requested format (Row {idx + 1}: Title, Description, Source, URL)
        print("\nArticle Information:")
        for idx, row in news_df.iterrows():
            print(f"Row {idx + 1}:")
            print(f"Title: {row['Title']}")
            print(f"Description: {row['Description']}")
            print(f"Source: {row['Source']}")
            print(f"URL: {row['URL']}")
            print("\n")
    else:
        print("No articles found.")

"""### Try to fetch information about tomatos supply chain management using kaggle api"""

import requests
import pandas as pd

# Constants
API_URL = "https://www.kaggle.com/api/v1/datasets/download/bonifacechosen/tomato-retail-sales-data-2009-2022"
API_KEY = "485aba36b259a5295d30f07a0d031a8f"

def fetch_data_from_api():
    """Fetch data from the API."""
    headers = {
        "Authorization": f"Bearer {API_KEY}"  # Adjust headers as required by your API
    }

    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()  # Parse JSON response
            return data
        except requests.exceptions.JSONDecodeError:
            print("Response is not in JSON format.")
            return []
    else:
        print(f"API call failed with status code {response.status_code}: {response.text}")
        return []

def save_data_to_csv(data, filename="output.csv"):
    """Save the fetched data to a CSV file."""
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

if __name__ == "__main__":
    # Fetch data from the API
    api_data = fetch_data_from_api()

    # Save data to a CSV file
    save_data_to_csv(api_data, filename="api_data.csv")

print(response.headers.get("Content-Type"))

import requests
import zipfile
import os
import pandas as pd

# API endpoint
API_URL = "https://www.kaggle.com/api/v1/datasets/download/bonifacechosen/tomato-retail-sales-data-2009-2022"

# File paths
ZIP_FILE_PATH = "data.zip"
EXTRACTION_FOLDER = "extracted_files"

# Function to download and extract ZIP file
def download_and_extract_zip(api_url, zip_file_path, extraction_folder):
    response = requests.get(api_url)

    if response.status_code == 200:
        # Save ZIP file locally
        with open(zip_file_path, "wb") as file:
            file.write(response.content)
        print("ZIP file downloaded successfully.")

        # Extract ZIP file
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            if not os.path.exists(extraction_folder):
                os.makedirs(extraction_folder)
            zip_ref.extractall(extraction_folder)
        print(f"Files extracted to {extraction_folder}")
        return True
    else:
        print(f"API call failed with status code {response.status_code}: {response.text}")
        return False

# Function to convert extracted CSV files to pandas DataFrames
def process_csv_files(extraction_folder):
    for root, dirs, files in os.walk(extraction_folder):
        for filename in files:
            if filename.endswith(".csv"):
                file_path = os.path.join(root, filename)
                print(f"Processing file: {file_path}")

                # Load CSV into a DataFrame
                df = pd.read_csv(file_path)

                # Save DataFrame to a new CSV file (optional)
                new_csv_path = f"processed_{filename}"
                df.to_csv(new_csv_path, index=False)
                print(f"Processed CSV saved as: {new_csv_path}")

# Main execution
if __name__ == "__main__":
    if download_and_extract_zip(API_URL, ZIP_FILE_PATH, EXTRACTION_FOLDER):
        process_csv_files(EXTRACTION_FOLDER)

import pandas as pd
data=pd.read_csv("/content/extracted_files/tomato_retail_sales_daily_2009_2022 (1).csv")
data

# @title Store Location

from matplotlib import pyplot as plt
import seaborn as sns
data.groupby('Store Location').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

"""## Final Dataset"""

import pandas as pd
data = pd.read_csv("/content/tomato_supply_chain (1).csv")
data

"""# Sentiment and Risk Analysis

### model: facebook/bart-large-mnli
"""

import pandas as pd
from openai import ChatCompletion
from transformers import pipeline

OPENAI_API_KEY = "AIzaSyDCQ1-AUH3C6xU5GGAHxY9QvL_kRZ-OHUY"

# LLM Initialization
def initialize_openai():
    ChatCompletion.api_key = OPENAI_API_KEY

def initialize_llama():
    return pipeline("text-classification", model="facebook/bart-large-mnli")

# risk analysis with OpenAI GPT
def analyze_risk_with_gpt(content):
    try:
        response = ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in supply chain risk analysis."},
                {"role": "user", "content": content}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error with OpenAI GPT: {e}")
        return None

# sentiment analysis with LLaMA
def analyze_sentiment_with_llama(content, llama_pipeline):
    try:
        results = llama_pipeline(content)
        return results
    except Exception as e:
        print(f"Error with LLaMA: {e}")
        return None

# Aggregating data from the dataset
def aggregate_data_from_csv(file_path):
    try:
        # Load dataset
        dataset = pd.read_csv(file_path)
        return dataset
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Main pipeline
def main():
    # Initialize models
    initialize_openai()
    llama_pipeline = initialize_llama()

    # Load dataset
    dataset_path = "/content/tomato_supply_chain (1).csv"
    structured_data = aggregate_data_from_csv(dataset_path)
    if structured_data is None:
        return

    # Analyze risk and sentiment for each row
    results = []
    for _, row in structured_data.iterrows():
        print(f"Analyzing data for Date: {row['Date']}, Region: {row['Region']}, Supplier: {row['Supplier']}")

        # Combine relevant fields for analysis
        content = (f"Region: {row['Region']}, Country: {row['Country']}, Supplier: {row['Supplier']}, "
                   f"Inventory Level: {row['Inventory Level']}, Lead Time: {row['Lead Time (days)']}, "
                   f"Transport Status: {row['Transport Status']}, News Sentiment: {row['News Sentiment']}, "
                   f"Risk Factor: {row['Risk Factor']}")

        gpt_analysis = analyze_risk_with_gpt(content)
        sentiment_analysis = analyze_sentiment_with_llama(content, llama_pipeline)

        results.append({
            "Date": row['Date'],
            "Region": row['Region'],
            "Country": row['Country'],
            "Supplier": row['Supplier'],
            "GPT Risk Analysis": gpt_analysis,
            "Sentiment Analysis": sentiment_analysis
        })

    # Convert results to a DataFrame and save
    results_df = pd.DataFrame(results)
    results_df.to_csv("supply_chain_analysis_results.csv", index=False)
    print("Analysis complete. Results saved to 'supply_chain_analysis_results.csv'.")

if __name__ == "__main__":
    main()

res_data=pd.read_csv("/content/supply_chain_analysis_results.csv")
res_data

# @title Region vs Country

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['Country'].value_counts()
    for x_label, grp in res_data.groupby('Region')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('Region')
_ = plt.ylabel('Country')

"""## Risk Alalysis 1
using basic functions based on the value and information given in other columns
"""

import pandas as pd

# Load dataset
def load_dataset(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Analyze risk based on dataset columns
def calculate_risk(row):

    risk_score = 0

    # Low inventory increases risk
    if row['Inventory Level'] < 100:
        risk_score += 30

    # Long lead time increases risk
    if row['Lead Time (days)'] > 7:
        risk_score += 20

    # Transport status
    if row['Transport Status'] == "Delayed":
        risk_score += 40

    # Negative news sentiment increases risk
    if row['News Sentiment'] == "Negative":
        risk_score += 10

    # Return final risk factor capped at 100
    return min(risk_score, 100)


def main():
    dataset_path = "/content/tomato_supply_chain (1).csv"

    # Load the dataset
    data = load_dataset(dataset_path)
    if data is None:
        return

    # Add risk factor column
    data['Risk Factor'] = data.apply(calculate_risk, axis=1)

    # Display results
    print("Dataset with Risk Analysis:")
    print(data.head(10))

    # Save the updated dataset
    output_path = "tomato_supply_chain_with_risk.csv"
    data.to_csv(output_path, index=False)
    print(f"Updated dataset saved to {output_path}")

if __name__ == "__main__":
    main()

risk_data=pd.read_csv("/content/tomato_supply_chain_with_risk.csv")
risk_data

"""## Risk Alalysis main

### model: "facebook/bart-large-mnli"
"""

import pandas as pd
from transformers import pipeline

# Initialize the LLM model for text analysis
def initialize_llm():
    return pipeline("text-classification", model="facebook/bart-large-mnli")

# Perform risk analysis
def analyze_risk(content, llm_pipeline):
    try:
        # Analyze sentiment or risk categorization
        result = llm_pipeline(content)
        # Extract the most probable label
        risk_label = result[0]['label']
        confidence = result[0]['score']
        return risk_label, confidence
    except Exception as e:
        print(f"Error analyzing risk: {e}")
        return "Error", 0.0

# Main pipeline
def main():
    input_csv = "/content/tomato_supply_chain (1).csv"
    df = pd.read_csv(input_csv)

    llm_pipeline = initialize_llm() # Initialize LLM pipeline

    # Add new columns for risk analysis
    df["Risk Analysis"] = ""
    df["Risk Confidence"] = 0.0

    # Perform risk analysis on the "News Sentiment" column
    for index, row in df.iterrows():
        news_sentiment = row.get("News Sentiment", "No sentiment provided")
        risk_label, confidence = analyze_risk(news_sentiment, llm_pipeline)

        # Save the results into the dataframe
        df.at[index, "Risk Analysis"] = risk_label
        df.at[index, "Risk Confidence"] = confidence

        print(f"Row {index + 1}/{len(df)} analyzed. Risk: {risk_label}, Confidence: {confidence:.2f}")

    # Save the updated dataset
    output_csv = "tomato_supply_chain_with_risk_main.csv"
    df.to_csv(output_csv, index=False)
    print(f"Updated dataset with risk analysis saved to: {output_csv}")

if __name__ == "__main__":
    main()

risk_data_main = pd.read_csv("/content/tomato_supply_chain_with_risk_main.csv")
risk_data_main

# @title Lead Time (days) vs Risk Confidence

from matplotlib import pyplot as plt
risk_data_main.plot(kind='scatter', x='Lead Time (days)', y='Risk Confidence', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

"""## Use model: cardiffnlp/twitter-roberta-base-sentiment & yiyanghkust/finbert-tone"""

import pandas as pd
from transformers import pipeline

# Initialize sentiment and risk models
def initialize_sentiment_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def initialize_risk_model():
    return pipeline("text-classification", model="yiyanghkust/finbert-tone")

# Analyze sentiment and risk
def analyze_sentiment_and_risk(content, sentiment_pipeline, risk_pipeline):
    try:
        # Sentiment analysis
        sentiment_results = sentiment_pipeline(content)
        sentiment_label = sentiment_results[0]['label']
        sentiment_score = sentiment_results[0]['score']

        # Risk analysis
        risk_results = risk_pipeline(content)
        risk_label = risk_results[0]['label']

        return sentiment_label, sentiment_score, risk_label
    except Exception as e:
        print(f"Error analyzing sentiment and risk: {e}")
        return "Error", 0.0, "UNKNOWN"

# Process CSV file and analyze sentiment and risk
def process_csv(file_path, sentiment_pipeline, risk_pipeline):
    try:
        data = pd.read_csv(file_path)

        # Add new columns for sentiment and risk analysis
        data['Sentiment'] = ""
        data['Sentiment Score'] = 0.0
        data['Risk'] = ""

        for index, row in data.iterrows():
            content = f"Supply chain update: {row['Region']}, {row['Country']}, Supplier: {row['Supplier']}, Inventory Level: {row['Inventory Level']}, Lead Time: {row['Lead Time (days)']} days, Transport Status: {row['Transport Status']}, News Sentiment: {row['News Sentiment']}, Risk Factor: {row['Risk Factor']}"
            sentiment_label, sentiment_score, risk_label = analyze_sentiment_and_risk(
                content, sentiment_pipeline, risk_pipeline
            )
            data.at[index, 'Sentiment'] = sentiment_label
            data.at[index, 'Sentiment Score'] = sentiment_score
            data.at[index, 'Risk'] = risk_label

        return data
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        return None

# Main pipeline
def main():
    # Initialize models
    sentiment_pipeline = initialize_sentiment_model()
    risk_pipeline = initialize_risk_model()

    # Input CSV file path (from the dataset generated earlier)
    input_csv = "/content/tomato_supply_chain (1).csv"

    # Process the CSV file
    processed_data = process_csv(input_csv, sentiment_pipeline, risk_pipeline)
    if processed_data is not None:
        # Save the processed data to a new CSV file
        output_csv = "tomato_supply_chain_analysis_1.csv"
        processed_data.to_csv(output_csv, index=False)
        print(f"Processed data saved to: {output_csv}")
    else:
        print("Failed to process CSV data.")

if __name__ == "__main__":
    main()

res_data_1 = pd.read_csv("/content/tomato_supply_chain_analysis_1.csv")
res_data_1

import pandas as pd
from transformers import pipeline

# Initialize sentiment and risk models
def initialize_sentiment_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def initialize_risk_model():
    return pipeline("text-classification", model="yiyanghkust/finbert-tone")

# Analyze sentiment using FinBERT
def analyze_sentiment_with_finbert(content, sentiment_pipeline):
    try:
        results = sentiment_pipeline(content)
        sentiment_label = results[0]['label']
        sentiment_score = results[0]['score']
        return sentiment_label, sentiment_score
    except Exception as e:
        print(f"Error with FinBERT Sentiment Analysis: {e}")
        return None, None

# Analyze risk using FinBERT
def analyze_risk_with_finbert(content, risk_pipeline):
    try:
        results = risk_pipeline(content)
        risk_label = results[0]['label']
        risk_score = results[0]['score']
        return risk_label, risk_score
    except Exception as e:
        print(f"Error with FinBERT Risk Analysis: {e}")
        return None, None

# Process CSV file and analyze sentiment and risk
def process_csv(file_path, sentiment_pipeline, risk_pipeline):
    try:
        # Load data
        data = pd.read_csv(file_path)

        # Add new columns for sentiment and risk analysis
        data['Sentiment'] = ""
        data['Sentiment Score'] = 0.0
        data['Risk'] = ""
        data['Risk Score'] = 0.0

        for index, row in data.iterrows():
            content = f"Supply chain update: {row['Region']}, {row['Country']}, Supplier: {row['Supplier']}, Inventory Level: {row['Inventory Level']}, Lead Time: {row['Lead Time (days)']} days, Transport Status: {row['Transport Status']}, News Sentiment: {row['News Sentiment']}, Risk Factor: {row['Risk Factor']}"

            # Analyze sentiment
            sentiment_label, sentiment_score = analyze_sentiment_with_finbert(content, sentiment_pipeline)
            # Analyze risk
            risk_label, risk_score = analyze_risk_with_finbert(content, risk_pipeline)

            # Update DataFrame
            data.at[index, 'Sentiment'] = sentiment_label
            data.at[index, 'Sentiment Score'] = sentiment_score
            data.at[index, 'Risk'] = risk_label
            data.at[index, 'Risk Score'] = risk_score

        return data
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        return None

# Main pipeline
def main():
    # Initialize models
    sentiment_pipeline = initialize_sentiment_model()
    risk_pipeline = initialize_risk_model()

    input_csv = "/content/tomato_supply_chain (1).csv"

    # Process the CSV file
    processed_data = process_csv(input_csv, sentiment_pipeline, risk_pipeline)
    if processed_data is not None:
        # Save the processed data to a new CSV file
        output_csv = "tomato_supply_chain_analysis_2.csv"
        processed_data.to_csv(output_csv, index=False)
        print(f"Processed data saved to: {output_csv}")
    else:
        print("Failed to process CSV data.")

if __name__ == "__main__":
    main()

res_data_2 = pd.read_csv("/content/tomato_supply_chain_analysis_2.csv")
res_data_2

# @title Risk Score

from matplotlib import pyplot as plt
res_data_2['Risk Score'].plot(kind='hist', bins=20, title='Risk Score')
plt.gca().spines[['top', 'right',]].set_visible(False)

"""### Sentiment Score Distribution"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette("muted")

# Define a colormap for the histogram
colormap = plt.cm.viridis

# Plot histogram
plt.figure(figsize=(8, 6))
n, bins, patches = plt.hist(res_data_2['Sentiment Score'], bins=20, edgecolor='black', alpha=0.8)

# Apply colors to the bars
for i in range(len(patches)):
    patches[i].set_facecolor(colormap(i / len(patches)))

plt.title("Sentiment Score Distribution", fontsize=16)
plt.xlabel("Sentiment Score", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

plt.gca().spines[['top', 'right']].set_visible(False)

# Show plot
plt.tight_layout()
plt.show()

# @title Sentiment Score vs Risk Score

from matplotlib import pyplot as plt
res_data_2.plot(kind='scatter', x='Sentiment Score', y='Risk Score', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

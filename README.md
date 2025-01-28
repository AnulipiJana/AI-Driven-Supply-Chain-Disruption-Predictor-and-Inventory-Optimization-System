# **AI-Driven Supply Chain Disruption Predictor and Inventory Optimization System**
This repository contains the code for an AI-Driven Supply Chain Disruption Predictor and Inventory Optimization System aims to provide businesses with a solution for predicting supply chain disruptions and optimizing inventory in real-time. The system leverages FastAPIs, advanced machine learning algorithms and real-time data integration to proactively identify and manage disruptions in global supply chains. Forecasts potential disruptions, and suggests dynamic inventory adjustments based on predictive models. 
## Key features
1. Monitor Global Supply Chain Data: The system will keep track of global news, supplier information, and transportation updates, using APIs (NewsApi, GoMaps, WeatherApi etc.)
2. Predict Potential Disruptions: The LLM Models (Bert, T5, MetaLLM) will identify and analysis possible risks and sentiment that could affect the supply chain.
3. Optimize Inventory Levels: Based on the predicted risks, the system will suggest adjustments to inventory levels to avoid shortages or excess stock. It will forecast these disruptions before they happen.
4. Send Real-Time Alerts: Businesses will get instant notifications (via tools like Slack or email) about potential disruptions and what actions to take. This includes recommendations to reorder products or adjust inventory.

# Milestone 1
## Setup & Data Collection
### Tasks
1. Project Infrastructure Setup. Set up tools and libraries for development (e.g.Google Colab, Python, NLP libraries, data analysis tools).
2. Generate and Integrate APIs for data collection.
3. Data Collection. Identify and shortlist reliable data sources (e.g., global news APIs, supplier databases, and transportation reports).
Extract data such as news articles, supplier updates, import export dates, and market trends.
4. Configure project repository and folder structure in GitHub.
5. Install and configure LLMs like bert distilbert, t5 model and Meta LLaMA for trainig using collected data.
### Problems & Solutions
1. During local setup of Tensorflow, Pytorch mismatch the versions of various libraries. --> Choose **Googl collab** platform. Most of the librarious are pre-install with suitable libraries.
2. Finding suitable resources. Search free or publec **APIs key and Base url** and mainly distinguished them as per requirements --> **Newsapi, Kaggle , GoMaps**
![image](https://github.com/user-attachments/assets/1e1784ae-95ed-4f2d-89da-c92fea1fa487)

# Milestone 2
## Risk & Sentiment Analysis
### Tasks
1. Choose a specific product for start to end analysis. **Product --> Tomato**
2. Collect information about the product using APIs
3. Store all collected and processed data in a structured format (e.g., CSV files or databases) and maintain uniformity. [Sample dataset consist of columns: Date, Region, Country, Supplier, Item, Inventory Level, Lead Time (days), Transport Status, News Sentiment, Risk Factors]
4. Feed informations to the LLM (OpenAI GPT-4 or open-source LLaMA). Train the model.
5. Extract:Sentiment (positive/negative/neutral) & Risk Analysis
### Problems & Solutions
1. Faced challenges to collect proper data. --> explore newapi, kaggle, Govt. agriculture Dept. , chatgpt
![image](https://github.com/user-attachments/assets/a13250e0-2588-417b-a4c5-4a38ea52d9e8)
use NewsAPIs fetch only 9 rows.
2. Try to fetch data from Kaggle faces issued in formate of dataset
![image](https://github.com/user-attachments/assets/c384762d-ae1f-4a2d-8da4-28f406b0fab0)
3. Lack of specific columns in dataset collected from kaggle.
4. Modified all fetched information and generate sample dataset using chatgpt
5. Free models for sentiment and Risk analysis : ** facebook/bart-large-mnli, cardiffnlp/twitter-roberta-base-sentiment , yiyanghkust/finbert-tone**

# Milestone 3
## Generate Alert based on Risk & Sentiment Analysis And Trained the model
### Tasks
1. Analysis Risk Score and Sentiment Score generated by NLP model in Milestone 2.
2. Set Thresholds and conditions, Calculate Warehouse capacity.
4. Use historical data to forecast future actions [SELL, BUY, MONITOR]
5. Based on the future action train model for future prediction in new data.
### Problems & Solutions
1. Unable to Fetch free API for ERP system : Try to clone github Repository, where I get pre-build ERP system.
2. There are some library (Tkinter) for display in cloning Github Repository is not supported by Google Collab : install virtual display
![image](https://github.com/user-attachments/assets/b5e8d6d9-4ef1-4176-b1ea-ea9c6ebb069a)
3. Without API and Libraries like (Tkinter) Simple code is in ** INFOSYS_MAIN **: Predict suitable Action for future.
![image](https://github.com/user-attachments/assets/87a3da2e-d37b-4bf1-b61a-886a84d10f62)
![image](https://github.com/user-attachments/assets/516179b2-48f7-483c-913e-0040fe4e5547)
# Milestone 4
## Real-Time Alert & Reporting Dashboard Deployment
### Tasks
1. Deploy a dashboard that provides visualizations of supply chain risks, disruptions, and inventory status using data visualization libraries like ‘matplotlib’ or ‘seaborn’ etc.
2. Integrate the system with Slack or Email to notify teams about critical disruptions or required stock adjustments in real time.
### Problems & Solutions
1. Find difficulty in finding slack webhook URL
2. Find difficulty in email and app specific password and security.
![image](https://github.com/user-attachments/assets/b221ad8b-8310-49a1-8a2f-f986043aebd8)
![image](https://github.com/user-attachments/assets/f39469ee-1901-421d-87d7-963263420280)

![image](https://github.com/user-attachments/assets/3cbaded7-3807-4260-ba29-2b4a5b9cc685)




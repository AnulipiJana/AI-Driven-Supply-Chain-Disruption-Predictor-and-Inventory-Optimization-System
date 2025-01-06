## **Goals**

### Accurate Predictions: 
The system will analyze trends from multiple data sources to predict supply chain issues.
### Better Inventory Management: 
Dynamic adjustments to stock levels will reduce waste and prevent stockouts.
### Real-Time Notifications: 
Businesses will get quick updates about risks and solutions to act immediately.
### Improved Efficiency:
Proactive management will save money and keep operations running without interruptions.

## **Specifications**

1. Monitor Global Supply Chain Data: The system will keep track of global news, supplier information, and transportation updates. It will use advanced AI tools (like OpenAI GPT and Meta LLaMA) to understand this data.

2. Predict Potential Disruptions: The AI will identify possible risks (e.g., natural disasters, strikes, or political instability) that could affect the supply chain. It will forecast these disruptions before they happen.

3. Optimize Inventory Levels: Based on the predicted risks, the system will suggest adjustments to inventory levels to avoid shortages or excess stock. It will automatically calculate the best stock levels to keep operations running smoothly.

4. Send Real-Time Alerts: Businesses will get instant notifications (via tools like Slack or email) about potential disruptions and what actions to take. This includes recommendations to reorder products or adjust inventory.

# **Milestones**
## Milestone 1
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

## Milestone 2
### Tasks
1. Choose a specific product for start to end analysis.
2. Collect information about the product using APIs
3. Store all collected and processed data in a structured format (e.g., CSV files or databases) and maintain uniformity. [Sample dataset consist of columns: Date, Region, Country, Supplier, Item, Inventory Level, Lead Time (days), Transport Status, News Sentiment, Risk Factors]
4. Feed informations to the LLM (OpenAI GPT-4 or open-source LLaMA). Train the model.
5. Extract:Sentiment (positive/negative/neutral)
6. Risk Analysis
### Problems & Solutions

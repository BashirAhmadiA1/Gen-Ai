Created a chat bot using openapi that answers queries from the given CSV file and general questions.

Install required imports:
pip install openai
pip install pandas
pip install langchain
pip install -q langchain openai chromadb


To run programme:
python genAi.py


IMPORTANT!!!
    - If you are asking a question from the data file you must mention 'csv' in your question. e.g. 'How many columns are there in the csv file'


Example: 
You: hey how are you?

Bot: I'm doing well, thank you for asking! How about yourself?

You: give me a list of the columns in the csv file

Bot: Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome, Dt_Customer, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Z_CostContact, Z_Revenue, Response

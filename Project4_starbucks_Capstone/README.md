# Starbucks Capstone Project
## Data Scientist Nanodegree

# 1.Library used in this project:
    -pandas
    -numpy
    -math
    -json
    -datetime
    -seaborn
    -sklearn
    -matplotlib

# 2.Project overview:
Starbucks frequently provides offers to its customers through its rewards mobile app to drive more sales. These offers can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). This project focuses on tailoring the promotional offers for customers based on their responses to the previous offers and predict the response of a customer to an offer, meaning whether or not the customer would either complete an discount or bogo offer or the customer would have a transaction after viewing an informational offer. The most challenging part is cleaning of the dataset. Some users might not receive any offers during certain weeks. Some users might receive an offer, either not review it, or review it but choose to ignore it. Other users can also receive an offer, never actually view the offer, and still complete the offer. There will be an offer completion record in the data set; however, the customer was not influenced by the offer because the customer never viewed the offer. So it is crucial to distinguish the offers received followed by a transaction influenced by the offer. This is the challenging part in this project.

- #### First, combining transaction, demographic and offer data.
- #### Second, Label the received offers with completed for discount or bogo offers and effective for informational offers.
        For discount or bogo offers, the offer journey could be:
                  1) offer received-transaction-offer completed
                  2) offer received-offer reviewed-transaction
                  3) offer received-offer reviewed
                  4) offer received-transaction
                  5) offer received
                  6) offer received-offer reviewed-transaction-offer completed
        Only the scenario 6 could be labelled as completed offer for the offers of discount or bogo.

        For informational offers, the offer journey could be:
                  1) offer received-transaction
                  2) offer received-offer reviewed-transaction after valid time
                  3) offer received-offer reviewed
                  4) offer received
                  5) offer received-offer reviewed-transaction within valid time
         Only the scenario 6 could be labelled as effective offer for the informational offers.

 - #### Third, to determine which demographic groups respond best to which offer type. Exploratory Data Analysis(EDA) is performed to find the customer group.

 - #### Last, two machine learning models (one for discount and bogo offers, the other one for informational offers) are built to predict the customer’s response to an offer so that Starbucks can properly target who they send their offers to.
 Here I chose F1-score as evaluation metrics. As we could see from data exploratory analysis, the final dataset for bogo or discount offers are imbalanced. Only about 25% of the received offers are effective. F1 score sort of maintains a balance between the precision and recall for the classifier. 


# 3.Datasets and Inputs:
For this project, the data sets are provided by Starbucks and Udacity in the form of three JSON files. These contains simulated data that mimics customer behavior on the Starbucks rewards mobile app.

   -portfolio.json - containing offer ids and meta data about each offer (duration, type, etc.)
   -profile.json - demographic data for each customer
   -transcript.json - records for transactions, offers received, offers viewed, and offers completed
Here is the schema and explanation of each variable in the files:

#### portfolio.json

- id (string) - offer id
- offer_type (string) - type of offer ie BOGO, discount, informational
- difficulty (int) - minimum required spend to complete an offer
- reward (int) - reward given for completing an offer
- duration (int) - time for offer to be open, in days
- channels (list of strings)

#### profile.json

- age (int) - age of the customer
- became_member_on (int) - date when customer created an app account
- gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
- id (str) - customer id
- income (float) - customer's income

#### transcript.json

- event (str) - record description (ie transaction, offer received, offer viewed, etc.)
- person (str) - customer id
- time (int) - time in hours since start of test. The data begins at time t=0
- value - (dict of strings) - either an offer id or transaction amount depending on the record
 
# 4. Conclusions from Exploratory Data Analysis and models
## Conclusions
Overall, this project is challenging, mainly due to the structure of the data in the ‘transcript’ dataset.
### Recommendations for company distributing bogo or discount offers:
1. Customers who filled in age with 118 or leave gender or income empty rarely respond to offers. Company could avoid to send offers to these customers who tend not to fill up their profiles.
2. Female customers respond better than males with bogo or discount offer. Company could send more bogo or discount offers to female customers.
3. Senior customers complete offers more than young customers, especially for customers older than 50. Company could send more bogo or discount offers to senior customers.
4. Customers who have higher income has better ratio of completing an offer which is surprising. Company could send more bogo or discount offers to higher income customers.
5. Customers who have longer tenure complete an offer more often. Company could definitely reward longer tenured customers more with bogo or discount offers.
6. The top important variables from best random forest tree model also suggest Customer income, Tenure days, Customer age, Offer delivered by Social, Customers with unknown gender are important for effective offers.
### Recommendations for company distributing informational offers:
1. About 50% of Male customers respond to an informational offer while Female customers slightly respond less often which is different from the response to bogo or discount offers. Company could target informational offers slightly more to male customers.
2. Customers with age under 50 respond to informational offers better. which is opposite to the ones for bogo or discount offers. Company could target informational offers more to customers who are under 50.
3. Customers who filled with age 118, or leave sex and income empty, respond to informational offers less often. which is similar to the bogo or discount offer. Company should send less informational offers to the ones who don’t fill in their profiles.
4. Customers with Low income and Middle income respond to informational offers better. Company could send informational offers to middle income or low income customers.
5. Customers who have longer tenure respond an offer more often. Company could definitely send longer tenured customers more informational offers.
6. The top important variables from best random forest tree model suggest Tenure days, Customer income, Customer age, Offer received time, Number of offers received before current offer are important for an effective offer.
# 5. Further Improvements and Experimentation
Overall the model performances are relatively good in terms of predicting whether bogo/discount offers be completed and informational offers be effective. And the predicting model for bogo/discount performs better than the informational offers. My thoughts of improving informational offers’ predictions are to gain more informations to make better judgements for effective offers as stated above in model performance summary.
In the future, I can also do some more experiment on feature engineering to see if any other new features can improve the model. I can also try different ways to deal with imbalanced dataset for bogo/discount offers.
Also, so far the analysis and models are focused more on customers who receive an offer would use the offer or not. I could also build the transaction datasets to predict how much a customer would spend in Starbucks with or without an offer.
In addition, I could also try some unsupervised machine learning such as KNN to group the customers who will be more likely to respond to a given offer.
# 6.Links for project :
### Blog Post Report for this project present here:
https://dsfjm.medium.com/data-science-help-optimize-starbucks-promotion-strategy-bbf97bb5df86


# 7.Files included:
## 1. data
    - portfolio.json
    - profile.json
    - transcript.json
## 2. scripts
Starbucks_Capstone_notebook.ipynb

   
# 8.Acknowledgement
I want to thank Starbucks and Udacity for dataset, and thank Udacity for advice and review.

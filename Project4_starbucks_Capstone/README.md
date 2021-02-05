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
Starbucks frequently provides offers to its customers through its rewards mobile app to drive more sales. These offers can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). This project focuses on tailoring the promotional offers for customers based on their responses to the previous offers and predict the response of a customer to an offer, meaning whether or not the customer would either complete an discount or bogo offer or the customer would have a transaction after viewing an informational offer.

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
 
# 4.Links for project :
### Blog Post Report for this project present here:
https://dsfjm.medium.com/data-science-help-optimize-starbucks-promotion-strategy-bbf97bb5df86


# 5.Files included:
## 1. data
    - portfolio.json
    - profile.json
    - transcript.json
## 2. scripts
Starbucks_Capstone_notebook.ipynb

   
# 6.Acknowledgement
I want to thank Starbucks and Udacity for dataset, and thank Udacity for advice and review.

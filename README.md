# 1.Library used in this project:
    -pandas
    -numpy
    -scipy
    -sklearn
    -matplotlib
    -seaborn

# 2.Motivation of the project:
This is a classification task with the aim of predicting which loans will default. 
Hopefully this model could help investors to make decisions of investing the loans with different risks.

# 3.Files in the repository:
 ## - licence (BSD 2-Clause License)
 ## - LendinClub-logestic_0929.ipynb 
### •	load data
### •	data cleaning     
       o	derive response variable,
       o	deleting columns with NA >99%,
       o	generate new variable 'credit_len',
       o	drop columns that happen after default,
       o	transform 'int_rate' and 'revol_util' to numerical variable,
       o	transform emp_length and grade to numerical variable,
       o	dummy categorical variables)
### •	build logistic regression 
       o	lasso to select features 
       o	Use AUC as performance matrics)
### •	Data exploration
        
 ## - LoanStats3a.csv (The data contains lending club loan data from 2007 to 2011.)
 ## - Readme.md

# 4. A summary of the results of the analysis
This visualization results were published using [Media](https://medium.com/@biofjm/should-we-invest-on-lending-club-loans-4f2a31736fca).


## Question1: What is the overall yearly funded amount and return rate?
   Answer:   The total loan amount issued from LendingClub continued to grow from less than 1M in 2007 to more than 200M in 2011 and the return rate also increased from about 1% to over 12%.
  
## Question2: Are there a significant portion of default loans.
   Answer:   Yes, from 2007 to 2011, the defalut loans are 15.2% of the total loans.

## Question3: How to choose low risk of loans to invest?
   Answer: Features like low interes loans and 36-month term loans have lower risk of default.
   
 # 5. Acknowledgement
   ## 1) I learned some visualization codes from this kaggle post here:
      https://www.kaggle.com/janiobachmann/lending-club-risk-analysis-and-metrics
   ## 2) Some column knowledge and concepts are learned from the below github post.
      https://github.com/harrinac/lending_club_analysis

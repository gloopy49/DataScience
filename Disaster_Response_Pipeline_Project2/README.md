# Disaster Response Pipeline Project
## Data Scientist Nanodegree
## Data Engineering

# 1.Library used in this project:
    -pandas
    -numpy
    -sqlalchemy
    -sklearn
    -matplotlib
    -nltk
    -pickle
    -Flask
    -Plotly

# 2.Motivation of the project:
This project will provide disaster responses to analyze data from Figure Eight to build a model for an API that classifies disaster messages.
This project will include a web app where an emergency worker can input a new message and get classification results in categories. 
The web app will also display visualizations of the data.


# 3.Project Components:
 ## ETL Pipeline
 ### File data/process_data.py:
    - Reads messages and categories dataset
    - Merges and cleans data
    - Save data in a SQLite database

 ## Machine Learning Pipeline
 ### File models/train_classifier.py:
    - Loads data from SQLite database
    - Creates training and testing datasets
    - Builds a machine learning pipeline
    - Trains the model
    - Optimize hyperparameters using GridSearchCV
    - Evaluate the model with testing dataset
    - Export final model as a pickle file

 ## Flask Web App
 ### File app/run.py:
    - Load datasets and pickle model file
    - data visualization
# 4. Running pipelines 

### 1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

### 2. Run the following command in the app's directory to run your web app.
    `python run.py`

### 3. If run from local: Go to http://0.0.0.0:3001/
###    If Running the Web App from the Project Workspace IDE:
       open another Terminal, type env|grep WORK
       Go to https://spaceid-3001.udacity-student-workspaces.com/


# 4. Some screen shots from the web app

Information can be seen on the main app page: 
![alt text](https://github.com/gloopy49/DataScience/tree/master/Disaster_Response_Pipeline_Project2/images/flask_web_app.png)

# 5. Files included:
## 1. data
    1) disaster_categories.csv: dataset contains categories
    2) disaster_messages.csv: dataset contains messages
    3) process_data.py: ETL pipeline scripts to load, clean, merge and store data into a database
    4) DisasterResponse.db: SQLite database containing processed messages and categories data
## 2. models
    1) train_classifier.py: machine learning pipeline scripts to build, train, and save a model
    2) classifier.pkl: exported model in pkl format
## 3. app
    1) run.py: Python script to integrate all above files and to start the web application
    2) templates contains html file for the web applicatin

   
# 6. Acknowledgement
I want to thank Figure Eight for dataset, and thank Udacity for advice and review.

import sys
import re
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import nltk 
import nltk
nltk.download(['punkt', 'wordnet', 'stopwords'])
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import Pipeline
import pickle
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.multioutput import MultiOutputClassifier

def load_data(database_filepath):
    """
       Function:
       load data from database
       Args:
       database_filepath: the path of the database
       Return:
       X (DataFrame) : Message features dataframe
       Y (DataFrame) : target dataframe
       category (list of string) : target columns'name list
    """
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table('database_disaster_tbl', engine)
    category_names = df.columns[4:].tolist()
    X = df['message']  # Message Column
    Y = df.iloc[:, 4:]  # Classification label
    return X, Y, category_names


def tokenize(text):
    """
    Function: split text into words and return the root form of the words
    Args:
      text(string): the message
    Return:
      lemm(list of string): a list of the message words
    """
    #normalize and tokenize text
    words = word_tokenize(re.sub(r"[^a-zA-Z0-9]", " ", text.lower()))
    
    # Remove stopwords
    words = [t for t in words if t not in stopwords.words('english')]
    
    # Lemmatization
    lemm = [WordNetLemmatizer().lemmatize(w) for w in words]
    return lemm   


def build_model():
    """
     Function: build a model for classifing the disaster messages
     Return:
       cv(list of str): classification model
     """

    # Create a pipeline
    pipeline = Pipeline([
            ('vect', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer()),
            ('clf', MultiOutputClassifier(AdaBoostClassifier()))
     ])
    
    # Create Grid search parameters
    parameters = {
    'clf__estimator__learning_rate': [0.2,0.4],
    'clf__estimator__n_estimators': [100,200]
     }

    cv = GridSearchCV(pipeline, param_grid=parameters)

    return cv


def evaluate_model(model, X_test, y_test, category_names):
    """
    Function: Evaluate the model performance and print the results for each output category of the dataset.
    Args:
    model: the classification model
    X_test: messages in test dataset
    Y_test: actual values for target variable in test dataset
    category_names: output category of the target
    """
    y_pred = model.predict(X_test)
    # Calculate the accuracy for each of them.
    for i in range(len(category_names)):
       print('Category: {} '.format(category_names[i]))
       print(classification_report(y_test.iloc[:, i].values, y_pred[:, i]))
       print('Accuracy {}\n\n'.format(accuracy_score(y_test.iloc[:, i].values, y_pred[:, i])))


def save_model(model, model_filepath):
    '''
    Save the model in a pickle file 
    Args:
        model (pipeline.Pipeline): model to be saved
        model_filepath (str): destination pickle filename
    '''
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
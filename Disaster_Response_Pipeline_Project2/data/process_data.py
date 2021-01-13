import sys
import pandas as pd 
import numpy as np 
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''
    input:
        messages_filepath: The path for messages dataset.
        categories_filepath: The path for categories dataset.
    output:
        df: The merged dataset
    ''' 
#load messages data from csv
    messages = pd.read_csv(messages_filepath)
#load categories data from csv
    categories = pd.read_csv(categories_filepath) 
# merge
    df=pd.merge(messages,categories, on='id',how='outer')
    return df

def clean_data(df):
    '''
    input:
        df: The raw dataset.
    output:
        df: The cleaned dataset
    ''' 
    categories = df['categories'].str.split(';',expand=True)
    row=categories.head(1)
    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = row.applymap(lambda x: x[:-2]).iloc[0,:].tolist()
    categories.columns = category_colnames
    
    #Convert category values to just numbers 0 or 1
    # - Iterate through the category columns in df to keep only the last character of each string (the 1 or 0). For example, `related-        #0` becomes `0`, `related-1` becomes `1`. Convert the string to a numeric value.
    # - You can perform [normal string actions on Pandas Series](https://pandas.pydata.org/pandas-docs/stable/text.html#indexing-with-        #str), like indexing, by including `.str` after the Series. You may need to first convert the Series to be of type string, which        #you can do with `astype(str)`.
    for column in categories:
    # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1]  
    # convert column from string to numeric
        categories[column] =  categories[column].astype(int)
    
    # drop the original categories column from `df`
    df.drop(columns=['categories'],inplace=True)
    
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df,categories],axis=1)
    # check number of duplicates
    #  Remove duplicates 
    df.duplicated().sum()
    df.drop_duplicates(inplace=True)

    return df

def save_data(df, database_filename):
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('database_disaster_tbl', engine, index=False) 


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
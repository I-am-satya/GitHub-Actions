import pandas as pd

def validate_data(file_path="synthetic_data.csv"): 
  try:
    df= pd.read.csv(file_path) 
  except FileNotFoundError:
    print("X synthetic_data.csv not found. Please run generate_data.py first.")
    return
  expected_columns={'Age', 'Income', 'Purchased'}
  
  actual_columns= set(df.columns)
  
  print(" Column validation:")
  
  print("Expected:", expected_columns)
  
  print("Actual:", actual_columns)
  
  print("Match:", expected_columns == actual_columns)
  
  print("\n Data types:") 
  
  print(df.dtypes)
  
  print("\n Value ranges:")
  
  print("Age:", df['Age'].min(), "-", df['Age'].max()) 
  
  print("Income:", df['Income'].min(), "-", df['Income'].max()) 
  
  print("Purchased values:", df['Purchased'].unique())
  
  print("\n Basic statistics:")
  
  print(df.describe())

if __name__ ="__main__": 
  validate_data()

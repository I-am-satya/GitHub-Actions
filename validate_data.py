import pandas as pd

def validate_data(file_path="synthetic_data.csv"): 
  try:
    df= pd.read_csv(file_path) 
  except FileNotFoundError:
    print("X synthetic_data.csv not found. Please run generate_data.py first.")
    return
  expected_columns={'Name','Email','Phone Number','Age', 'Income', 'Purchased'}
  
  actual_columns= set(df.columns)
  
  print(" Column validation:")
  
  print("Expected:", expected_columns)
  
  print("Actual:", actual_columns)
  
  print("Match:", expected_columns == actual_columns)
  

if __name__=="__main__": 
  validate_data()

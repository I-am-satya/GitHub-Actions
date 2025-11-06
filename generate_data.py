import numpy as np


import pandas as pd

3

و

4

5

def generate_synthetic_data(num_samples=1000, seed=42):

>

6

7

8

9

np.random.seed(seed)

A

# Generate synthetic data

10

11

ages np.random.randint(18, 70, size=num_samples)

income = np.random.normal(loc=50000, scale=15000, size=num_samples).astype(int)

purchase_probability = np.clip((income / 100000) + (ages / 100), 0, 1)

purchased = np.random.binomial (1, purchase_probability)

12

13

#Create DataFrame

14

df = pd.DataFrame({

15

'Age': ages,

16

'Income': income, 'Purchased': purchased

17

18

})

return df

def main():

df = generate_synthetic_data()

print("Synthetic data preview:")

print(df.head())

#Save to CSV

df.to_csv('synthetic_data.csv', index=False)

print("Synthetic data saved to 'synthetic_data.csv'.")

if_name _main__":

main()

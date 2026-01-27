import pandas as pd
from sklearn.___ import ___, ___

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a65bbc96-309e-4df9-a790-a1eb8c815a1c/penguins_imputed.csv')
# Assign X, y variables
y = df['species']
X = df.drop('species', axis=1)
# Initialize an ...Encoder object
feature_enc = ___
# Encode the 'island' and 'sex' columns and add encodings to X
encoded = ___.___(___).toarray()
X[['island_Biscoe', 'island_Dream', 'island_Torgersen', 'sex_FEMALE', 'sex_MALE']] = encoded
X.drop(['island', 'sex'], axis=1, inplace=True) # Drop initial 'sex', 'island' columns
# Encode the y
label_enc = ___
y = ___
# Print the X
print(X)
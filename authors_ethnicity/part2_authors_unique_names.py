import pandas as pd

# only keep unique names
# run on HPC

df = pd.read_csv("/scratch/mps565/capstone_data/AuthorsNoEthnicity.csv")
df = df['NormalizedName'].unique()
print("number of unique names: " + str(len(df)))
df = pd.DataFrame(df)
df.to_csv("AuthorsNoEthnicityUnique.csv", index = False)
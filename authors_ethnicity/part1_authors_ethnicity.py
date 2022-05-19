import pandas as pd

# TASK 2
# find number of scientists in MAG dataset for which ethnicity was not identified yet
# run on HPC

# all scientists in MAG dataset
df1 = pd.read_csv("/scratch/mps565/capstone_data/mag/Authors.txt", sep = "\t", names = ["AuthorId", "Rank", "NormalizedName", "DisplayName", "LastKnownAffiliationId", "PaperCount", "PaperFamilyCount", "CitationCount", "CreatedDate"], usecols = ["NormalizedName"])

# scientists for which we already know ethnicity
df2 = pd.read_csv("/scratch/mps565/capstone_data/AuthorName_Race_Ethnicity.tsv",sep = "\t", names = ["NormalizedName", "Ethnicity", "Details"], usecols = ["NormalizedName"])

df = df1.merge(df2,how='left', indicator=True)
df = df[(df['_merge']=='left_only')].copy() 
df = df.drop(columns='_merge').copy()

# print number of authors with ethnicity not identified
print(len(df.index))

# save AuthorsId with ethnicity not identified
df.to_csv("AuthorsNoEthnicity.csv", index = False)

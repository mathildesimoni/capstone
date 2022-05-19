import pandas as pd

# count the number of papers for each author with no ethnicity identified
# run on HPC

df_authors = pd.read_csv("/scratch/mps565/capstone_data/mag/Authors.txt", sep = "\t", names = ["AuthorId", "Rank", "NormalizedName", "DisplayName", "LastKnownAffiliationId", "PaperCount", "PaperFamilyCount", "CitationCount", "CreatedDate"], usecols = ["NormalizedName", "PaperCount"])

df_ethnicity = pd.read_csv("/scratch/mps565/capstone_data/AuthorsNoEthnicityUnique.csv")
df_ethnicity = df_ethnicity.set_axis(["NormalizedName"], axis=1, inplace=False)


df_authors = df_authors.groupby(["NormalizedName"], sort = False)["PaperCount"].sum().reset_index()

df_authors_papers = df_authors.merge(df_ethnicity, on = "NormalizedName")

df_authors_papers.to_csv("AuthorsPaperCount.csv", index = False)
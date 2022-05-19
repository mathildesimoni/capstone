import pandas as pd

# inferring the discipline of authors algorithm
# sample code in jupyter notebook part 2
# this code was run on HPC

# PART1: calculate confidence each paper belongs to a given high-level discipline
# Relationships between low and high level disciplines are available in ParentChildrenDisciplines.csv
# Fields of study for papers are available in PaperFieldsOfStudy.txt
df_disciplines = pd.read_csv("ParentChildrenDisciplines.csv", names = ['child', 'parent'])
df_papers = pd.read_table("advanced/PaperFieldsOfStudy.txt", names = ['paper', 'discipline', 'confidence'])

df = df_papers.merge(df_disciplines, left_on='discipline', right_on='child')
df = df[['paper', 'parent', 'confidence']]
df = df.rename(columns = {'parent': 'field'})
df = df[df['confidence'] >= 0.5] 

df = df.groupby(['paper', 'field'])['confidence'].sum().reset_index()
df = df.rename(columns = {'confidence': 'score'})


# PART 2: calculate confidence that a scientist belongs to a high-level discipline
# Author IDs of all papers are available in aperAuthorAffiliationsSample.csv
df_author = pd.read_csv("mag/PaperAuthorAffiliations.csv", names = ['paperId', 'authorId'])
# change above line
# df_author = pd.read_csv("mag/PaperAuthorAffiliations.csv", sep="\t", names = ['PaperId', 'AuthorId', 'AffiliationId', 'AuthorSequenceNumber', 'OriginalAuthor', 'OriginalAffiliation'], usecols = ['PaperId', 'AuthorId'])
# df_author.dropna()
df_author = df_author[['authorId', 'paperId']]

df = df_author.merge(df, left_on='paperId', right_on='paper')
df = df[['authorId', 'paperId','field', 'score']]

df = df.groupby(['authorId', 'field'])['score'].sum().reset_index()


# PART 3: calculate primary discipline of a scientist
df = df[df.groupby(['authorId'])['score'].transform(max) == df['score']]
df.to_csv("ScientistsPrimaryDiscipline.csv", index = False)
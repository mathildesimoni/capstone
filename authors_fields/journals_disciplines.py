import pandas as pd

# inferring the discipline of authors algorithm
# sample code in jupyter notebook part 3
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

# code for journals starts here
df_journal = pd.read_csv("mag/Papers.csv", names = ['paperId', 'journalId'])
# add more line, open as Michael showed me
# df_journal = pd.read_csv("mag/Papers.txt", sep="\t", names = ['PaperId', 'Rank', 'Doi', 'DocType', 'PaperTitle', 'OriginalTitle', 'BookTitle', 'Year', 'Date', 'OnlineDate', 'Publisher', 'JournalId', 'ConferenceSeriesId', 'ConferenceInstanceId', 'Volume', 'Issue', 'FirstPage', 'LastPage', 'ReferenceCount', 'CitationCount', 'EstimatedCitation', 'OriginalVenue',  'FamilyId', 'FamilyRank', 'DocSubTypes', 'CreatedDate'],  usecols = ['PaperId', 'JournalId'])
# df_journal.dropna()
df_journal = df_journal[['journalId', 'paperId']]
# print(df_journal)

df = df_journal.merge(df, left_on='paperId', right_on='paper')
df = df[['journalId', 'paperId','field', 'score']]
# print(df)

df = df.groupby(['journalId', 'field'])['score'].sum().reset_index()
# print(df)

df = df[df.groupby(['journalId'])['score'].transform(max) == df['score']]

df.to_csv("journals_primary_dsicipline.csv", index = False)
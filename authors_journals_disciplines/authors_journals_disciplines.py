import pandas as pd

# inferring the discipline of authors algorithm

# PART1: calculate confidence each paper belongs to a given high-level discipline
# Relationships between low and high level disciplines are available in ParentChildrenDisciplines.csv
# Fields of study for papers are available in PaperFieldsOfStudy.txt
df_disciplines = pd.read_csv("ParentChildrenDisciplines.csv", names = ['ChildId', 'ParentId'])
df_papers = pd.read_csv("advanced/PaperFieldsOfStudy.txt", sep="\t", names = ['PaperId', 'FieldOfStudyId', 'Score'])

df0 = df_papers.merge(df_disciplines, left_on='FieldOfStudyId', right_on='ChildId')
df0 = df0[['PaperId', 'ParentId', 'Score']]
df0 = df0.rename(columns = {'ParentId': 'FieldId'})
df0 = df0[df0['Score'] >= 0.5] 

df0 = df0.groupby(['PaperId', 'FieldId'])['Score'].sum().reset_index()


# PART 2: calculate confidence that a scientist belongs to a high-level discipline
# Author IDs of all papers are available in PaperAuthorAffiliationsSample.txt
df_author = pd.read_csv("mag/PaperAuthorAffiliations.txt", sep="\t", names = ['PaperId', 'AuthorId', 'AffiliationId', 'AuthorSequenceNumber', 'OriginalAuthor', 'OriginalAffiliation'], usecols = ['PaperId', 'AuthorId'])
df_author = df_author[['AuthorId', 'PaperId']]

df = df_author.merge(df0, on='PaperId')
df = df[['AuthorId', 'PaperId','FieldId', 'Score']]

df = df.groupby(['AuthorId', 'FieldId'])['Score'].sum().reset_index()


# PART 3: calculate primary discipline of a scientist
df = df[df.groupby(['AuthorId'])['Score'].transform(max) == df['Score']]
df.to_csv("ScientistsPrimaryDiscipline.csv", index = False)


# PART 4: calculate confidence that a journal belongs to a high-level discipline
# Journal IDs of all papers are available in Papers.txt
df_journal = pd.read_csv("mag/Papers.txt", sep="\t", names = ['PaperId', 'Rank', 'Doi', 'DocType', 'PaperTitle', 'OriginalTitle', 'BookTitle', 'Year', 'Date', 'OnlineDate', 'Publisher', 'JournalId', 'ConferenceSeriesId', 'ConferenceInstanceId', 'Volume', 'Issue', 'FirstPage', 'LastPage', 'ReferenceCount', 'CitationCount', 'EstimatedCitation', 'OriginalVenue',  'FamilyId', 'FamilyRank', 'DocSubTypes', 'CreatedDate'],  usecols = ['PaperId', 'JournalId'])
# df_journal.dropna()
df_journal = df_journal[['JournalId', 'PaperId']]

df = df_journal.merge(df0, on='PaperId')
df = df[['JournalId', 'PaperId','FieldId', 'Score']]

df = df.groupby(['JournalId', 'FieldId'])['Score'].sum().reset_index()


# PART 5: calculate primary discipline of a journal
df = df[df.groupby(['JournalId'])['Score'].transform(max) == df['Score']]
df.to_csv("JournalsPrimaryDiscipline.csv", index = False)


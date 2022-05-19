# capstone

### Files

* authors_fields/ : *directory for take 1: find disciplines of authors and journals in MAG*
    * part1_parent_children_disciplines.ipynb : *find highest level discipline for each lower level discipline speficied in MAG*
    * part2_authors_disciplines.ipynb : *sample code to link each AUTHOR in MAG with a discipline (the one with the highest score)*
    * part3_journals_disciplines.ipynb : *sample code to link each JOURNAL in MAG with a discipline (the one with the highest score)* 

    * authors_disciplines.py : *same as "part2_authors_disciplines.ipynb" file but was run on HPC*
    * journals_disciplines.py : *same as "part3_journals_disciplines.ipynb" file but was run on HPC*
    * authors_journals_diciplines.py : *script with code of both "authors_disciplines.py" and "journals_disciplines.py"* 

    * highLevelDisciplines.csv : *contains the 19 highest level disciplines in MAG*
    * FieldOfStudyChildren.txt : *relationships between lower and higher level disciplines in MAG*
    * ParentChildrenDisciplines.csv : *result of part1 jupyter notebook: each lower level discipline is linked with highest level discipline*
    * PaperFieldsOfStudySample.txt : *sample of papers and disciplines in MAG*
    * PaperAuthorAffiliationsSample.csv : *sample of papers and authors in MAG for part 2 notebook*
    * PaperJournalSample.csv : *sample of papers and journals in MAG for part 3 notebook* 

    * scientists_primary_discipline_sample.csv : *resulting dataset from "part2_authors_disciplines.ipynb"*
    * journals_primary_discipline_sample.csv : *resulting dataset from "part3_journals_disciplines.ipynb"*


* authors_ethnicity/ :
    * part1_authors_ethnicity.py : *get authors in MAG for who ethnicity wasn't identified yet*
    * part2_authors_unique_names.py : *remove duplicate names*
    * part3_count_papers_per_author.py : *count number of papers per author*

    * checkDataset.ipynb : *analyze the dataset with authors for which we don't have ethnicity identified yet*

    * AuthorsNoEthnicity.csv : *result of part1_authors_ethnicity.py*
    * AuthorsNoEthnicityUnique.csv : *result of part2_authors_unique_names.py*
    * unique_authornames_MAG.csv : *dataset with authors for which etnicity was identified before, shared by Bedoor*
    * AuthorsNoEthnicityUniqueRelevant.csv : *after removing duplicates, remove authors for who the classifier didn't return any result in the past*
    * AuthorsPaperCount.csv : *result of part3_count_papers_per_author.py*
    * FinalAuthorsNoEthnicity.csv : *final dataset to send to classifier*






* README.md : *this file*


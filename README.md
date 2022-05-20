# capstone

### Files

* **authors_fields/** : *directory for task 1: find disciplines of authors and journals in MAG*
    * **part1_parent_children_disciplines.ipynb** : *find highest level discipline for each lower level discipline speficied in MAG*  
    * **part2_authors_disciplines.ipynb** : *sample code to link each AUTHOR in MAG with a discipline (the one with the highest score)*
    * **part3_journals_disciplines.ipynb** : *sample code to link each JOURNAL in MAG with a discipline (the one with the highest score)* 
    * 
    * **authors_disciplines.py** : *same as "part2_authors_disciplines.ipynb" file but was run on HPC*
    * **journals_disciplines.py** : *same as "part3_journals_disciplines.ipynb" file but was run on HPC*
    * **authors_journals_diciplines.py** : *script with code from both "authors_disciplines.py" and "journals_disciplines.py"* 
    * 
    * **highLevelDisciplines.csv** : *contains the 19 highest level disciplines in MAG*
    * **FieldOfStudyChildren.txt** : *relationships between lower and higher level disciplines in MAG*
    * **ParentChildrenDisciplines.csv** : *result of part1 jupyter notebook: each lower level discipline is linked with a highest level discipline*
    * **PaperFieldsOfStudySample.txt** : *sample of papers and disciplines in MAG from part 2 and 3 jupyter notebook*
    * **PaperAuthorAffiliationsSample.csv** : *sample of papers and authors in MAG for part 2 jupyter notebook*
    * **PaperJournalSample.csv** : *sample of papers and journals in MAG for part 3 jupyter notebook* 
    * 
    * **scientists_primary_discipline_sample.csv** : *resulting dataset from "part2_authors_disciplines.ipynb"*
    * **journals_primary_discipline_sample.csv** : *resulting dataset from "part3_journals_disciplines.ipynb"*

* **authors_ethnicity/** : *directory for task 2: find ethnicity of authors in MAG*
    * **part1_authors_ethnicity.py** : *get authors in MAG for whom ethnicity wasn't identified yet*
    * **part2_authors_unique_names.py** : *remove duplicate names from part 1 result, run on HPC*
    * **part3_count_papers_per_author.py** : *count number of papers per author in MAG, run on HPC*
    * 
    * **checkDataset.ipynb** : *analyze the dataset with authors for whom we don't have ethnicity identified yet*
    * The following files couldn't be added on Github but can be shared on HPC if requested:
        * **AuthorsNoEthnicity.csv** : *result of part1_authors_ethnicity.py*
        * **AuthorsNoEthnicityUnique.csv** : *result of part2_authors_unique_names.py*
        * **unique_authornames_MAG.csv** : *dataset with authors for which etnicity was identified before, shared by Bedoor*
        * **AuthorsNoEthnicityUniqueRelevant.csv** : *after removing duplicates, remove authors for whom the classifier didn't return any result in the past*
        * **AuthorsPaperCount.csv** : *result of part3_count_papers_per_author.py*
        * **FinalAuthorsNoEthnicity.csv** : *result of checkDataset.ipynb, final dataset to send to classifier*

* **scrap_journals/** : *directory for task 3: webscraping task to get info about editorial boards*
    * **request_module.ipynb** : *contains all scripts which download pages from internet (using request module in Python)*
    * **1 - parsing module journals for each editor.ipynb** : *get all journals for each editor and their link to main pages on library genesis*
    * **2 - Parsing module journals.ipynb** : *get number of pages to scrap for each journal*
    * **3 - Parsing find issue links.ipynb** : *for each journal belonging to each publisher, find links to 1st issues of volumes corresponding to a specific period of time*
    * **4 - Parsing find PDFs.ipynb** : *get the links to relevant PDF documents for the issues previously selected (Relevant PDF means PDF with potential information about the editorial board, the selection is based on a list of keywords)*
    * **5 - Parsing find PDF docs Wiley.ipynb** : *get the VALID links to relevant PDF documents (the previous links from step 4 are not "valid", I needed to do some modifications to get links we can download). Implemented only for Wiley*
    * **6 - Parsing PDFs.ipynb** : *convert PDF documents to textfiles. Implemented only for Wiley*
    * **opt - Analysis links to PDFs.ipynb** : *analysis of results from previous steps*
    * 
    * **JournalsSpringer.csv** : *dataset with info about journals belonging to Springer. Updated at every step*
    * **JournalsWiley.csv** : *dataset with info about journals belonging to Wiley. Updated at every step*
    * **JournalsElsevier.csv** : *dataset with info about journals belonging to Elsevier. Updated at every step*
    * **JournalsTaylor.csv** : *dataset with info about journals belonging to Taylor. Updated at every step*
    * 
    * **JournalsSpringerPDFs.csv** : *dataset with links to relevant PDF documents for journals belonging to Springer. Updated at steps 4 and 5*
    * **JournalsWileyPDFs.csv** : *dataset with links to relevant PDF documents for journals belonging to Wiley. Updated at steps 4 and 5*
    * **JournalsElsevierPDFs.csv** : *dataset with links to relevant PDF documents for  journals belonging to Elsevier. Updated at steps 4 and 5*
    * **JournalsTaylorPDFs.csv** : *dataset with links to relevant PDF documents for  journals belonging to Taylor. Updated at steps 4 and 5*
    * 
    * **JournalsSpringerGotPDFs.csv** : *dataset with bool values to check if I got a link to PDF for each year and each journal belonging to Springer. Updated at step 4*
    * **JournalsWileyGotPDFs.csv** : *dataset with bool values to check if I got a link to PDF for each year and each journals belonging to Wiley. Updated at step 4*
    * **JournalsElsevierGotPDFs.csv** : *dataset with bool values to check if I got a link to PDF for each year and each journals belonging to Elsevier. Updated at step 4*
    * **JournalsTaylorGotPDFs.csv** : *dataset with bool values to check if got I a link to PDF for each year and each journals belonging to Taylor. Updated at step 4*
    * 
    * **ElsevierDOIs.csv** : *contains DOIs for PDFs with relevant editorial info from journals belonging to Elsevier. Sent to Michael*
    * 
    * **elsevier/** : *directory which contains sub-directories for each journal belonging to Elsevier. A sub-directory stores all scraped pages for a specific journal*
    * **springer/** : *directory which contains sub-directories for each journal belonging to Springer. A sub-directory stores all scraped pages for a specific journal*
    * **taylor/** : *directory which contains sub-directories for each journal belonging to Taylor. A sub-directory stores all scraped pages for a specific journal*
    * **wiley/** : *directory which contains sub-directories for each journal belonging to Wiley. A sub-directory stores all scraped pages for a specific journal*
    * 
    * **journals/** : *contains scraped pages with names of all journals in library genesis*

* **README.md** : *this file*


### Instructions to scrap library genesis pages and get PDF documents with editorial board information

* no need to run steps 1 - and 2 - 

* run notebook "**3 - Parsing find issue links.ipynb:**" and don't forget to update list of publishers, start_year and end_year depending on the period of time you want to analyze: this will find all links to issues pages

* run part 4 (**# 4: journal issues: getting all 1st issues of volumes from start_year to end_year**) of request_module.ipynb in order to scrap all issue pages (and don't forget to update list of publishers, start_year and end_year)

* run notebook "**4 - Parsing find PDFs.ipynb**" and don't forget to update list of publishers, start_year and end_year depending on the period of time you want to analyze: this will find links to relevant PDF documents for each issue previously selected

* run part 5 (**# 5: get all PDF for Wiley info pages**) of request_module to get 1st PDF pages (not valid to download). This step was only implemented for Wiley. Need to do the same for Elsevier. 

* run notebook "**5 - Parsing find PDF docs Wiley.ipynb**" to get VALID links (that we can download) to PDFs. This step was only implemented for Wiley. Need to do the same for Elsevier. 

* run part 5.2 (**# 5.2 get actual PDFs**) of request_module to download the PDFs. This step was only implemented for Wiley. Need to do the same for Elsevier. 

* run notebook  "**6 - Parsing PDFs.ipynb**" to convert PDF documents to textfiles. Need to check this code. The error rate is very high.

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
    * **request_module.ipynb** : *contains all scripts which download pages from internet*
    * **1 - parsing module journals for each editor.ipynb** : *get all journals for each editor and their link to main pages on library genesis*
    * **2 - Parsing module journals.ipynb** : *get number of pages to scrap for each journal*
    * **3 - Parsing find issue links.ipynb** : *for each journal in each publisher, find links to issues for a specific period of time*
    * **4 - Parsing find PDFs.ipynb** : *get the links to relevant PDF documents for the issues previously selected (based on a list of keywords)*
    * **5 - Parsing find PDF docs Wiley.ipynb** : *get the VALID links to relevant PDF (the previous link got in step 4 are not "valid", needed to do some modifications to get links we can download). Implemented only for wiley*
    * **6 - Parsing PDFs.ipynb** : *convert PDF documents to textfiles (implemented only for Wiley)*
    * **opt - Analysis links to PDFs.ipynb** : *analysis of results from previous step*
    * 
    * **JournalsSpringer.csv** : *contains about journals belonging to Springer*
    * **JournalsWiley.csv** : *contains about journals belonging to Wiley*
    * **JournalsElsevier.csv** : *contains about journals belonging to Elsevier*
    * **JournalsTaylor.csv** : *contains about journals belonging to Taylor*
    * 
    * **JournalsSpringerPDFs.csv** : *contains links to relevant PDF documents for journals belonging to Springer*
    * **JournalsWileyPDFs.csv** : *contains links to relevant PDF documents for journals belonging to Wiley*
    * **JournalsElsevierPDFs.csv** : *contains links to relevant PDF documents for  journals belonging to Elsevier*
    * **JournalsTaylorPDFs.csv** : *contains links to relevant PDF documents for  journals belonging to Taylor*
    * 
    * **JournalsSpringerGotPDFs.csv** : *dataset with bool values to check if got a link to PDF for each year and each journals belonging to Springer*
    * **JournalsWileyGotPDFs.csv** : *dataset with bool values to check if got a link to PDF for each year and each journals belonging to Wiley*
    * **JournalsElsevierGotPDFs.csv** : *dataset with bool values to check if got a link to PDF for each year and each journals belonging to Elsevier*
    * **JournalsTaylorGotPDFs.csv** : *dataset with bool values to check if got a link to PDF for each year and each journals belonging to Taylor*
    * 
    * **ElsevierDOIs.csv** : *contains DOIs for PDFs with relevant editorial info. Sent to Michael*
    * 
    * **elsevier/** : *contains directories for each journal belonging to elsevier. Those directories store all scraped pages corresponding to the specific journal*
    * **springer/** : *contains directories for each journal belonging to springer. Those directories store all scraped pages corresponding to the specific journal*
    * **taylor/** : *contains directories for each journal belonging to taylor. Those directories store all scraped pages corresponding to the specific journal*
    * **wiley/** : *contains directories for each journal belonging to wiley. Those directories store all scraped pages corresponding to the specific journal*
    * 
    * **journals/** : *contains scraped pages with names of all journals on library genesis website*

* **README.md** : *this file*


### Instructions to scrap library genesis pages and get PDF documents with editorial board information

* no need to run steps 1 - and 2 - 

* run notebook "**3 - Parsing find issue links.ipynb:**" and don't forget to update list of publishers, start_year and end_year depending on the period of time you want to analyze: this will find all links to issues pages

* run part 4 (**# 4: journal issues: getting all 1st issues of volumes from start_year to end_year**) of request_module.ipynb in order to scrap all issue pages (and don't forget to update list of publishers, start_year and end_year)

* run notebook "**4 - Parsing find PDFs.ipynb**" and don't forget to update list of publishers, start_year and end_year depending on the period of time you want to analyze: this will find links to relevant PDF documents for each issue previously selected

* run part 5 (**# 5: get all PDF for Wiley info pages**) of request_module. This step was only implemented for Wiley. Need to do the same for elsevier. 

* run notebook "**5 - Parsing find PDF docs Wiley.ipynb**" (again, only implemented for Wiley) to get valid links to releant PDFs

* run part 5.2 (**# 5.2 get actual PDFs**) of request_module. (again, only implemented for Wiley) go download the relevant PDFs

* run notebook  "**6 - Parsing PDFs.ipynb**" to convert PDF documents to textfiles





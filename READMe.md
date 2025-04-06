# Data Engineer Take-Home Assignment for AllTrails

AllTrails is a freemium consumer subscription app and wants to better understand what factors contribute to revenue growth. One assumption of the company is that encouraging users to record activities (hikes, bike-rides, etc.) soon after their first signup could positively impact Pro subscription rates. Therefore, the company would like you to help the analysts find insights around the relationship between when users sign-up and when they complete their first GPS recording. To aid the data analysts in this task, your job is to write a batch-processing job to create a single clean, structured dataset that can be more-easily manipulated to help them find the data they need.

### Steps taken

1. Read and load TSV files for users and recordings into pandas DataFrames.
2. Parse recording_summary JSON column in recordings into individual columns.
3. Filter out first recording for each user.
4. Join first recordings with users.
5. Calculate time difference in hours between user's signup_date and their first recording.
5. Filter out anomalies (negative values for time differences).
6. Import everything to clean CSV files.

### Assumptions made

1. recording_summary JSON is a well-formed JSON column.
2. user's first recording is selected by earliest recording_date per each user.
3. user has to have at least one recording to be considered.
4. user has to have a sign up date.
5. if difference between user's first recording and their sign up date is negative, treat it as bad data and exclude it.

### Tasks

Warning! This code is written the way that it uses the source files that live in /data folder of this project. However files are too large to be uploaded into this repo so you wiil need to download them manually into your local project folder in order for this code to work properly. File names are recordings_2017.tsv and users_2017.tsv

Initial analysis and data processing is done using python and pandas dataframes. Please make sure you have python3 and pandas installed.

/scripts/processing.ipynb contains the main logic for all the steps taken. You will need Jupyter Notebook/Jupyter Lab/Jupyter Desktop to run it.

There is one more file users_second_recording_bonus_part.ipynb contains analysis for user's second recording (this is a bonus part of the assignment).

Additionally there is a bonus tests/test_processing.py file handles a few testing scenarios of the current logic (please make sure you have pytest installed). 

For that processing.ipynb file is refactored and converted to processing.py file which also lives in /scripts directory. Tests run againts that file.

Also I created a draft version of airflow DAG and put it into /dags directory. This is not a production ready DAG but it is there to demostrate how this pipeline can be automated.

### Next steps

For the next steps final DataFrame can be loaded into Data Warehouse instead of csv files, using parquet or other file format of your choice for further analysis.

Additionally this pipeline can be converted into pySpark taking advantage of spark's distributed nature and parallel processing.

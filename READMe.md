## Data Engineer Take-Home Assignment for AllTrails

AllTrails is a freemium consumer subscription app and wants to better understand what factors contribute to revenue growth. One assumption of the company is that encouraging users to record activities (hikes, bike-rides, etc.) soon after their first signup could positively impact Pro subscription rates. Therefore, the company would like you to help the analysts find insights around the relationship between when users sign-up and when they complete their first GPS recording. To aid the data analysts in this task, your job is to write a batch-processing job to create a single clean, structured dataset that can be more-easily manipulated to help them find the data they need.

# Steps taken

1. Read and load TSV files for users and recordings into pandas DataFrames.
2. Parse recording_summary JSON column in recordings into individual columns.
3. Filter out first recording for each user.
4. Join first recording to users.
5. Calculate time difference in hours between user's signup_date and first recording.
5. Filter out anomalies (negative values for time difference).
6. Import everything to clean CSV files.
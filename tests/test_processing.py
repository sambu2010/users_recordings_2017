import pandas as pd
import pytest
from io import StringIO
from scripts/processing import load_users, load_recordings, get_first_recordings, join_user_recordings

# Random records from users data
USER_DATA = """Pseudo_User_ID\tsignup_date\tstart_date
*1E8FFA834EF4FE81D7B3C4C779D33AE1644A0085\t2017-01-01 00:00:23\t2020-07-03 12:42:23
*8DCFB1F4D4482F892E37AC445138381DFA640ACA\t2017-01-01 00:07:41\tNULL
"""

# Random records from recordings data
RECORDING_DATA = """Recording_ID\tDate_Time\tPseudo_User_ID\tActivity_Type\tRecording_Summary\tCity\tState\tCountry
*C4BE760C32879845A8DC463AD8C530063742D9D8\t2017-01-01 00:58:28\t*5C9CFCAB5CF9E7D86F451C4D867B159F0CEA5C2B\tHiking\t{"calories": 408, "duration": 40, "timeTotal": 3262, "updatedAt": "2020-02-23T04:55:36+00:00", "timeMoving": 2421, "paceAverage": 0.5070741132486465, "speedAverage": 1.9720983064849236, "distanceTotal": 4774.45, "elevationGain": 189, "elevationLoss": 170}\tBarron Park\tCA\tUnited States
*BE7E802DCECBC98F1A12D12C33551871E89498DA\t2017-01-01 01:19:57\t*6C5C9DDA86B57302ADF494993AD166297CE194B7\tHiking\t{"calories": 408, "duration": 40, "timeTotal": 3262, "updatedAt": "2020-02-23T04:55:36+00:00", "timeMoving": 2421, "paceAverage": 0.5070741132486465, "speedAverage": 1.9720983064849236, "distanceTotal": 4774.45, "elevationGain": 189, "elevationLoss": 170}\tBarron Park\tCA\tUnited States
"""

@pytest.fixture
def users_df():
    return load_users(StringIO(USER_DATA))

@pytest.fixture
def recordings_df():
    return load_recordings(StringIO(RECORDING_DATA))

def test_load_users(users_df):
    assert users_df.shape[0] == 2
    assert "user_signup_date" in users_df.columns
    assert "user_start_date" in users_df.columns

def test_load_recordings(recordings_df):
    assert recordings_df.shape[0] == 2
    assert "recording_date_time" in recordings_df.columns
    assert "pace_average" in recordings_df.columns
    assert "calories" in recordings_df.columns
    assert "evelation_gain" in recordings_df.columns

def test_get_first_recordings(recordings_df):
    first_recordings = get_first_recordings(recordings_df)
    assert first_recordings.shape[0] == 2
    assert "recording_date_time" in first_recordings.columns
    assert "evelation_gain" in recordings_df.columns
    assert "updated_at" in recordings_df.columns

def test_join_user_recordings(users_df, recordings_df):
    first_recordings = get_first_recordings(recordings_df)
    final = join_user_recordings(users_df, first_recordings)
    assert "hours_till_first_recording" in final.columns
    assert final["hours_till_first_recording"].ge(0).all()

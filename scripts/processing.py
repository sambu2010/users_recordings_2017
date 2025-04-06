import pandas as pd
import json
from pathlib import Path

def load_users(users_path):
    users_df = pd.read_csv(users_path, sep='\t', parse_dates=["signup_date", "start_date"])
    users_df.columns = users_df.columns.str.lower()
    users_df = users_df.rename(columns={
        "signup_date": "user_signup_date",
        "start_date": "user_start_date"
    })
    return users_df

def load_recordings(recordings_path):
    recordings_df = pd.read_csv(recordings_path, sep='\t', parse_dates=["Date_Time"])
    recordings_df.columns = recordings_df.columns.str.lower()
    recordings_df["recording_summary"] = recordings_df["recording_summary"].fillna('{}').astype(str)
    summary_df = recordings_df["recording_summary"].apply(json.loads).apply(pd.Series)
    recordings_df = pd.concat([recordings_df.drop(columns=["recording_summary"]), summary_df], axis=1)
    recordings_df["updatedAt"] = pd.to_datetime(recordings_df["updatedAt"])
    recordings_df = recordings_df.rename(columns={
        "date_time": "recording_date_time",
        "timeTotal": "time_total",
        "updatedAt": "updated_at",
        "timeMoving": "time_moving",
        "paceAverage": "pace_average",
        "speedAverage": "speed_average",
        "distanceTotal": "distance_total",
        "elevationGain": "evelation_gain",
        "elevationLoss": "elevation_loss"
    })
    return recordings_df

def get_first_recordings(recordings_df):
    recordings_df = recordings_df.sort_values(by=["pseudo_user_id", "recording_date_time"])
    return recordings_df.groupby("pseudo_user_id").first().reset_index()

def join_user_recordings(users_df, first_recording_df):
    df = pd.merge(users_df, first_recording_df, on="pseudo_user_id", how="inner")
    df["hours_till_first_recording"] = (
        (df["recording_date_time"] - df["user_signup_date"]).dt.total_seconds() / 3600
    )
    return df[df["hours_till_first_recording"] >= 0]

def export_to_csv(df, output_path):
    df.to_csv(output_path, index=False)

def main():
    data_dir = Path("../data")
    output_dir = Path("../output")
    users_df = load_users(data_dir / "users_2017.tsv")
    recordings_df = load_recordings(data_dir / "recordings_2017.tsv")
    first_recording_df = get_first_recordings(recordings_df)
    final_df = join_user_recordings(users_df, first_recording_df)

    export_to_csv(final_df, output_dir / "users_first_recording_2017.csv")

if __name__ == "__main__":
    main()

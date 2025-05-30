import pandas as pd
import matplotlib.pyplot as plt
import pytz

# Parse start date
df = pd.read_csv('strava_activities.csv', parse_dates=['start_date'])

# Filter out activities to run only
df = df[df['type']=='Run']

# set date range
utc = pytz.UTC
start_date = utc.localize(pd.to_datetime('2025-01-01'))
end_date = utc.localize(pd.to_datetime('2025-04-30'))

# filter the dataframe

df_filtered = df[(df['start_date'] >= start_date) & (df['start_date'] <= end_date)]

print(df_filtered[['start_date', 'name', 'distance', 'moving_time', 'average_heartrate', 'average_speed', 'average_cadence']].head())
print(f"\nFiltered down to {len(df_filtered)} runs between Jan 6 and May 4, 2025.")

def format_pace(pace_float):
    minutes = int(pace_float)
    seconds = int(round((pace_float - minutes) * 60))
    # handle edge case where seconds rounds to 60
    if seconds == 60:
        minutes += 1
        seconds = 0
    return f"{minutes}:{seconds:02d}"


df['start_date'] = pd.to_datetime(df['start_date'])
df['distance_miles'] = df['distance'] / 1609.34
df['moving_time_min'] = df['moving_time'] / 60
df['pace_min_per_mile'] = df['moving_time_min'] / df['distance_miles']
df['cadence_spm'] = df['average_cadence'] * 2
df['week'] = df['start_date'].dt.to_period('W').apply(lambda r: r.start_time)



# Filter pace using IQR-based method
q1 = df['pace_min_per_mile'].quantile(0.25)
q3 = df['pace_min_per_mile'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

df = df[(df['pace_min_per_mile'] >= lower_bound) & (df['pace_min_per_mile'] <= upper_bound)]



print("Avg Weekly Distance:", df['distance_miles'].mean())
print("Avg Pace:", df['pace_min_per_mile'].mean())

weekly_summary = df.groupby('week').agg({
    'distance_miles': 'sum',
    'moving_time_min': 'sum',
    'pace_min_per_mile': 'mean',
    'average_heartrate': 'mean',
    'average_speed': 'mean',
    'cadence_spm': 'mean'
}).reset_index()




weekly_summary = weekly_summary.round(2)


ig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

# 1. Weekly Mileage
axs[0].plot(weekly_summary['week'], weekly_summary['distance_miles'], marker='o')
axs[0].set_title('Weekly Mileage')
axs[0].set_ylabel('Miles')
for x, y in zip(weekly_summary['week'], weekly_summary['distance_miles']):
    axs[0].text(x, y + 0.3, f"{y:.1f}", ha='center', fontsize=8)

# 2. Weekly Pace
axs[1].plot(weekly_summary['week'], weekly_summary['pace_min_per_mile'], marker='o', color='green')
axs[1].set_title('Weekly Avg Pace')
axs[1].set_ylabel('Min/Mile')
for x, y in zip(weekly_summary['week'], weekly_summary['pace_min_per_mile']):
    pace_str = format_pace(y)
    axs[1].text(x, y + 0.05, pace_str, ha='center', fontsize=8)


# 3. Heart Rate
axs[2].plot(weekly_summary['week'], weekly_summary['average_heartrate'], marker='o', color='red')
axs[2].set_title('Weekly Avg Heart Rate')
axs[2].set_ylabel('BPM')
for x, y in zip(weekly_summary['week'], weekly_summary['average_heartrate']):
    axs[2].text(x, y + 1, f"{y:.0f}", ha='center', fontsize=8)

# 4. Cadence
axs[3].plot(weekly_summary['week'], weekly_summary['cadence_spm'], marker='o', color='purple')
axs[3].set_title('Weekly Avg Cadence')
axs[3].set_ylabel('SPM')
axs[3].set_xlabel('Week')
for x, y in zip(weekly_summary['week'], weekly_summary['cadence_spm']):
    axs[3].text(x, y + 1, f"{y:.0f}", ha='center', fontsize=8)

plt.tight_layout()
plt.show()
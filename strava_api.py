import requests
import pandas as pd

CLIENT_ID = '162124'
CLIENT_SECRET = 'c52dff6d17f72a64502e1a4c3aec341042870d94'
REDIRECT_URI = 'http://localhost'

# Step 1: Generate authorization URL
auth_url = f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&approval_prompt=force&scope=activity:read_all"
print("Go to this URL and authorize access:", auth_url)

# Step 2: After authorizing, paste the code from the redirected URL
auth_code = input("Paste the authorization code here: ")

# Step 3: Exchange code for access token
token_response = requests.post(
    url='https://www.strava.com/oauth/token',
    data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': auth_code,
        'grant_type': 'authorization_code'
    }
)

tokens = token_response.json()
access_token = tokens['access_token']
print("Access token received.")

# Step 4: Fetch your activities
headers = {'Authorization': f'Bearer {access_token}'}
activities_response = requests.get(
    "https://www.strava.com/api/v3/athlete/activities",
    headers=headers,
    params={'per_page': 100}
)


activities = activities_response.json()

# Step 5: Load into pandas DataFrame
df = pd.json_normalize(activities)
print(df[['name', 'start_date', 'distance', 'moving_time', 'average_speed', 'total_elevation_gain']])

# Step 6 (optional): Export to CSV
df.to_csv('strava_activities.csv', index=False)
print("Activities saved to strava_activities.csv")

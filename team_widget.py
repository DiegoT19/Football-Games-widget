import tkinter as tk
import requests
from datetime import datetime

# Your Football Data API key here
API_KEY = "YOUR API KEY"

# Function to fetch upcoming FC Barcelona matches
def get_team_fixtures():
    url = "https://api.football-data.org/v4/teams/81/matches?status=SCHEDULED"
    headers = {"X-Auth-Token": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["matches"][:5]  # Get next 5 matches
    else:
        print("Error fetching data:", response.status_code)
        return []

# Update widget with match details
def update_widget():
    matches = get_team_fixtures()
    display_text = "⚽ Upcoming YOUR TEAM Matches:\n\n" #Make sure to change "TEAM" with yout team's name
    for match in matches:
        opponent = match["awayTeam"]["name"] if match["homeTeam"]["name"] == "YOUR TEAM" else match["homeTeam"]["name"] #Make sure to change "YOUR TEAM" with yout team's name
        date = datetime.strptime(match["utcDate"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b, %Y - %H:%M")
        display_text += f"📅 {date}\n🆚 {opponent}\n\n"
    
    label.config(text=display_text)
    root.after(3600000, update_widget)  # Update every hour (3600000 ms)

# Tkinter window setup
root = tk.Tk()
root.title("TEAM Widget") #Make sure to change "TEAM" with yout team's name
root.geometry("350x400")

label = tk.Label(root, text="Loading...", font=("Helvetica", 12), justify="left", wraplength=300)
label.pack(pady=20)

update_widget()  # Initial call
root.mainloop()

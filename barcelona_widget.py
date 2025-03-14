import tkinter as tk
import requests
from datetime import datetime

# Your Football Data API key here
API_KEY = "YOUR KEY"

# Function to fetch upcoming FC Barcelona matches
def get_barca_fixtures():
    url = "https://api.football-data.org/v4/teams/81/matches?status=SCHEDULED"
    headers = {"X-Auth-Token": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["matches"][:10]  # Get next 10 matches
    else:
        print("Error fetching data:", response.status_code)
        return []

# Update widget with match details
def update_widget():
    matches = get_barca_fixtures()
    display_text = "⚽ Upcoming FC Barcelona Matches:\n\n"
    
    for match in matches:
        opponent = match["awayTeam"]["name"] if match["homeTeam"]["name"] == "FC Barcelona" else match["homeTeam"]["name"]
        date = datetime.strptime(match["utcDate"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b, %Y - %H:%M")
        competition = match["competition"]["name"]
        display_text += f"📅 {date}\n🆚 {opponent}\n🏆 {competition}\n\n"
    
    text_widget.config(state=tk.NORMAL)  # Enable editing
    text_widget.delete("1.0", tk.END)   # Clear current content
    text_widget.insert(tk.END, display_text)  # Insert new content
    text_widget.config(state=tk.DISABLED)  # Make it read-only

    root.after(3600000, update_widget)  # Update every hour

# Make the widget draggable
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def on_drag(event):
    x = root.winfo_x() + (event.x - root.x)
    y = root.winfo_y() + (event.y - root.y)
    root.geometry(f"+{x}+{y}")

# Tkinter window setup
root = tk.Tk()
root.title("FC Barcelona Widget")
root.geometry("400x500")

# Make window always on top
root.attributes("-topmost", True)

# Make window transparent
root.attributes("-alpha", 0.9)

# Widget styling
root.configure(bg="#0A0A2A")
title_label = tk.Label(root, text="🔵🔴 FC Barcelona Matches", font=("Helvetica", 16, "bold"), fg="white", bg="#0A0A2A")
title_label.pack(pady=10)

# Scrollable text widget for match display
text_frame = tk.Frame(root, bg="#0A0A2A")
text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_widget = tk.Text(text_frame, font=("Courier", 12), fg="white", bg="#1C1C3A", wrap=tk.WORD, yscrollcommand=scrollbar.set, relief=tk.FLAT, height=20)
text_widget.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=text_widget.yview)

# Make the widget draggable
root.bind("<Button-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", on_drag)

# Populate the widget
update_widget()

root.mainloop()

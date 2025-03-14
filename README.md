# Football-Games-widget
This widget will create a small window with the next upcoming games of your favorite team without the need of going to an external page!!

Step 1:
  Ensure you have Python installed (version 3.8+ recommended). You can check by running:
  
    python --version
    
  If not installed, download it from python.org.
    
Step 2: 
  Install Required Packages
  
    pip install requests
    
Step 3:
  Go to https://www.football-data.org/ and sign up for a free API key.
  Once registered, save your API key for later.

Step 4: Create the Widget \n
  Download the code provided

Step 5:
  Save the script (e.g., team_widget.py) and run:
  
    python team_widget.py


## EXTRA ##
If you want the widget to be an application:
  Install pyinstaller (a tool to package Python programs):
  
    pip install pyinstaller
Create the executable:
  Run the following command in the same directory where barca_widget.py is located:

    pyinstaller --noconsole --onefile team_widget.py
    
  --noconsole: Hides the command window.
  --onefile: Bundles everything into a single .exe file.
Locate the executable:
  Go to the dist/ folder in the same directory.
  You’ll find barca_widget.exe. Double-click to launch the widget!

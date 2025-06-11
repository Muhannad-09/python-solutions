import webbrowser
import time

# List of favorite or frequently used websites
websites = [
    "https://www.github.com",
    "https://www.gmail.com",
    "https://www.linkedin.com",
    "https://www.google.com",
    "https://www.stackoverflow.com",
]

# Open each website in a new browser tab
for site in websites:
    webbrowser.open_new_tab(site)
    time.sleep(1)  # Pause 1 second between tabs


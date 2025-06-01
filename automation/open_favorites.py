import webbrowser  # lets us open URLs

# Step 1: A list of websites to open
websites = [
    "https://www.google.com",
    "https://www.youtube.com",
]

# Step 2: Go through each website and open it
for site in websites:
    webbrowser.open(site)

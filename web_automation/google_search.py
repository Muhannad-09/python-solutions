import webbrowser
import urllib.parse

# Ask the user for a search query
query = input("What do you want to search for on Google? ")

# Encode the search text for a URL
encoded_query = urllib.parse.quote_plus(query)

# Build the full Google search URL
url = f"https://www.google.com/search?q={encoded_query}"

# Open it in the default web browser
webbrowser.open(url)
print(f"Searching for: {query}")


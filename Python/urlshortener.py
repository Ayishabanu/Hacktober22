import pyshorteners
url = input("Enter your url: ")
s = pyshorteners.Shortener(api_key="YOUR_KEY")
print(s.bitly.short(url))

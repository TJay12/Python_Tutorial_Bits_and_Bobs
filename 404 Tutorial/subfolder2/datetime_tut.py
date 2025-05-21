from datetime import datetime

# Get current date and time
print(datetime.now())

# Format to readable string
print(datetime.now().strftime("%Y-%m-%d"))
print(datetime.now().strftime("%H:%M:%S")) # 24hr
print(datetime.now().strftime("%I:%M %p")) # 12hr
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

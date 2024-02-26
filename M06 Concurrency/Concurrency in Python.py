import os #Used this to make running the program a bit easier 
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "today.txt"
file_path = os.path.join(current_dir, file_name)

#13.1
current_date = datetime.now().strftime("%Y-%m-%d")
with open(file_path, "w") as file:
    file.write(current_date)

#13.2
with open(file_path, "r") as file:
    today_string = file.read()

#13.3
parsed_date = datetime.strptime(today_string, "%Y-%m-%d")

print("Today's String:", today_string)
print("Parsed Date:", parsed_date)

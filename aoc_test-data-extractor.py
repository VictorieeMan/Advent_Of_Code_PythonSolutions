"""Created: 2023-02-08
Purpose: Extract the input data from the https://adventofcode.com website,
and store it in an easy machine readable file structure for the individual
solutions to read from. Used for testing code.

The online data have the following link structure:
https://adventofcode.com/20YY/day/DD/input

YY >= 15, in [15,<This Year>]
DD in [1,25]
"""
import requests
from pathlib import Path

repository_url = "https://github.com/VictorieeMan/Advent_Of_Code_PythonSolutions"
newFileContent_base = "\"\"\"" + "Created: 2023-, by @VictorieeMan\n" 
newFileContent_base = newFileContent_base + "Repository url: " + repository_url

session_uid = input("Cookie UID:")
session = requests.session()
session.cookies.set("session", session_uid, domain=".adventofcode.com")

base_url = "https://adventofcode.com/" # sample "https://adventofcode.com/2022/day/1/input"

days = range(1,26)
events = range(2015,2023)

for event in events:
    for day in days:
        data_url = base_url + str(event) + "/" + "day" + "/" + str(day) + "/input"
        request = session.get(data_url)

        eventYY = str(event)
        dayNN = str(day)

        # Note the importance of this placement, before altering the dayNN below.
        event_url = base_url + eventYY + "/day/" + dayNN
        newFileContent = newFileContent_base + "\nEvent url: " + event_url +"\n\"\"\""

        if(day < 10):
            dayNN = "0" + dayNN

        path_uri = "events/" + str(event) + "/day" + dayNN
        Path(path_uri).mkdir(parents=True, exist_ok=True)

        data_filename = path_uri + "/input.txt"
        with open(data_filename,'wb') as file:
            file.write(request.content)

        solution_filename = path_uri + "/" + eventYY + "-" + dayNN + "-sol.py"
        with open(solution_filename,'w') as file:
            file.write(newFileContent)
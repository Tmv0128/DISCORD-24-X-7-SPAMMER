from webserver import keep_alive
import requests

channelID = 976071787488096306
headers = {
    "authorization":
    ""NzY2MjQzMDM2NjczNjA1NjQz.GdUFlN.klENUFyZkdULXNlWDdvSVVmYUZDb1JiZ2YzWXpwVko2WktEbXkybmZ0ZVdFMExtNzJpRXZ4ZnA4SUMxWWM3bEdWSDR6dDBaVHdhcHlRNEE0""
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})

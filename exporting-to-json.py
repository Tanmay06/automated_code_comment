# import sqlite3
import json
# import re

with open('view.sql', 'r') as sql_file:
    sql_script = sql_file.read()

sql_commands = sql_script.split(';')

sql_commands = [command.strip().replace('\n', ' ') for command in sql_commands if command.strip()]

sql_data = {"sql_commands": sql_commands}

with open('views.json', 'w') as json_file:
    json.dump(sql_data, json_file, indent=4)

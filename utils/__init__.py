import os
import pygsheets


service_file = os.environ["service_file"]
gc = pygsheets.authorize(service_file=service_file)
sheetname = "Поиск 2022"
sh = gc.open(sheetname)

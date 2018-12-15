import pandas as pd
import pygal as pg
from pygal.style import DarkStyle
dic = {}
#creat dictionary

data = pd.read_csv("years.csv")
year = range(2552, 2562)
dic['Number of Deaths'] = data['Number of deaths']
dic ['Number of Injured'] = data['number of Injured']
line_chart = pg.Bar(style=DarkStyle)
line_chart.x_labels = year
line_chart.title = 'graph of deaths and injuries in 2552 - 2561'
# import file
# 7 days dangerous
# setting key = 'Number of Deaths and setting vallue = A column named 'Number of deaths' form data'
# setting key = 'Number of Injured and setting vallue = A column named 'number of Injured' form data'
#type chart
#setting value x axis = year
#name chart


for i in dic:
    line_chart.add(i, dic[i])
line_chart.render_to_file('graph of deaths and injuries in 2552 - 2561.svg')

# create cahart
# export file svg

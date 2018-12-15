import pandas as pd
import pygal as pg
from pygal.style import DarkStyle
dic = {}

#creat dictionary

data = pd.read_csv("year2559.csv")
day = range(1, 8)
dic['Number of Accidents'] = data['accidents']
dic['Number of Injured'] = data['injuries']
dic ['Number of Deaths'] = data['deaths']
line_chart = pg.Bar(style=DarkStyle)
line_chart.x_labels = day
line_chart.title = 'graph of deaths and injuries and accidents during 7 Days dangerous in Songkran Festival in 2559'

# import file
# 7 days dangerous
# setting key = 'Number of Accident and setting vallue = A column named 'accidents' form data'
# setting key = 'Number of Injured and setting vallue = A column named 'injuries' form data'
# setting key = 'Number of Deaths and setting vallue = A column named 'deaths' form data'
#type chart
# setting value x axis = day
#name chart

for i in dic:
    line_chart.add(i, dic[i])
line_chart.render_to_file('Songkran in 2559.svg')
# create cahart
# export file svg

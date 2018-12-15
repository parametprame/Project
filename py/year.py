import pandas as pd
import pygal as pg
from pygal.style import DarkStyle
dic = {}
#creat dictionary


data = pd.read_csv("years.csv") # import file
year = range(2552, 2562)
dic['Number of Accidents'] = data['Number of accidents']
line_chart = pg.Line(interpolate='cubic', style=DarkStyle)
line_chart.x_labels = year
line_chart.title = 'Number of Accidents in 2552 - 2561'
# import file
# years 2552-2561
# setting key = 'Number of Accident and setting vallue = A column named 'Number of accidents' form data'
#type chart
# setting value x axis = year
#name chart

for i in dic:
    line_chart.add(i, dic[i]) # create
line_chart.render_to_file('year.svg') # export file svg

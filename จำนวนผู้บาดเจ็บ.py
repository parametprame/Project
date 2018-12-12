import pygal
line_chart = pygal.Line()
line_chart.title = 'Number of Casualty'
line_chart.x_labels = map(str, range(2552, 2562))
line_chart.add('จำนวนผู้บาดเจ็บ', [4332, 3802, 3476, 3320, 3040, 3225, 3559, 3656, 3808, 3897])

line_chart.render_to_file('ผู้บาดเจ็บ.svg')

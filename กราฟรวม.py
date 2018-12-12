import pygal
line_chart = pygal.Bar()
line_chart.title = 'Number of deaths and Number of Casualty'
line_chart.x_labels = map(str, range(2552, 2562))
line_chart.add('จำนวนผู้เสียชีวิต', [373, 361, 271, 320, 321, 322, 364, 442, 390, 418])
line_chart.add('จำนวนผู้บาดเจ็บ ', [4332, 3802, 3476, 3320, 3040, 3225, 3559, 3656, 3808, 3897])

'''line_chart.add('2559',      [442, 3656])
line_chart.add('2560',  [390, 3808])
line_chart.add('2561',  [418, 2897])'''
line_chart.render_to_file('number_chart4.svg')

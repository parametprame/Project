import pygal
line_chart = pygal.Line()
line_chart.title = 'Number of Dead'
line_chart.x_labels = map(str, range(2552, 2562))
line_chart.add('จำนวนผู้เสียชีวิต', [373, 361, 271, 320, 321, 322, 364, 442, 390, 418])

line_chart.render_to_file('ผู้เสียชีวิต.svg')

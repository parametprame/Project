import pygal
line_chart = pygal.Bar()
line_chart.title = 'Number of deaths during the Songkran festival over the past 5 years'
'''line_chart.x_labels = map(str, range(2557, 2561))'''
line_chart.add('2552', [3977])
line_chart.add('2553', [3516])
line_chart.add('2554', [3215])
line_chart.add('2555', [3129])
line_chart.add('2556', [2828])
line_chart.add('2557', [2992])
line_chart.add('2258', [3373])
line_chart.add('2559', [3447])
line_chart.add('2560', [3690])
line_chart.add('2561', [3724])
line_chart.render_to_file('number_chart.svg')

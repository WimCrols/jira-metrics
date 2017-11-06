from datetime import date

from visualizer import VisualizerCsv


def test_output():
    visualizer = VisualizerCsv()
    data = [
        (date(2000, 1, 1), "foo", 1234),
        (9, "Teddy bear", "Barbie doll"),
        (date(2000, 1, 15), None, "Pots"),
    ]
    assert visualizer.output(data) == '''\
2000-01-01\tfoo\t1234
9\tTeddy bear\tBarbie doll
2000-01-15\t\tPots
'''

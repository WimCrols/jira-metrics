from datetime import date

from metrics_open_bugs import MetricOpenBugs
from visualizer import VisualizerCsv


def main():
    metric = MetricOpenBugs()
    data = metric.get_data(date(2016, 1, 1), date(2016, 2, 1))  # date.today())
    visualizer = VisualizerCsv()
    print()
    print(visualizer.output(data))


main()

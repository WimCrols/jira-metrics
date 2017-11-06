import csv

from io import StringIO


class VisualizerCsv:
    """
    Writes given output as CSV, so it can be imported in e.g. Google Sheets.
    """

    def output(self, data, delimiter='\t'):
        """
        Each list item will be written as a line.
        :param data: :type: List of tuples
        :param delimiter: Separator character
        """
        out = StringIO()
        writer = csv.writer(out, delimiter=delimiter, lineterminator='\n')
        writer.writerows(data)
        result = out.getvalue()
        out.close()
        return result

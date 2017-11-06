import pytest
from datetime import date
from unittest.mock import MagicMock

from pytest import raises

from jirawrapper.query import JiraQuery
from metrics_distribution_bugs import MetricDistributionBugs
from metrics_open_bugs import MetricOpenBugs


def test_create_data():
    metric = MetricDistributionBugs()
    metric.add_squad('Haedwyn', jql)
    metric.add_squad('Jodariel', jql)
    metric.add_squad('Rukey', jql)
    results = metric.get_data(date(2000, 1, 1), date(2000, 1, 25))

    assert results == [""
            ('Week', 'Haedwyn', 'Jodariel', 'Rukey'),
            (date(2000, 1, 1), 1, 2, 3),
            (date(2000, 1, 8), 1, 2, 3),
            (date(2000, 1, 15), 2, 3, 4),
    ]


def test_create_data_with_bad_range():
    with raises(RuntimeError):
        MetricDistributionBugs().get_data(date(2000, 1, 1), date(1999, 1, 25), [])

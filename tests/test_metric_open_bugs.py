import pytest
from datetime import date
from unittest.mock import MagicMock

from pytest import raises

from jirawrapper.query import JiraQuery
from metrics_open_bugs import MetricOpenBugs


# noinspection PyProtectedMember
def test_total_open_bugs_for_week():
    bug_count = 31
    query_mock = JiraQuery(None)
    query_mock.count = MagicMock(return_value=bug_count)
    metric = MetricOpenBugs(query_mock)
    assert bug_count == metric._get_total_open_bugs_for_week(date(2009, 8, 7))
    metric.jira_query.count.assert_called_once_with(
        'Type = bug AND (Role = development OR Project = "UWA Squad") AND'
        ' Resolution WAS IN (EMPTY) ON (2009-08-07) AND Created <= 2009-08-07')


# noinspection PyProtectedMember
def test_new_bugs_for_week():
    bug_count = 16
    query_mock = JiraQuery(None)
    query_mock.count = MagicMock(return_value=bug_count)
    metric = MetricOpenBugs(query_mock)
    assert bug_count == metric._get_new_bugs_for_week(date(2009, 8, 7))
    metric.jira_query.count.assert_called_once_with(
        'Type = bug AND (Role = development OR Project = "UWA Squad") AND'
        ' (Resolution = Done OR Resolution = Unresolved) AND Created >= 2009-08-07 AND Created < 2009-08-14')


def test_create_data():
    """ get_data returns data for every week STARTED between start and end date. """
    bug_count_total = 9
    bug_count_new = 1

    metric = MetricOpenBugs()
    metric._get_total_open_bugs_for_week = MagicMock(return_value=bug_count_total)
    metric._get_new_bugs_for_week = MagicMock(return_value=bug_count_new)

    results = metric.get_data(date(2000, 1, 1), date(2000, 1, 25))

    assert results == [
            ('Week', 'Total open bugs', 'Delta new bugs'),
            (date(2000, 1, 1), bug_count_total, bug_count_new),
            (date(2000, 1, 8), bug_count_total, bug_count_new),
            (date(2000, 1, 15), bug_count_total, bug_count_new),
            (date(2000, 1, 22), bug_count_total, bug_count_new),
    ]


def test_create_data_with_bad_range():
    with raises(RuntimeError):
        MetricOpenBugs().get_data(date(2000, 1, 1), date(1999, 1, 25))

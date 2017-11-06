from datetime import date

from jirawrapper.backend import create_jira_backend
from jirawrapper.query import JiraQuery


def test_count_one_issue():
    """ Not a unit test, since it connects to JIRA. """
    query = JiraQuery(create_jira_backend())
    assert 1 == query.count('key = TEX-100')


def test_query_one_issue():
    """ Not a unit test, since it connects to JIRA. """
    query = JiraQuery(create_jira_backend())
    results = query.run('key = TEX-100')
    assert 1 == len(results)
    assert results[0].key == 'TEX-100'


def test_query_date_format():
    query = JiraQuery(None)
    assert '2016-03-28' == query.format_date(date(2016, 3, 28))

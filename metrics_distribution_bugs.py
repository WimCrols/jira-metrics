from jirawrapper.backend import create_jira_backend
from jirawrapper.query import JiraQuery
from datetime import timedelta


class MetricDistributionBugs:
    """
    Returns data about the distribution over squads of incoming bugs per week.
    """

    def __init__(self, jira_query=None):
        """
        :param jira_query: Overridable for testability
        """
        if not jira_query:
            jira_query = JiraQuery(create_jira_backend())
        self.jira_query = jira_query
        self.category_jql = 'Type = bug AND (Role = development OR Project = "UWA Squad")'

    def add_squad(self, squad_name, jql):
        """
        Add a squad to the distribution, so we can see it's part of the data.
        :param squad_name:
        :param jql:
        """
        pass

    def get_data(self, start_date, end_date):
        """
        :param start_date: :type datetime.date
        :param end_date: :type datetime.date
        """
        if end_date <= start_date:
            raise RuntimeError(f'start_date ({start_date}) must be before end_date ({end_date}).')
        # Add header at the top
        results = [('Week',) + squads]
        week_start_date = start_date
        while week_start_date < end_date:
            print(f'Querying for week {week_start_date}...')
            # noinspection PyTypeChecker
            # results.append((week_start_date,
            #                self._get_total_open_bugs_for_week(week_start_date),
            #                self._get_new_bugs_for_week(week_start_date)))
            week_start_date += timedelta(weeks=1)
        return results

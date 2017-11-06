from jirawrapper.backend import create_jira_backend
from jirawrapper.query import JiraQuery
from datetime import timedelta


class MetricOpenBugs:
    """
    Returns data about the historic total of open bugs bugs per week.
    """

    def __init__(self, jira_query=None):
        """
        :param jira_query: Overridable for testability
        """
        if not jira_query:
            jira_query = JiraQuery(create_jira_backend())
        self.jira_query = jira_query
        self.category_jql = 'Type = bug AND (Role = development OR Project = "UWA Squad")'

    def get_data(self, start_date, end_date):
        if end_date <= start_date:
            raise RuntimeError(f'start_date ({start_date}) must be before end_date ({end_date}).')
        # Add header at the top
        results = [('Week', 'Total open bugs', 'Delta new bugs')]
        week_start_date = start_date
        while week_start_date < end_date:
            print(f'Querying for week {week_start_date}...')
            # noinspection PyTypeChecker
            results.append((week_start_date,
                           self._get_total_open_bugs_for_week(week_start_date),
                           self._get_new_bugs_for_week(week_start_date)))
            week_start_date += timedelta(weeks=1)
        return results

    def _get_total_open_bugs_for_week(self, week_start_date):
        """
        :return Total number open bugs for given week.
        :param week_start_date :type datetime.date
        """
        start_date = self.jira_query.format_date(week_start_date)
        count = self.jira_query.count(
            f'{self.category_jql} AND Resolution WAS IN (Unresolved) ON ({start_date}) AND Created <= {start_date}')
        return count

    def _get_new_bugs_for_week(self, week_start_date):
        """
        :return Number of new bugs created in the given week.
        :param week_start_date :type datetime.date
        """
        start_date = self.jira_query.format_date(week_start_date)
        end_date = self.jira_query.format_date(week_start_date + timedelta(weeks=1))
        count = self.jira_query.count(
            f'{self.category_jql} AND (Resolution = Done OR Resolution = Unresolved)'
            f' AND Created >= {start_date} AND Created < {end_date}')
        return count

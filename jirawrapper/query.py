from jirawrapper.issue import JiraIssue


class JiraQuery:
    def __init__(self, jira_backend):
        self.jira_backend = jira_backend

    def format_date(self, date):
        """
        Format inputted date into format expected for JQL.
        :param date: :type datetime.time
        """
        return date.strftime('%Y-%m-%d')

    def run(self, jql):
        return [JiraIssue(i) for i in self.jira_backend.search_issues(jql)]

    def count(self, jql):
        """
        Returns number of issues found for this query (limited to 1000).
        """
        return len(self.jira_backend.search_issues(jql, maxResults=1000, fields='key'))





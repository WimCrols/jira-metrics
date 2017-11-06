from jira import JIRA

from settings import JIRA_USERNAME, JIRA_PASSWORD, JIRA_SERVER


def create_jira_backend():
    return JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD), validate=True)

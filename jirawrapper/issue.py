
class JiraIssue:
    """
    An issue from JIRA.
    """

    # Fields present in JIRA.Issue:
    #
    # aggregateprogress
    # aggregatetimeestimate
    # aggregatetimeoriginalestimate
    # aggregatetimespent
    # assignee
    # attachment
    # comment
    # components
    # created
    # creator
    # customfield_10000
    # customfield_10001
    # customfield_10006
    # customfield_10007
    # customfield_10008
    # customfield_10009
    # customfield_10010
    # customfield_10011
    # customfield_10401
    # customfield_10402
    # customfield_10403
    # customfield_10404
    # customfield_10405
    # customfield_10406
    # customfield_10407
    # customfield_10408
    # customfield_10409
    # customfield_10900
    # customfield_11000
    # customfield_11200
    # customfield_11202
    # customfield_11203
    # customfield_11307
    # customfield_11309
    # customfield_11310
    # customfield_11311
    # customfield_11321
    # customfield_11322
    # customfield_11323
    # customfield_11324
    # customfield_11325
    # customfield_11326
    # customfield_11327
    # customfield_11328
    # customfield_11329
    # customfield_11330
    # customfield_11334
    # customfield_11335
    # customfield_11336
    # customfield_11337
    # customfield_11338
    # customfield_11339
    # customfield_11340
    # customfield_11341
    # customfield_11400
    # customfield_11401
    # customfield_11402
    # customfield_11600
    # customfield_11601
    # customfield_11602
    # customfield_11603
    # customfield_11800
    # customfield_11900
    # customfield_12000
    # customfield_12100
    # customfield_12200
    # customfield_12300
    # customfield_12400
    # customfield_12401
    # customfield_12402
    # customfield_12500
    # customfield_12600
    # customfield_12700
    # customfield_12900
    # customfield_12901
    # customfield_12902
    # customfield_12903
    # customfield_12904
    # customfield_12905
    # customfield_12906
    # customfield_12907
    # customfield_12908
    # customfield_13000
    # customfield_13100
    # customfield_13200
    # description
    # duedate
    # environment
    # fixVersions
    # issuelinks
    # issuetype
    # labels
    # lastViewed
    # priority
    # progress
    # project
    # reporter
    # resolution
    # resolutiondate
    # status
    # subtasks
    # summary
    # timeestimate
    # timeoriginalestimate
    # timespent
    # timetracking
    # updated
    # versions
    # votes
    # watches
    # worklog
    # workratio

    def __init__(self, jira_issue=None):
        """
        :param jira_issue: :type JIRA.Issue to initialize from.
        """
        if jira_issue:
            self.key = jira_issue.key
            self.components = jira_issue.fields.components
            self.created = jira_issue.fields.created
            self.creator = jira_issue.fields.creator
            self.description = jira_issue.fields.description
            self.issuetype = jira_issue.fields.issuetype
            self.labels = jira_issue.fields.labels
            self.project = jira_issue.fields.project
            self.project = jira_issue.fields.project
            self.reporter = jira_issue.fields.reporter
            self.resolution = jira_issue.fields.resolution
            self.resolutiondate = jira_issue.fields.resolutiondate
            self.status = jira_issue.fields.status
            self.summary = jira_issue.fields.summary
            self.updated = jira_issue.fields.updated

    def __repr__(self):
        return f'<JiraIssue {self.key}>'




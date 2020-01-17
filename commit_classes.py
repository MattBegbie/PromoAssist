class Commit:
    def __init__(self, index, company, repo, dateCommited, title, accLink, prLink, JiraLink, pr, jira):
        self.index = index
        self.comany = "Default Company"
        self.repo = repo
        self.dateCommited = None
        self.title = "Default Title"
        self.accLink = "Default Link"
        self.prlink = "Default PR"
        self.pr = "Default pr"
        self.jiraLink = "Default Jira"
        self.jira = 'Default jira'


    def AddRepo(self, repo):
        self.repo = repo

    def AddDate(self, date):
        self.dateCommited = date

    def AddTitle(self, title):
        self.title = title

    def AddAccLink(self, URL):
        self.accLink = URL

    def AddPRLink(self, prNum):
        if prNum == '':
            self.prLink = 'CHECK URL FOR PR LINK'
        elif prNum == 'NoPR':
            self.prLink = 'No PR'
        else:
            self.prLink = 'https://github.com/{0}/{1}/pull/{2}'.format(self.company, self.repo, prNum)

    def AddJiraLink(self, jiraID):
        if jiraID == '':
            self.jiraLink = 'CHECK URL FOR TICKET'
        elif jiraID == 'NoT':
            self.jiraLink = 'No Ticket'
        else:
            self.jiraLink = 'https://{0}.atlassian.net/browse/{1}'.format(self.company, jiraID)


    def PrintData(self):
        print('\tTitle:\t\t{0}'.format(self.title))
        print('\tURL:\t\t{0}'.format(self.accLink))
        print('\tPR Link:\t{0}'.format(self.prLink))
        print('\tTicket:\t\t{0}'.format(self.jiraLink))
        print("\n\n")

    def PrintAll(self):
        print('\tRepo:\t\t{0}'.format(self.repo))
        print('\tIndex:\t\t{0}'.format(self.index))
        print('\tTitle:\t\t{0}'.format(self.title))
        print('\tURL:\t\t{0}'.format(self.accLink))
        print('\tPR Link:\t{0}'.format(self.prLink))
        print('\tTicket:\t\t{0}'.format(self.jiraLink))
        print('\tdate:\t\t{0}'.format(self.dateCommited))
        print("\n\n")

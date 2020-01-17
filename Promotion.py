# python3 ./documents/github/PromoAssist/Promotion.py

import json
from datetime import datetime
from commit_classes import Commit
import sys

sys.stdout.write("\x1b[8;40;121t") #resize the terminal so that everything fits on it without wrapping

repos = [ #specified repos that i want
]
Company = ''
comms = []

def getDiffs():
    index = 0
    for repo in repos:
        doc = './documents/github/PromoAssist/JSON_data/{0}.json'.format(repo)

        with open(doc, "r") as read_file:
            data = json.load(read_file)
        print(repo)

        for dict in data['commits']:
            #set up/reset info for each thing
            currURL = ''
            currCom = ''
            currPR = ''
            currTick = ''
            isPR = False
            isTick = False

            #create the object
            comms.append(Commit(index, company, repo, None, None, None, None, None, None, None))

            #get the title of the commmit
            for character in dict['commit']['message']:
                #print(character, end='')
                if character == "\n": #this just gets the first line because the whole message is written in the url
                    break
                currCom = currCom + character

            #loop goes through the message and searches for the PR number, and Jira ID
            for character in currCom:
                #code getting the ticket info
                if character == ']':
                    isTick = False
                if isTick == True:
                    currTick = currTick + character
                if character == '[':
                    isTick = True

                #this is the code for getting the Pull Request Number, getting the Jira ticket is the same, except the opening will be []
                if character == ')':
                    isPR = False
                if isPR == True:
                    currPR = currPR + character
                if character == '#':
                    isPR = True

            #add the information to the object
            comms[index].AddTitle(currCom)
            comms[index].AddAccLink(dict['html_url'])
            comms[index].AddPRLink(currPR)
            comms[index].AddJiraLink(currTick)
            #print the information
            comms[index].PrintData()

            index = index + 1


getDiffs()

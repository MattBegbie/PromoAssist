

```
██████╗ ██████╗  ██████╗ ███╗   ███╗ ██████╗      █████╗ ███████╗███████╗██╗███████╗████████╗
██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔═══██╗    ██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║   ██║██╔████╔██║██║   ██║    ███████║███████╗███████╗██║███████╗   ██║
██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██║   ██║    ██╔══██║╚════██║╚════██║██║╚════██║   ██║
██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝    ██║  ██║███████║███████║██║███████║   ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝
```

# How to use:
  1. Installation:<br />
    - Clone the repo into your documents folder.
      - The filepath should look something like this -> ``./document/GitHub/PromoAssist/``
      - if it doesnt look like this you can change the filepaths in each file, there are at most one or two filepath references in each file.
  2. Configuring:<br />
    - Make sure all filepaths are right
    - In the `Promotion.py` and `Promotion.sh` files there are two empty arrays named 'Repos' fill them in with the arrays which you wish to use
      - Fill in the python array and company name like below, for however many repos you desire
        ```
        repos = [
        'repo1',
        'repo2',
        'repo3'
        ]
        Company = 'CompanyName'
        ```
      - Fill in the shell array and company name with the same information
        ```
        repo=(
        'repo1',
        'repo2',
        'repo3')
        company='CompanyName'
        ```
        **NOTES:**
        - the information in both has to be the same
        - you can only do one company at all time, all repos must be from the same company
    - Ensure you have access to the repos, and create a token **to create a token do the following:**.<br />
    a. login to github.com and click on your profile picture in the top right corner, and select settings<br />
    b. in settings, navigate to developer settings, and then personal access tokens<br />
    c. click generate new token<br />
    d. if prompted for password sign in to enter sudo mode<br />
    e. select the correct permissions required. suggested:<br />
      I. repo - all within repo<br />
    f. the big green 'generate token' button<br />
    g. or you can look at this [website](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)<br />
    h.  _remember this can be used over and over again. so you can either delete it after a single use or store it somewhere safe as if it was a password_ <br />
  3. Running the program (standard):<br />
    - running the program is possible through console.<br />
    - In the console type `sh ./documents/github/PromoAssist/Promotion.sh`<br />
      - _FUN FACT_: each file which can be run has the command used to run it commented in the first line, this way you can easily run the filefor debugging and such.<br />
    - The program will ask for your token. If you do not have one refer to the end of '**2. Configuring:**'<br />
    - That is all you need. The program should now gather your information. For help refer to 'HELP' at the bottom of this readme<br />
  4. using the information for the better of society:<br />
    - standard output will look somewhat like this:<br />

    ```
    repo1
    	Title:		 Reworked docker environment (#4146)
    	URL:		   https://github.com/CompanyName/repo1/commit/921103db8259eb9de72f42db8b939895f5651489
    	PR Link:	 https://github.com/CompanyName/repo1/pull/4146
    	Ticket:		 CHECK URL FOR TICKET

    	Title:		[FM-123] Adding data to Builder (#4167)
    	URL:		  https://github.com/CompanyName/repo1/commit/6kl7n3kbkpje24m5smri7qb6eyyptf78islbec3r
    	PR Link:	https://github.com/CompanyName/repo1/pull/4167
    	Ticket:		https://weeverapps.atlassian.net/browse/FM-123

        ...
    ```
    - Note in the first commit there is no ticket in the title, so there is no `Ticket:` url given, check for it manually by using the `URL:` provided.
    - The only information that you need to put in the promotion document is the `PR Link:`, and `Ticket:`
  5. HELP:
      - sorry bud, but you are on your own. Just kidding. Email me at md.begbie@gmail.com if you run into any issues


![WeeverApps](https://weeverapps.com/wp-content/uploads/2019/03/Weever-Apps-logo-with-shadow.png "WeeverApps")

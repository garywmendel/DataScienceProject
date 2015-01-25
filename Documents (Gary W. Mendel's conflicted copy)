#### January 28: Data Exploration and Analysis Plan


Gary W. Mendel:

**What is/are the question/s I hope to answer?**

 1. Yopine - What are the natural content 'Categories' that have been
    created via app usage as arrived at scientifically using data from tables 'Poll' and 'Brainstorm'.
    
 2. Yopine - What is the overall tone/sentiment of votes, contributions and comments?  Is the Yopine user base mostly happy and positive or angry a-holes?
 3. Yopine - When I get a new document (aka poll), how accurately can I automatically place it into an existing category?

**Q.**  **What data have I gathered, and how did I gather it?**
**A.**  I exported the Poll and Brainstorm tables from Yopine-LIVE production dbms

 - Corresponding Datasets:
	 -  [POLL table ](https://www.dropbox.com/s/pf4gv0cdh05np2h/poll.csv?dl=0) & [metadata](https://www.dropbox.com/s/xduv6prclzg1ri9/metadata.xlsx?dl=0): 
		 - isBtoP
		 - isNonShareable
		 -  name
		 -  pollAddress
		 -  pollAnswer
		 -  pollComments
		 - pollCreatedAt
		 -  pollId
		 -  pollInvitees
		 -  pollLocation
		 -  pollNearMeInvited
		 - pollQuestion
		 -  pollState
		 -  pollTags
		 -  pollThemeImage
		 -  pollVisibility
		 - pollType
		 -  userId
	 -  [BRAINSTORM table](https://www.dropbox.com/s/16h3dqnubxf5zpy/brainstorm.csv?dl=0) & [metadata](https://www.dropbox.com/s/xduv6prclzg1ri9/metadata.xlsx?dl=0):
		 - XYZ...coming

**Q. What steps have I taken to explore the data?**
**A.** I visually inspected it to gain a deep understanding of what was what; then I parsed a single record into a text file and further understand exactly what field mapped to its corresponding object in the app;  I then went to office hours with Kevin on Jan 11.  
We concluded that the best way to deal with the polls would be to cluster them as documents.  
Kevin suggested talking to Brandon about an NLP topic called "topic modeling".  I talked to  Brandon but we have to pick that convo back up.
Kevin provided a [code snippet](https://gist.github.com/justmarkham/5331105f5e22577e00ac) that automatically pulls the poll answers and vote count into a dictionary...note the poll 'answers and votes' are contained in column e, 'PollAnswer'.

My next inclination would be to expand the code to iterate through the entire data set(s).  Currently it takes only record 3881 (a high response record pertaining to the Sony/The Interview headline).
I would create a dictionary of that data then use NLP techniques to answer my questions.

**Q.**  **Which areas of the data have you cleaned, and which areas still need cleaning? **
**A.**  I have cleaned the column 'PollAnswer' which accounts for the aforementioned data (answers and vote count).  I need to do the same to column L "pollQuestion".

**Q.**  **What insights have you gained from your exploration? **
**A.**  TBD

**Q.**  **Will you be able to answer your question with this data, or do you need to gather more data (or adjust your question)?  **
**A.** For Q1 & 2, yes this data should do it.  Both questions revolve around being able use NLP to gather trending keywords.  I will need to figure out how to associate given words with a category.  For example:  for category 'Sports', keywords 'baseball', football', 'basketball', 'hockey' etc would all represent occurrences or a poll that could be categorized as Sports.  The same goes for column pollTags (hashtags).

For Q3,  I will have to talk to Kevin as it was his idea.

**Q.**  **How might you use modeling to answer your question?  **
**A.**  Natural Language Processing via topic modeling.  This is the next phase I will investigate in the coming week.
 

	
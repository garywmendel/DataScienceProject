Craig, this is a very interesting project as sun spots, for me, go back to my childhood when i first learned about them.  i remember thinking they were cool (both temperature and hip-wise) but totally flummoxed by how they could possibly be so, surrounded by the immeasurable heat and energy that is a star.  i learned quite a bit reviewing your project and am even more in awe of the fact that solar flares are so powerful that they can affect electronic systems at such distances.  
also, you will likely get extra credit from Sinan for mentioning "x-ray flux" which smacks of "flux-capacitor".

These are my observations, comments and questions:
---------------------------------------------
- in your narrative you state "The ability to predict solar flares from observable solar features, such as sunspots, would allow protective measures to be taken on critical systems prior to the arrival of the flare." i would be very curious as to what types of measures could be taken to, ostensibly, thwart/shield/protect varying forms of infrastructure from this type of threat.  what immediately comes to mind is, like you might have at one time unplugged all of your electrical appliances during a lighting storm, municpalities would shut down parts of the grid or impose rolling blackouts or simply stop the flow in a pipeline etc.  its anecdotal relative to this assignment but i am curious.

- goes_sunspot_parser.py - you state you are using data from '82-'14 but the range parm is set to '75-'15.
	
- i got into the data GOES x-ray dataframe (goes_MX) in goes_1975_2014.csv which helped me answer questions like 'how are x-ray flares tracked and identified? - sunspot_region_number and obc lat_long.
-  a question i have is 5,630 instances of x_ray_class M/X over 39 years seems low, for which we are probably grateful...wondering what the total number is adding A, B, C.

- i got into the data sunspot_regions dataframe in USAF_sunspot_1981_2013.csv decided to understand 'Zurich'. I noticed there are 25,600 rows with a NULL zurich value.  wondering if they're missing part of the Zpc or if its just some incomplete data.  then i looked, but couldnt find anywhere in the code where you stripped the rows with NULLs?  might not matter but seems as if it would.
-  very interesting was the volume of sunspots and their relative size and the fact that you really cant see them without some pretty good aid, is a testament to the sheer size of the sun...!!

- obviously you broke the loops up into three data files in light of the data volume.

- i ran flare_prediction.py locally and got (1st set) plots of:
[Zurich Class vs Count](https://www.dropbox.com/s/a6d5l7mvgu7m1l4/ZClassVCount.png?dl=0)
[Penumbra Class vs Count](https://www.dropbox.com/s/xb4ifrkeicwugo7/PvalueVCount.png?dl=0)
[Compactness Class vs Count](https://www.dropbox.com/s/omxga02p76v63ua/CompactVCount.png?dl=0)
[X-ray Class Vs Count](https://www.dropbox.com/s/66oib72nj4gamtq/X-rayClassVCount.png?dl=0)

This is a great project with code (that works)...as i went through it i could think of myriad real-life business cases.  If the senate can get the votes to override Obama's Keystone Pipeline veto, you will have a clear opportunity.  : ))

> Written with [StackEdit](https://stackedit.io/).

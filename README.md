# Campaign_Spending_Rematch_Elections

The relationship between campaign spending and votes received is the subject of widespread research and speculation. In the two years leading up to the 2018 elections, congressional campaigns spent over 1.13 billion dollars. Another $3.29 billion dollars was spent by political parties and PACs. Many powerful people would likely spend large quantities of money for the means to accurately measure the impact of these expenditures. 
 
Alas, elections are complex. It is difficult to even identify all of the influencing factors that contribute to election results, let alone quantify said factors. To name a few: 

1. Candidate Appeal
2. Party Affiliation
3. World Affairs / Economy
4. Voter Turnout
5. Incumbent, Challenger, or Open Seat?
6. State & District

And yet, we're talking about $4+ billion dollars, so we should probably be able to detect a difference... right?

Detecting a difference may be the easy part; many studies have shown a positive correlation between challenger spending and votes received. The greater challenge lies in controlling for the many variables that could skew the results. Inspired by a study discussed in Freakonomics, I decided to focus specifically on rematch elections. In other words, instances in which the same two leading candidates have competed against each other multiple times. Levitt's paper (cited below) goes into specifics of how this approach controls for several externalities that could introduce bias. 

Steven D. Levitt (1994) '[Using Repeat Challengers to Estimate the Effect of Campaign Spending on Election Outcomes in the U.S. House](http://pricetheory.uchicago.edu/levitt/Papers/LevittUsingRepeatChallengers1994.pdf)', The Journal of Political Economy, Vol. 102: Iss. 4. 

### Getting the Data
I use Stanford's Database on Ideology, Money in Politics, and Elections (DIME). This is a comprehensive collection that combines campaign finance data, election results, and other relevant information. 

[Download Data](https://dataverse.harvard.edu/api/access/datafile/2865309?gbrecs=true) 

[Download Codebook](https://dataverse.harvard.edu/file.xhtml?fileId=2865308&version=2.2#)

### Running the Code
**This repo is a work in progress.** All notebooks are currently functional, but I am still adding commentary to **dime_regression** & **dime_EDA** for improved clarity. 

* To replicate the process, start by downloading the data at the link above. 
* Run the file **load.py**. If the downloaded CSV is placed in sub-directory 'data' within the main repository directory, then you should not need to change any filepaths to run the file. 
* You should have a new file called **candidate_df.csv**. This is the file needed to run the code in the **dime_EDA** and **dime_regression** notebooks. The **data_cleaning** notebook loads the original data file and describes the steps of data processing used in **load.py**. 


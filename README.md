# Election Analysis

## Overview
The purpose of this project is to determine the election results of a local Colorado congressional election using Python script. 

## Results 
A Python script was written to determine the election results. The data from the CSV file(https://github.com/chinzjay/Election_Analysis/tree/main/Resources) was read, analyzed and then the output was printed to a text file(https://github.com/chinzjay/Election_Analysis/tree/main/analysis). Using for loops, conditional and logical operators, the winner of the election as well as the county with the higest turnout was determined. 

![code screenshot](https://github.com/chinzjay/Election_Analysis/blob/main/code%20screenshot.PNG)
|:--:|
|Fig 1. Screenshot of the code|

*Fig 1* shows the code snippet to calculate the vote percentage for individual counties and the logic to determine the winning county.
Similarly, the county voter turnout and the percentage of votes for the individual counties were determined. 

The report includes analysis on candidate votes count turnout as well as breakdown by counties.
 - Based on the data given, three counties held elections for three candidates for this local congressional election.
 - 369,711 votes has been cast.
 - The breakdown of the number of votes, and the percentage for each county in the precinct is as follows:
   * **Jefferson** received a total of 38,855 votes that comprised of 10.5% of the total votes.
   * **Denver** received a total of 306,055 votes that comprised of 82.8% of the total votes.
   * **Arapahoe** received a total of 24,801 votes that comprised of 6.7% of the total votes.
 - The candidate results of the election is as follows:
   * **Charles Casper Stockham** received 23.0% of the vote and 85,213 votes.
   * **Diana DeGette** received 73.8% of the vote and 272,892 votes. 
   * **Raymon Anthony Doane** received 3.1% of the vote and 11,606 votes.
 - From the above results, we can see that the county **Denver** has the largest turnout with a total of 306,055 votes. It comprised of 82.8% ot the total votes turnout.
 - It is also evident that the candidate **Diana DeGette** won the election with a total of 272,892 votes which comprised of 73.8% of the total votes.

## Election Audit Summary
Similar to the above results, the winner of any elections can be identified by reusing the code used for this analysis. Some of the enhancements that can be made to this code for detailed analysis includes:
- To identify the candidates with the highest vote count for the individual counties
- To identify the counties with the lowest votes turnout. 
- To identify the 'popular' candidates in each county

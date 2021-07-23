# Election Analysis

## Project overview
A Colorado Board of Elections staff provided the following tasks needed to audit a recent local congressional election.

1. Calculate total numbeer of votes cast.
1. Compile complete list of candidates who received votes.
1. Calculate total number of votes received by each candidate.
1. Calculate percentage of votes received by each candidate.
1. Determine the winner of the election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.9, Visual Studio Code 1.58.2

## Summary
The analysis of the election shows that
- There were 369,711 total votes cast
- The candidates were
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were
  - Charles Casper Stockham received 23.0% of the votes with 85,213 total votes.
  - Diana DeGette received 73.8% of the votes with 272,892 total votes.
  - Raymon Anthony Doane received 3.1% of the votes with 11,606 total votes.
- The winner of the election was
  - Diana DeGette who received 272,892 votes, 73.8% of the total election votes.

## County audit
 The election commission has requested some additional data to complete the audit:
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

A total of 369,711 votes were cast in this congressional election.
Breakdown of the number of votes and the percentage of total votes for each county in the precinct:
* Jefferson: 10.5% (38,855)
* Denver: 82.8% (306,055)
* Arapahoe: 6.7% (24,801)

Denver county had the largest number of votes.

## Election Audit Summary

The recommendation we can conclude from this analysis is that the election commission might explore how this script can be used for any election including but not limited to:
1. larger or smaller elections, like state or city elections - this will require new source data with the same fields
1. additional details added to the final summary reports about the candidates, the financial components that are required to be disclosed by campaigns, or social media data - these would also require new source data, but with additional fields.

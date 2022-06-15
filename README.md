## Imposed instruction

### A. Profile management

1.Entering a profile: a new user must be able to enter his profile by answering successively
questions allowing you to clearly understand your person and your expectations.

**Input**: Profile files

**Outpout**: The same files, enriched with a newline

2.Display of a profile: a visitor must be able to display the profile of any use

**Input**: Profile files, a username

**Outpout**: The information (understandable by a human) about this user

Nb: All profiles will be stored in one or more text files containing one line per registered person.

For example, the line:
martin92,1,28/12/1997,8,4,1,2,2,3,2,3,4,1,2,4,3,5,4,2,1,5


3.Deletion of a profile: a user must be able to delete his profile.

**Input**: Profile files, a username

**Outpout**: The same files, minus the line about the specified user.


### B. Matching Profiles

1.Comparison between two profiles.

**Input**: Profile files, two usernames

**Outpout**: A compatibility value

2.Comparison between a profile and all the others


**Input**: Profile files, two usernames

**Outpout**: The 5 most compatible profiles (or less if 5 are not found), with their values
of compatibility


## Optional features
- Searching for multiple values ​​for the same criterion (for example, I am looking for people with blue or green or gray eyes).
- Write an algorithm that performs optimal matching on all the people registered (learn about optimal matching algorithms).
- Provide statistics on registered members (using visualizations with pyplot by example).
- Create an advanced graphical interface for browsing and consulting profiles, as well as for pairings.
- Store user appointment information. He can add a comment.
- Create a rating system for users encountered.
- Create a chat allowing future lovebirds to get to know each other better.
- Create a connection system with username and password, allowing to know what are the online users.
- Use JSON file format to store data.

# Screenshot

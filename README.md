# PSNE-and-WDS
Finds Pure Strategy Nash Equilibria and lists all Very Weakly Dominant Strategies for each player for a n-player game

### Input Format
The input is a n-Player Game with the payoffs listed in the NFG Format (as described in the [Gambit Project](http://www.gambit-project.org/)).
* First line contains the number of players n.
* The second line contains n space-separated numbers, the ith number corresponding to the number of strategies available to the ith player.
* The third line contains the list of payoffs in the NFG Format

### Output Format
* First line contains the number of PSNE(n_psne).
* Followed by n_psne lines, the ith line containing n space-separated numbers corresponding to the equilibrium strategies for each player respectively.
* Followed by n lines, with the ith line listing the number of very weakly dominant strategies for the ith player followed by the dominant strategies.

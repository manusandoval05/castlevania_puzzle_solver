# A simple solution for solving Pan's temple puzzle 

Do you want to complete Pan's temple puzzle in 5 moves, but you have no idea how? Tried every move but it seems genuinely impossible? 
Would it feel wrong just to search YouTube for a guy with the solutions you desperately desire for a couple of minutes and feel useless?
I will admit it, I ain't really that quick with my mind, especially when it comes to puzzles; just stuttering when trying to solve the second level of "The Room" level of slowness. That's why I went and asked my friend CPU to solve this puzzle for me. 
The problem isn't that conceptually hard once you play the game. But I'll explain it anyway. There are three disks with bridge segments each pointing at a 90 degree direction (relative north, south, east and west). All bridge segments start pointing east, and the objective is to get all segments to point south. Sounds easy, right? Yeah, if it weren't of course because of determined movement patterns.
## Movement patterns
1. If inner disk moves clockwise, medium disk will move counter-clockwise and viceversa
2. If medium disk moves clockwise, inner and outer disk will move counter-clockwise and viceversa
3. If outer disk moves clockwise, medium disk will move counter-clockwise and viceversa.

## Program objective
Solving the problem instinctively isn't that hard, but solving it in only 5 moves becomes kind of hard, especially for me. The program gets the most optimal solution with combinatories, I ain't proud of the BIG O efficiency but it gets the job done
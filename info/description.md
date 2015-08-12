The rooms in the mine floor are connected by corridors of various lengths (they can be isolated from the rest of the mine).
Each room may contain a varying number of miners at any given time.
We should calculate the percent of total miners can escape to the evacuation zone by a given time in an emergency situation.

Room and hallway information can be represented in a matrix (`M`). 
Each room has a number ranging from 0 to N where the matrix has a size of `NxN`.
In the diagonals we are given information about how many robots occupy the room --
`M[i][i]` is how many robots in the i-th room.

In other cells of the matrix, you are given an information about the hallways, 
specifically how much time (in minutes) is required to move from room i to room j
(`M[i][j] == M[j][i]`).
If the time is zero, then a hallway does not exist between these rooms.
The evacuation zone is the room marked with the number 0 (zero).

You are given a building matrix and evacuation time in minutes.
Robots must always use the shortest path to evacuate the mine floor.
By the specified time, how many percentages of the total miners will have escaped?
For this mission, passing through a room doesn’t take any time,
time only flows while passing through hallways.
A room will be considered evacuated if the total time to evacuate is less than or equal to the given time.
**The result should be rounded to integer number.**

For an example take a look at this schema:

```
-----0       -----1
| 0 |--------| 6 |
-----        -----
  |            |
  |            |
  |            |
  |            |
-----2       -----3   -----4
| 4 |--------| 1 |----| 3 |
-----        -----    -----
  |
  |
-----5
| 2 |
-----
```

```
| 0, 40, 40,  0,  0,   0|
|40,  6,  0, 40,  0,   0|
|40,  0,  4, 40,  0,  20|
| 0, 40, 40,  1, 20,   0|
| 0,  0,  0, 20,  3,   0|
| 0,  0, 20,  0,  0,   2|
```

If the given time is 80, then rooms 1, 2, 3 and 5 will be completely evacuated and the result is `100*(6+4+1+2)/16≈81%`.

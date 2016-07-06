"# design_and_analysis of alogirthms - Coursera Stanford course"

1. week 1 - 2 commits
   a. 1st commit - mergeSort implemented
   b. 2nd commit - inversions counted implemented
   
2. week 2: QuickSort.py - 3 commits
   a. 1st commit - randomized quickSort
   b. 2nd commit - deterministic quickSort
   c. 3rd commit - deterministic quickSort exactly as lecture notes instructed, solving problem 1

   QuickSort_last.py - 2 commits
   a. 1st commit - quickSort. pivot is the last element. reserve algorithm - starts from the end of the array and traverses to its beginning
   b. 2nd commit - quickSort. pivot is the last element. 
   c. 3rd commit - quickSort. problem 2 solved. pivot is the last element in the array, it is swapped with the first one and then follows the final implementation in QuickSort.py

   QuickSort_median.py - 1 commit
   a. 1st commit - quickSort. pivot is the median of three. pivot is swapped with the firt element of the array. implementation follows QuickSort.py

3. week3: rSelect_randomized.py
   a. 1st commit - randomized rSelect. Gets the i-th order statistics of an unosrted array

4. week4: bfs.py
   a. 1st commit - breadth-first search implemented - find all findable nodes from a starting node 's'. This implementation asks for a list of nodes and a list of edges. JPG with the two exaples tested with in ./week4/examples
   b. 2nd commit - bfs for shortest path for an undirected and weightless graph

   bfs_path.py
   a. 1st commit - bfs implemented - find shortest path from 'start' to 'end'. This implementation asks for an adjecancy list representation of the graph. It tracks the path from s to a desired node in the graph. added example 3 JPG
   b. 2nd commit - find all paths from node 'start' to node 'end' in the graph G.

   dfs.py
   a. 1st commit - recursive dfs implemented - find all findable nodes from a start node s in a graph.
   b. 2nd commit - recursive dfs implemented - topological sort
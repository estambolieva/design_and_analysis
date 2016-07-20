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
   b. 2nd commit - recursive dfs implemented - topological sort. added example 4 and example 5 JPG

   scc.py
   a. 1st commit - implemented SCC using DFS on the reverse and original graph
   b. 2nd commit - SCC with recursive DFS. using two dicts for the graph and reverse graph instead of a list of lists. PROBLEM: maximum recursion depth reached.
   c. 3rd commit - iterative scc with a stack. this is NOT the solution for problem 4
   d. 4th commit - iterative scc with a stack. solution to problem 4. fixed a bug in the prev. commit - in the indexing of the new nodes (time-1 vs num_nodes-time)

5. week 5: min_heap.py
   a. 1st commit - implemented min heap - the insertion and extract-min fuctions.
   
   dijkstra.py
   a. 1st commit - implemented dijkstra's shortest path with a heap. implemented the heap (insert, extract_min and delete_from_middle
   a.1 for a wrapper class heap implementation over python's heap object, check this solution: https://github.com/ChuntaoLu/Algorithms-Design-and-Analysis/blob/master/week5%20Heap%20and%20Dijkstra's%20shortest%20path/dijkstra.py 
   b. 2nd commit - dijkstra with a heap working, small bugs fixed from prev commit
   c. 3rd commit - fixed a small typo in at the very end when printing the shortest paths for 10 selected nodes.

6. week 6: two_sum.py
   a. 1st commit - implemented two binary searches in a sorted array. 1st: find the index of the first element in the array that is smaller or equal to a given number. 2nd - find the index of the last element in the array that is smaller or equal to a given number
   b. 2nd commit - finds all distinct pairs x,y, where x + y = t, t is in the interval [N,M] inclusively

   median_maintenance.py - used this for hints: http://waytocrack.com/blog/median-in-a-stream-of-integers/
   a. 1st commit - implemented a min heap in a class
   b. 2nd commit - implemented max heap class, in addition to the min heap class
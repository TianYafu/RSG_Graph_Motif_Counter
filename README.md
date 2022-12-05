# RSG_Graph_Motif_Counter
Calculate the distribution of motifs in RSG Graph

For any given graph, such as this one:

![](img/graph_motif_distrib_1.png)

We can generate graph motif distribution vector, which represents the motif distribution of this graph.

This distribution could be of any size, according to the amount of motifs you may want to use.

For example, Here we generate the motif distribution vector of the previous random graph using graph motifs from 1 node to 6 nodes. Here is the distribution:

![](img/graph_motif_distrib.png)

However, for a somehow larger, and denser graph, things will go weird:

Like this one, it takes much more time to calculate.

![](img/graph_motif_distrib_4.png)

![](img/graph_motif_distrib_3.png)

And calculating this will take a long time...

![](img/graph_motif_distrib_5.png)

## Pre-computed graph motifs

Here we list all connected graph motifs with in size 1-7

You can load them easily without any time-consuming calculation.

Graph motifs stores in ```data/```

### Size-1 Graph Motif

![](img/M0.png)

### Size-2 Graph Motif

![](img/M2.png)

### Size-3 Graph Motif

![](img/M3.png)

### Size-4 Graph Motif

![](img/M4.png)

### Size-5 Graph Motif

![](img/M5.png)

### Size-6 Graph Motif

![](img/M6.png)

### Size-7 Graph Motif

![](img/M7.png)







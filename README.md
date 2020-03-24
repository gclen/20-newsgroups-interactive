You can see the interactive widget [here](https://gclen.github.io/20-newsgroups-interactive/plots/umap_20_newsgroups_interactive.html).


### Methodology

1. Embed the [20 newsgroups dataset](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html) using [UMAP](https://umap-learn.readthedocs.io/en/latest/)
2. Cluster the embedding using [HDBSCAN](https://hdbscan.readthedocs.io/en/latest/index.html) to find related posts
3. Rank each point by its distance to a representative point within the cluster to find relevant documents within a cluster.
4. Use Bokeh to create widgets to visualize and interact with the embedding
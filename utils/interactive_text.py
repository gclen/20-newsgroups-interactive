from bokeh.models import Div

#header
header = Div(text="""<h1>Exploring the 20 newsgroups dataset</h1>""")

# title for the toolbox
toolbox_header = Div(text="""<h1>Toolbox:</h1>""")


description_search = Div(text="""<h3>Filter by keyword:</h3><p1>Enter a keyword to search for. It will search the text as well as 
the document category. Please keep in mind that only 140 characters of the posts are kept in the plot. Press enter to search. 
Clear and press enter to reset the plot.</p1>""")

description_slider = Div(text="""<h3>Filter by the Clusters:</h3><p1>The slider below can be used to filter the target cluster. 
Simply slide the slider to the desired cluster number to display the plots that belong to that cluster. 
Slide back to 20 to show all.</p1>""")

description_checkbox = Div(text="""<h3>Ignore outlying points:</h3><p1>The checkbox below can be used to ignore documents that are not part of a cluster.</p1>""")

citation = Div(text="""<p>This notebook was adapted from <a href="https://github.com/MaksimEkin/COVID19-Literature-Clustering/blob/master/COVID19_literature_clustering.ipynb"> a notebook created by MaksimEkin</a></p>""")
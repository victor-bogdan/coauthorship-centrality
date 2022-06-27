from coauthorship_centrality.utils.data import build_centrality_data
from coauthorship_centrality.utils.graph import build_networkx_graph, compute_graph_node_centrality


def compute_yearly_graph_centrality(yearly_graph_data, centrality_measure):
    yearly_graph_centrality_data = {}

    for year, year_data in yearly_graph_data.items():

        yearly_graph_centrality_data[year] = year_data.copy()

        year_nx_graph = build_networkx_graph(year_data)

        year_graph_centrality = compute_graph_node_centrality(year_nx_graph, centrality_measure)
        yearly_graph_centrality_data[year]["centrality_data"] = \
            build_centrality_data(year_graph_centrality)

    return yearly_graph_centrality_data

from coauthorship_centrality.utils import build_centrality_data, build_networkx_graph, compute_graph_node_centrality


def compute_year_graph_centrality(
    year_graph_data,
    centrality_measure,
    normalize,
    t_min,
    t_max
):
    year_nx_graph = build_networkx_graph(year_graph_data)

    year_graph_centrality = compute_graph_node_centrality(year_nx_graph, centrality_measure, normalize, t_min, t_max)

    year_graph_centrality_data = year_graph_data.copy()
    year_graph_centrality_data["centrality_data"] = build_centrality_data(year_graph_centrality)

    return year_graph_centrality_data

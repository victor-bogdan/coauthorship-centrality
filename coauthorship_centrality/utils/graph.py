from networkx import Graph, closeness_centrality, betweenness_centrality, degree, pagerank
from pandas import DataFrame


def build_networkx_graph(graph_data):
    graph = Graph()

    for node in graph_data['nodes']:
        graph.add_node(node['id'])

    for link in graph_data['links']:
        graph.add_edge(link['source'], link['target'])

    return graph


def compute_graph_node_centrality(nx_graph, centrality_measure, normalize, t_min, t_max):
    if centrality_measure.lower() == "closeness":
        centrality_values = closeness_centrality(nx_graph)
    elif centrality_measure.lower() == "betweenness":
        centrality_values = betweenness_centrality(nx_graph)
    elif centrality_measure.lower() == "degree":
        year_degree_centrality = {}
        degree_view = degree(nx_graph)
        for degree_tuple in degree_view:
            year_degree_centrality[degree_tuple[0]] = degree_tuple[1]
        centrality_values = year_degree_centrality
    elif centrality_measure.lower() == "pagerank":
        centrality_values = pagerank(nx_graph)
    else:
        centrality_values = closeness_centrality(nx_graph)

    if normalize:
        return graph_node_centrality_min_max_normalization(centrality_values, t_min, t_max)
    else:
        return centrality_values


def graph_node_centrality_min_max_normalization(centrality_values, t_min, t_max):
    df = DataFrame(centrality_values.items(), columns=['node_id', 'centrality_value'])
    df['centrality_value'] = (df['centrality_value'] - df['centrality_value'].min()) / \
                             (df['centrality_value'].max() - df['centrality_value'].min()) * \
                             (t_max - t_min) + t_min
    return dict(df.values)

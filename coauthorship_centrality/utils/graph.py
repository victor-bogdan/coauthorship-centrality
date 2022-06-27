from networkx import Graph, closeness_centrality, betweenness_centrality, degree, pagerank


def build_networkx_graph(graph_data):
    graph = Graph()

    for node in graph_data['nodes']:
        graph.add_node(node['id'])

    for link in graph_data['links']:
        graph.add_edge(link['source'], link['target'])

    return graph


def compute_graph_node_centrality(nx_graph, centrality_measure):
    if centrality_measure.lower() == "closeness":
        return closeness_centrality(nx_graph)
    elif centrality_measure.lower() == "betweenness":
        return betweenness_centrality(nx_graph)
    elif centrality_measure.lower() == "degree":
        year_degree_centrality = {}
        degree_view = degree(nx_graph)
        for degree_tuple in degree_view:
            year_degree_centrality[degree_tuple[0]] = degree_tuple[1]
        return year_degree_centrality
    elif centrality_measure.lower() == "pagerank":
        return pagerank(nx_graph)

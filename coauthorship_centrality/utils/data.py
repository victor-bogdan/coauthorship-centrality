
def build_centrality_data(node_centrality_values):
    nodes_centrality_data = []

    for node_id, node_centrality_value in node_centrality_values.items():
        nodes_centrality_data.append({
            "node_id": node_id,
            "node_data": {
                "centrality": node_centrality_value
            }
        })

    return nodes_centrality_data

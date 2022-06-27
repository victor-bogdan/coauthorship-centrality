from coauthorship_centrality.core.centrality.yearly_accumulative_centrality import compute_yearly_accumulative_graph_centrality
from coauthorship_centrality.core.centrality.yearly_centrality import compute_yearly_graph_centrality

CENTRALITY_MEASURES = ["closeness", "betweenness", "degree", "pagerank"]
YEAR_PERIOD_TYPES = ["yearly", "yearly_accumulative"]
LAYER_NODE_TYPES = ["default", "group"]


class CoauthorshipCentralityAnalyzer:

    def get_coauthorship_centrality(
            self,
            yearly_graph_data,
            centrality_measure,
            year_period_type,
            layer_node_type
    ):
        if year_period_type == "yearly":
            yearly_analysis_data = compute_yearly_graph_centrality(yearly_graph_data, centrality_measure)
            return yearly_analysis_data
        else:
            yearly_accumulative_analysis_data = compute_yearly_accumulative_graph_centrality(
                yearly_graph_data, centrality_measure, layer_node_type)
            return yearly_accumulative_analysis_data


class DBLPCoauthorshipCentralityAnalyzer:
    pass

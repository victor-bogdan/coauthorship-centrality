from ..core.centrality.yearly_accumulative_centrality import \
    compute_yearly_accumulative_graph_centrality
from ..core.centrality.year_centrality import compute_year_graph_centrality

CENTRALITY_MEASURES = ["closeness", "betweenness", "degree", "pagerank"]
LAYER_NODE_TYPES = ["default", "group"]


class CoauthorshipCentralityAnalyzer:

    def get_year_coauthorship_centrality(
            self,
            year_graph_data,
            centrality_measure,
            layer_node_type
    ):
        yearly_analysis_data = compute_year_graph_centrality(year_graph_data, centrality_measure, layer_node_type)
        return yearly_analysis_data

    def get_yearly_accumulative_coauthorship_centrality(
            self,
            yearly_graph_data,
            centrality_measure,
            layer_node_type
    ):
        yearly_accumulative_analysis_data = compute_yearly_accumulative_graph_centrality(
            yearly_graph_data, centrality_measure, layer_node_type)
        return yearly_accumulative_analysis_data


class DBLPCoauthorshipCentralityAnalyzer:
    pass

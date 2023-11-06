from coauthorship_centrality.core import compute_yearly_accumulative_graph_centrality, compute_year_graph_centrality, \
    DBLPDataParser

CENTRALITY_MEASURES = ["closeness", "betweenness", "degree", "pagerank"]
DATA_TYPES = ["authors", "collaborator_groups"]
LAYER_NODE_TYPES = ["default", "group"]


class CoauthorshipCentralityAnalyzer:

    def get_year_coauthorship_centrality(
        self,
        year_graph_data,
        centrality_measure,
        data_type,
        normalize=False,
        t_min=0,
        t_max=1
    ):
        yearly_analysis_data = compute_year_graph_centrality(
            year_graph_data, centrality_measure, normalize, t_min, t_max)
        return yearly_analysis_data

    def __get_year_layer_node_type(
        self,
        data_type
    ):
        if data_type == "authors":
            return "default"
        elif data_type == "collaborator_groups":
            return "default"
        else:
            return "default"

    def get_yearly_accumulative_coauthorship_centrality(
        self,
        yearly_graph_data,
        centrality_measure,
        data_type,
        normalize=False,
        t_min=0,
        t_max=1
    ):
        layer_node_type = self.__get_yearly_accumulative_layer_node_type(data_type)
        yearly_accumulative_analysis_data = compute_yearly_accumulative_graph_centrality(
            yearly_graph_data, centrality_measure, layer_node_type, normalize, t_min, t_max)
        return yearly_accumulative_analysis_data

    def __get_yearly_accumulative_layer_node_type(self, data_type):
        if data_type == "authors":
            return "default"
        elif data_type == "collaborator_groups":
            return "group"
        else:
            return "default"


class DBLPCoauthorshipCentralityAnalyzer(CoauthorshipCentralityAnalyzer):

    def __init__(self):
        self._dblp_data_parser = DBLPDataParser()

    def get_year_coauthorship_centrality(
        self,
        dblp_year_graph_data,
        centrality_measure,
        data_type,
        normalize=False,
        t_min=0,
        t_max=1
    ):
        year_graph_data = self._dblp_data_parser.parse_dblp_year_graph_data(dblp_year_graph_data, data_type)
        return super().get_year_coauthorship_centrality(
            year_graph_data, centrality_measure, data_type, normalize, t_min, t_max)

    def get_yearly_accumulative_coauthorship_centrality(
        self,
        dblp_yearly_graph_data,
        centrality_measure,
        data_type,
        normalize=False,
        t_min=0,
        t_max=1
    ):
        yearly_graph_data = self._dblp_data_parser.parse_dblp_yearly_graph_data(dblp_yearly_graph_data, data_type)
        return super().get_yearly_accumulative_coauthorship_centrality(
            yearly_graph_data, centrality_measure, data_type, normalize, t_min, t_max)

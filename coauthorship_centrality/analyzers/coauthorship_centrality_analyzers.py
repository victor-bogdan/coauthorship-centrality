
CENTRALITY_MEASURES = ["betweenness", "closeness", "degree", "pagerank"]
ANALYSIS_TYPES = ["author", "collaborator_group"]
YEAR_PERIOD_TYPES = ["yearly", "yearly_accumulative"]


class CoauthorshipCentralityAnalyzer:

    def __init__(self):
        self._yearly_accumulative_analysis_data = {}

    def get_coauthorship_centrality(self, centrality_measure, analysis_type, end_year):
        pass

    def get_node_edges(self, analysis_type, end_year):
        pass

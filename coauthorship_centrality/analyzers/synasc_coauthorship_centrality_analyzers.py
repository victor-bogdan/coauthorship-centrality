from os.path import dirname
from glob import glob
from json import loads

from .coauthorship_centrality_analyzers import CoauthorshipCentralityAnalyzer


class SYNASCCoauthorshipCentralityAnalyzer(CoauthorshipCentralityAnalyzer):

    def __init__(self):
        super().__init__()
        self.__init_data()

    def __init_data(self):
        project_root_path = dirname(dirname(__file__))
        synasc_data_path = "{0}/resources/synasc_data".format(project_root_path)
        folder_path = "{0}/*.json".format(synasc_data_path)
        file_paths = [f for f in glob(folder_path)]

        for file_path in file_paths:
            with open(file_path, "r", encoding="utf-8-sig") as file:
                data = loads(file.read())
                self._yearly_accumulative_analysis_data[str(data['end_year'])] = data

    def get_coauthorship_centrality(self, centrality_measure, analysis_type, end_year):
        centrality_dict = {}

        if analysis_type == "author":
            for author_name, author_data in \
                    self._yearly_accumulative_analysis_data[end_year]['accumulative_authors'].items():
                if centrality_measure.lower() == "betweenness":
                    centrality_dict[author_name] = author_data['accumulative_author_betweenness_centrality']
                elif centrality_measure.lower() == "closeness":
                    centrality_dict[author_name] = author_data['accumulative_author_closeness_centrality']
                elif centrality_measure.lower() == "degree":
                    centrality_dict[author_name] = author_data['accumulative_author_degree_centrality']
                elif centrality_measure.lower() == "pagerank":
                    centrality_dict[author_name] = author_data['accumulative_author_pagerank_centrality']
        elif analysis_type == "collaborator_group":
            for collaborator_group_id, collaborator_group_data in \
                    self._yearly_accumulative_analysis_data[end_year]['accumulative_collaborator_groups'].items():
                if centrality_measure.lower() == "betweenness":
                    centrality_dict[collaborator_group_id] = \
                        collaborator_group_data['accumulative_collaborator_groups_betweenness_centrality']
                elif centrality_measure.lower() == "closeness":
                    centrality_dict[collaborator_group_id] = \
                        collaborator_group_data['accumulative_collaborator_groups_closeness_centrality']
                elif centrality_measure.lower() == "degree":
                    centrality_dict[collaborator_group_id] = \
                        collaborator_group_data['accumulative_collaborator_groups_degree_centrality']
                elif centrality_measure.lower() == "pagerank":
                    centrality_dict[collaborator_group_id] = \
                        collaborator_group_data['accumulative_collaborator_groups_pagerank_centrality']

        return centrality_dict

    def get_node_edges(self, analysis_type, end_year):
        if analysis_type == "author":
            return self._yearly_accumulative_analysis_data[end_year]['accumulative_author_links']
        elif analysis_type == "collaborator_group":
            return self._yearly_accumulative_analysis_data[end_year]['accumulative_collaborator_group_links']

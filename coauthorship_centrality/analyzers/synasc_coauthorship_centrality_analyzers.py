from os.path import dirname
from glob import glob
from json import loads
from types import SimpleNamespace

from .coauthorship_centrality_analyzers import CoauthorshipCentralityAnalyzer


class SYNASCCoauthorshipCentralityAnalyzer(CoauthorshipCentralityAnalyzer):

    def __init__(self):
        super().__init__()
        self.__yearly_accumulative_analysis_data_list = []
        self.__init_data()

    def __init_data(self):
        project_root_path = dirname(dirname(__file__))
        synasc_data_path = "{0}/resources/synasc_data".format(project_root_path)
        folder_path = "{0}/*.json".format(synasc_data_path)
        file_paths = [f for f in glob(folder_path)]

        for file_path in file_paths:
            with open(file_path, "r", encoding="utf-8-sig") as file:
                data = file.read()
                self.__yearly_accumulative_analysis_data_list.append(
                    loads(data, object_hook=lambda d: SimpleNamespace(**d)))

    def get_coauthorship_centrality(self, centrality_measure):
        if centrality_measure.lower() == "betweenness":
            pass
        elif centrality_measure.lower() == "closeness":
            pass
        elif centrality_measure.lower() == "degree":
            pass
        elif centrality_measure.lower() == "pagerank":
            pass
        else:
            pass

    def get_authors_graph(self):
        pass

    def get_collaborator_groups_graph(self):
        pass

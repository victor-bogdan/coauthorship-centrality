from os.path import join, abspath, curdir
from json import loads

from coauthorship_centrality import CoauthorshipCentralityAnalyzer

AUTHORS_DATA_PATH = "resources/synasc_data/authors/SYNASC_{0}_author_graph_data.json"
COLLABORATOR_GROUPS_DATA_PATH = \
    "resources/synasc_data/collaborator_groups/SYNASC_{0}_collaborator_group_graph_data.json"


def test_year_coauthorship_centrality(year, centrality_measure, layer_node_type, data_type, data_path):
    root_path = abspath(curdir)

    path_string = join(root_path, data_path.format(year))

    with open(path_string, "r", encoding="utf-8-sig") as file:
        year_graph_data = loads(file.read())

        coauthorship_centrality_analyzer = CoauthorshipCentralityAnalyzer()
        year_coauthorship_centrality_data = coauthorship_centrality_analyzer.\
            get_year_coauthorship_centrality(year_graph_data, centrality_measure, layer_node_type, data_type)

        sorted_list = sorted(
            year_coauthorship_centrality_data['centrality_data'],
            key=lambda d: d['node_data']['centrality'],
            reverse=True
        )

        print(["{0} - {1}".format(node['node_id'], node['node_data']['centrality']) for node in sorted_list[0:10]])


def test_yearly_accumulative_coauthorship_centrality(
        start_year,
        end_year,
        centrality_measure,
        layer_node_type,
        data_type,
        data_path
):
    yearly_graph_data = {}

    root_path = abspath(curdir)

    for year in range(start_year, end_year + 1):
        path_string = join(root_path, data_path.format(year))

        with open(path_string, "r", encoding="utf-8-sig") as file:
            data = loads(file.read())
            yearly_graph_data[year] = data

    coauthorship_centrality_analyzer = CoauthorshipCentralityAnalyzer()
    yearly_accumulative_coauthorship_centrality_data = coauthorship_centrality_analyzer.\
        get_yearly_accumulative_coauthorship_centrality(yearly_graph_data, centrality_measure,
                                                        layer_node_type, data_type, True, 1, 10)

    sorted_list = sorted(
        yearly_accumulative_coauthorship_centrality_data['centrality_data'],
        key=lambda d: d['node_data']['centrality'],
        reverse=True
    )

    print(["{0} - {1}".format(node['node_id'], node['node_data']['centrality']) for node in sorted_list[0:10]])


if __name__ == "__main__":
    test_year_coauthorship_centrality(2009, "betweenness", "default", "authors", AUTHORS_DATA_PATH)
    test_yearly_accumulative_coauthorship_centrality(2005, 2009, "closeness", "default", "authors", AUTHORS_DATA_PATH)

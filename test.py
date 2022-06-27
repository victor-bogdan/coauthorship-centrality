from os.path import dirname
from json import loads

from coauthorship_centrality import CoauthorshipCentralityAnalyzer

if __name__ == "__main__":

    yearly_graph_data = {}

    dirname = dirname(__file__)

    for year in range(2005, 2022):
        path_string = "{0}/coauthorship_centrality/resources/synasc_data/collaborator_groups/SYNASC_{1}_collaborator_group_graph_data.json".format(
            dirname, year)

        with open(path_string, "r", encoding="utf-8-sig") as file:
            data = loads(file.read())
            yearly_graph_data[year] = data

    a = CoauthorshipCentralityAnalyzer()
    years_accumulative_analysis_data = a.get_coauthorship_centrality(
        yearly_graph_data, "degree", "yearly_accumulative", "group")

    #print(years_accumulative_analysis_data[2005]['centrality_data'])

    sorted_list = sorted(
        years_accumulative_analysis_data[2021]['centrality_data'],
        key=lambda d: d['node_data']['centrality'], reverse=True
    )

    print(sorted_list)

#{0}/coauthorship_centrality/resources/synasc_data/authors/SYNASC_{1}_author_graph_data.json"
#{0}/coauthorship_centrality/resources/synasc_data/collaborator_groups/SYNASC_{1}_collaborator_group_graph_data.json"


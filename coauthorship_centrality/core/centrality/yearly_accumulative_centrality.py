from itertools import combinations
from networkx import Graph, compose

from coauthorship_centrality.utils.data import build_centrality_data
from coauthorship_centrality.utils.graph import build_networkx_graph, compute_graph_node_centrality


def compute_yearly_accumulative_graph_centrality(yearly_graph_data, centrality_measure, layer_node_type):
    if layer_node_type == "default":
        return compute_default_yearly_accumulative_graph_centrality(yearly_graph_data, centrality_measure)
    elif layer_node_type == "group":
        return compute_group_yearly_accumulative_graph_centrality(yearly_graph_data, centrality_measure)
    else:
        return compute_default_yearly_accumulative_graph_centrality(yearly_graph_data, centrality_measure)


def compute_default_yearly_accumulative_graph_centrality(yearly_graph_data, centrality_measure):
    yearly_accumulative_graph_centrality_data = {}

    yearly_nx_graphs = {}
    for year, year_data in yearly_graph_data.items():
        yearly_nx_graphs[year] = build_networkx_graph(year_data)

    years = list(yearly_graph_data.keys())
    years.sort()

    for end_year in years:

        yearly_accumulative_graph_centrality_data[end_year] = {}

        accumulative_nx_graph = Graph()

        for year in range(years[0], end_year + 1):
            accumulative_nx_graph = compose(accumulative_nx_graph, yearly_nx_graphs[year])

        yearly_accumulative_graph_centrality_data[end_year]['nodes'] = accumulative_nx_graph.nodes

        temp_links = []
        for node in accumulative_nx_graph.nodes:
            temp_links = temp_links + list(accumulative_nx_graph.edges(node))
        yearly_accumulative_graph_centrality_data[end_year]['links'] = set([tuple(sorted(i)) for i in temp_links])

        year_accumulative_graph_centrality = compute_graph_node_centrality(accumulative_nx_graph, centrality_measure)
        yearly_accumulative_graph_centrality_data[end_year]["centrality_data"] = \
            build_centrality_data(year_accumulative_graph_centrality)

    return yearly_accumulative_graph_centrality_data


def compute_group_yearly_accumulative_graph_centrality(yearly_graph_data, centrality_measure):
    yearly_accumulative_centrality_centrality_data = {}

    years = list(yearly_graph_data.keys())
    years.sort()

    for end_year in years:

        yearly_accumulative_centrality_centrality_data[end_year] = {}

        accumulative_group_nodes = {}
        for year in range(years[0], end_year + 1):
            for node_data in yearly_graph_data[year]['nodes']:
                if node_data['id'] not in accumulative_group_nodes:
                    accumulative_group_nodes[node_data['id']] = {
                        "id": node_data['id'],
                        "members": set(node_data['members'])
                    }

        accumulative_group_links = build_node_groups_links(accumulative_group_nodes)

        accumulative_graph = {"nodes": list(accumulative_group_nodes.values()), "links": accumulative_group_links}

        accumulative_nx_graph = build_networkx_graph(accumulative_graph)

        yearly_accumulative_centrality_centrality_data[end_year]['nodes'] = accumulative_nx_graph.nodes

        temp_links = []
        for node in accumulative_nx_graph.nodes:
            temp_links = temp_links + list(accumulative_nx_graph.edges(node))
        yearly_accumulative_centrality_centrality_data[end_year]['links'] = set([tuple(sorted(i)) for i in temp_links])

        year_closeness_centrality = compute_graph_node_centrality(accumulative_nx_graph, centrality_measure)
        yearly_accumulative_centrality_centrality_data[end_year]["centrality_data"] = \
            build_centrality_data(year_closeness_centrality)

    return yearly_accumulative_centrality_centrality_data


def build_node_groups_links(node_groups):
    collaborator_groups_links_set = set()
    links_list = []

    for first_collaborator_group_id, first_collaborator_group in node_groups.items():
        for second_collaborator_group_id, second_collaborator_group in node_groups.items():
            if first_collaborator_group_id == second_collaborator_group_id:
                continue

            first_collaborator_group_authors_set = set(first_collaborator_group['members'])
            second_collaborator_group_authors_set = set(second_collaborator_group['members'])

            if len(first_collaborator_group_authors_set.intersection(second_collaborator_group_authors_set)) > 0:
                for collaborator_group_link in combinations([
                    first_collaborator_group_id,
                    second_collaborator_group_id],
                    2
                ):
                    left_right = "{0} - {1}".format(collaborator_group_link[0], collaborator_group_link[1])
                    right_left = "{0} - {1}".format(collaborator_group_link[1], collaborator_group_link[0])

                    if left_right not in collaborator_groups_links_set and right_left not in collaborator_groups_links_set:
                        collaborator_groups_links_set.add(left_right)
                        links_list.append({"source": collaborator_group_link[0], "target": collaborator_group_link[1]})

    return links_list

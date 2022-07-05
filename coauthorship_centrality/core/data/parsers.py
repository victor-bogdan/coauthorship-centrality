from hashlib import sha256
from itertools import combinations


class DBLPDataParser:

    def parse_dblp_year_graph_data(self, dblp_year_graph_data, data_type):
        if data_type == "authors":
            return self.dblp_year_graph_authors_data(dblp_year_graph_data)
        elif data_type == "collaborator_groups":
            self.dblp_year_graph_collaborator_groups_data(dblp_year_graph_data)
        else:
            self.dblp_year_graph_authors_data(dblp_year_graph_data)

    def dblp_year_graph_authors_data(self, dblp_year_graph_data):
        authors = {}
        author_links_set = set()
        author_links = []

        for publication in dblp_year_graph_data:

            try:
                # Validate #
                if publication['authors'] is None:
                    continue

                # Create Dicts #
                for author_name in publication['authors']:
                    if author_name not in authors:
                        authors[author_name] = {"id": author_name}

                for author_link in combinations(publication['authors'], 2):
                    sorted_author_link = tuple(sorted(author_link))
                    if sorted_author_link not in author_links_set:
                        author_links_set.add(sorted_author_link)
                        author_links.append({"source": sorted_author_link[0], "target": sorted_author_link[1]})
            except:
                continue

        return {"nodes": authors.values(), "links": author_links.copy()}

    def dblp_year_graph_collaborator_groups_data(self, dblp_year_graph_data):
        collaborator_groups = {}

        for publication in dblp_year_graph_data:

            try:
                # Validate #
                if publication['authors'] is None:
                    continue

                # Create Dicts #

                sorted_author_list = list(publication['authors'])
                sorted_author_list.sort()

                authors_concatenated_name = ""
                for author in sorted_author_list[:-1]:
                    authors_concatenated_name += "{0} ".format(author)
                authors_concatenated_name += sorted_author_list[-1]

                first_sorted_author_name_list = sorted_author_list[0].split(' ')
                first_sorted_author_abbreviated_name = ""
                for name in first_sorted_author_name_list:
                    first_sorted_author_abbreviated_name += name[0]

                collaborator_group_id = "{0}-{1}".format(
                    first_sorted_author_abbreviated_name,
                    sha256(authors_concatenated_name.encode('ascii')).hexdigest()[:4].upper())

                if collaborator_group_id not in collaborator_groups:
                    collaborator_groups[collaborator_group_id] = {
                        "id": collaborator_group_id,
                        "members": sorted_author_list,
                    }
            except:
                continue

        collaborator_group_links = self.build_collaborator_groups_links(collaborator_groups)

        return {"nodes": collaborator_groups.values(), "links": collaborator_group_links.copy()}

    def build_collaborator_groups_links(self, collaborator_groups):
        collaborator_group_links_set = set()
        collaborator_group_links = []

        for first_collaborator_group_id, first_collaborator_group in collaborator_groups.items():
            for second_collaborator_group_id, second_collaborator_group in collaborator_groups.items():
                if first_collaborator_group_id == second_collaborator_group_id:
                    continue

                first_collaborator_group_authors_set = set(first_collaborator_group['authors'])
                second_collaborator_group_authors_set = set(second_collaborator_group['authors'])

                if len(first_collaborator_group_authors_set.intersection(second_collaborator_group_authors_set)) > 0:
                    for collaborator_group_link in combinations(
                        [first_collaborator_group_id, second_collaborator_group_id],
                        2
                    ):
                        sorted_collaborator_group_link = tuple(sorted(collaborator_group_link))
                        if sorted_collaborator_group_link not in collaborator_group_links_set:
                            collaborator_group_links_set.add(sorted_collaborator_group_link)
                            collaborator_group_links.append(
                                {
                                    "source": sorted_collaborator_group_link[0],
                                    "target": sorted_collaborator_group_link[1]
                                }
                            )

        return collaborator_group_links

    def parse_dblp_yearly_graph_data(self, dblp_year_graph_data, data_type):
        yearly_graph_data = {}

        for year, year_data in dblp_year_graph_data.items():
            yearly_graph_data[year] = self.parse_dblp_year_graph_data(year_data, data_type)

        return yearly_graph_data



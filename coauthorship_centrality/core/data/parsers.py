from itertools import combinations


class DBLPDataParser:

    def parse_dblp_year_graph_data(self, dblp_year_graph_data):
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
                    sorted_author_link = sorted(author_link)
                    if sorted_author_link not in author_links_set:
                        author_links_set.add(sorted_author_link)
                        author_links.append({"source": author_link[0], "target": author_link[1]})
            except:
                continue

        return {"nodes": authors.values(), "links": author_links.copy()}

    def parse_dblp_yearly_graph_data(self, dblp_year_graph_data):
        yearly_graph_data = {}

        for year, year_data in dblp_year_graph_data.items():
            yearly_graph_data[year] = self.parse_dblp_year_graph_data(year_data)

        return yearly_graph_data

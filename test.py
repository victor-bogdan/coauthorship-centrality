from coauthorship_centrality import SYNASCCoauthorshipCentralityAnalyzer

if __name__ == "__main__":
    a = SYNASCCoauthorshipCentralityAnalyzer()
    a.get_coauthorship_centrality("degree", "author", "2010", "yearly")

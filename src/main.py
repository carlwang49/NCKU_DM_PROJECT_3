import argparse
from utility.utils import initialize_graph_from_file
from HITS import run_hits_algorithm
from sim_rank import sim_rank
from page_rank import page_rank


def main():
    # Use argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description="Graph Algorithms")
    parser.add_argument(
        "algorithm",
        choices=["hits", "simrank", "pagerank"],
        help="Select the algorithm to run",
    )
    parser.add_argument("--graph-file", required=True, help="Path to the graph file")
    parser.add_argument(
        "--decay-factor", type=float, help="Decay factor for the SimRank algorithm"
    )
    parser.add_argument(
        "--iterations", type=int, help="Number of iterations for the algorithm"
    )

    args = parser.parse_args()

    # Initialize the graph
    graph = initialize_graph_from_file(args.graph_file)

    if args.algorithm == "hits":
        # Run the HITS algorithm
        num_iterations = args.iterations or 100
        run_hits_algorithm(graph, num_iterations)

        # Retrieve and print authority and hub values
        auth_list, hub_list = graph.get_authority_hub_lists()
        print("Authority values:", auth_list)
        print("Hub values:", hub_list)

    elif args.algorithm == "simrank":
        # Run the SimRank algorithm
        decay_factor = args.decay_factor or 0.7
        iterations = args.iterations or 30
        simrank_result = sim_rank(graph, decay_factor, iterations)
        print("SimRank Result:", simrank_result)

    elif args.algorithm == "pagerank":
        # Run the PageRank algorithm
        iteration = args.iterations or 30
        damping_factor = 0.1
        page_rank(graph, damping_factor, iteration)
        print(graph.get_pagerank())


if __name__ == "__main__":
    main()

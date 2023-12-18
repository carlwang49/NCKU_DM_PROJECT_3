import argparse
from utility.utils import initialize_graph_from_file
from HITS import run_hits_algorithm
from sim_rank import sim_rank
from page_rank import page_rank
import numpy as np
import os

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
    graph_file_base_name = os.path.splitext(os.path.basename(args.graph_file))[0]
    results_dir = f'../results/{graph_file_base_name}'

    # Initialize the graph
    graph = initialize_graph_from_file(args.graph_file)

    if args.algorithm == "pagerank":
        # Run the PageRank algorithm
        iteration = args.iterations or 30
        damping_factor = 0.1
        page_rank(graph, damping_factor, iteration)
        pagerank_result = graph.get_pagerank()

        # Print to STDOUT
        print("PageRank:")
        print("[", end="")
        print(" ".join(f"{value:.3f}" for value in pagerank_result), end="]\n")

        # Save to PageRank.txt
        np.savetxt(
            os.path.join(results_dir, f"{graph_file_base_name}_PageRank.txt"),
            pagerank_result.reshape(1, -1),  # Reshape to a 1D array
            fmt="%#.3f",
            delimiter=" ",
            newline="",
        )


    elif args.algorithm == "hits":
        # Run the HITS algorithm
        iteration = args.iterations or 30
        run_hits_algorithm(graph, iteration)

        # Retrieve and print authority and hub values
        auth_list, hub_list = graph.get_authority_hub_lists()

        # Convert to NumPy arrays
        auth_array = np.array(auth_list)
        hub_array = np.array(hub_list)

        # Print to STDOUT
        print("Authority:")
        print("[", end="")
        print(" ".join(f"{value:.3f}" for value in auth_array), end="]\n")
        print("Hub:")
        print("[", end="")
        print(" ".join(f"{value:.3f}" for value in hub_array), end="]\n")

        # Save to HITS_authority.txt and HITS_hub.txt
        np.savetxt(
            os.path.join(results_dir, f"{graph_file_base_name}_HITS_authority.txt"),
            auth_array.reshape(1, -1),  # Reshape to a 1D array
            fmt="%#.3f",
            delimiter=" ",
            newline="",
        )
        np.savetxt(
            os.path.join(results_dir, f"{graph_file_base_name}_HITS_hub.txt"),
            hub_array.reshape(1, -1),  # Reshape to a 1D array
            fmt="%#.3f",
            delimiter=" ",
            newline="",
        )



    elif args.algorithm == "simrank":
        # Run the SimRank algorithm
        decay_factor = args.decay_factor or 0.7
        iteration = args.iterations or 30
        simrank_result = sim_rank(graph, decay_factor, iteration)

        # Print to STDOUT
        print("Decay Factor:")
        print(decay_factor)
        print("SimRank:")
        print(simrank_result)

        # Save to SimRank.txt without newlines between rows
        np.savetxt(
            os.path.join(results_dir, f"{graph_file_base_name}_SimRank.txt"),
            simrank_result,
            fmt="%.3f",  # Format as floating point with 4 decimal places
            delimiter=' '  # Separate numbers with spaces
        )


if __name__ == "__main__":
    main()

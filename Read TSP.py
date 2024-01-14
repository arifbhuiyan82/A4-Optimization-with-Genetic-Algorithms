import tsplib95

def read_tsp_file(file_path, output_file="output.txt"):
    try:
        problem = tsplib95.load(file_path)
        with open(output_file, 'w') as output:
            output.write(f"Problem Name: {problem.name}\n")
            output.write(f"Type: {problem.type}\n")
            output.write(f"Comment: {problem.comment}\n")
            output.write(f"Dimension: {problem.dimension}\n")
            output.write(f"Edge Weight Type: {problem.edge_weight_type}\n")
            output.write(f"Edge Weight Format: {problem.edge_weight_format}\n")
            output.write(f"Display Data Type: {problem.display_data_type}\n\n")

            node_coords = problem.node_coords
            if node_coords:
                output.write("Node Coordinates:\n")
                for node, coords in node_coords.items():
                    output.write(f"Node {node}: ({coords[0]}, {coords[1]})\n")

            edge_weights = problem.edge_weights
            if edge_weights:
                output.write("\nEdge Weights:\n")
                for edge, weight in edge_weights.items():
                    output.write(f"Edge {edge}: {weight}\n")

        print(f"Output written to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
file_path = "Qatar194.tsp"
read_tsp_file(file_path, output_file="output.txt")

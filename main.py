def print_hi(name):

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def generate_node(number_of_nodes: int):
    result = {
        "nodes": []
    }
    with open("./inputData/1.json", 'w'):
        for line in range(number_of_nodes):
            #TODO add extracting prompt from DB
            result["nodes"].append({"node_id": 1, "node_type": "planet"})
    return result






# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    final_result = generate_node(2)
    print(final_result)


import osmnx as ox
import networkx as nx
import json
import matplotlib
import matplotlib.pyplot as plt
import uuid
from collections import ChainMap

def get_data(place_name="Yorba Linda", node_nums=10):
    # place_name = "Yorba Linda"
    graph = ox.graph_from_place(place_name, network_type='all', simplify=False)
    G = nx.Graph(graph)
    nodes = G.nodes(data=True)
    edges = G.edges(data=True)

    # printing only first record

    for i, j in zip(nodes,edges):
        print(i)
        print(j)
        break

    data = []  # Initialize an empty list to store dictionaries
    data_details = []

    ctr = 0
    for i in nodes:
        if ctr > node_nums:
            break
        for j in edges:
            if j[0] == i[0]:
                if int(j[2]["length"]) > 50:
                    try:
                        print(ctr)
                        ctr += 1
                        # print(j[2]["name"])
                        # print(i[0], '->', j[1], ": ",j[2]["length"])

                        # new code
                        entry = {
                            "data": {
                                "id": i[0],
                                "image": "https://picsum",
                                "name": j[2]["name"]  # Or provide a meaningful name based on the iteration
                            }
                        }
                        data.append(entry)

                        detail_entry = {
                            "data": {
                                "source": i[0],
                                "target": j[1],
                                "label": f"{j[0]}-{j[1]}",
                                "distance": j[2]["length"],
                                "time": 0,
                                "id": uuid.uuid4()
                            }
                        }
                        data_details.append(detail_entry)

                    except:
                        continue

    # print(data)
    # print("\n")
    # print(data_details)

    # merged_dicts = [{"data": {**d1["data"], **d2["data"]}} for d1, d2 in zip(data, data_details)]
    json_data = data + data_details
    # json_data = json.dumps([{"data": merged_dicts}], indent=2)
    # print(json_data)
    print(json_data)
    return json_data
import { dijkstra_list, dijkstra_list_v2, dijkstra_min_heap } from "../DijkstraList";
import { list1 } from "./graph";

test("dijkstra via adj list", function () {
    expect(dijkstra_list(0, 6, list1)).toEqual([0, 1, 4, 5, 6]);
});

test("dijkstra v2 via adj list", function () {
    expect(dijkstra_list_v2(0, 6, list1)).toEqual([0, 1, 4, 5, 6]);
});

test("dijkstra via adj list and minheap", function () {
    expect(dijkstra_min_heap(0, 6, list1)).toEqual([0, 1, 4, 5, 6]);
});
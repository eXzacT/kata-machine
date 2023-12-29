import MinHeapTuple from "../MinHeapTuple";

test("min heap", function () {
    const heap = new MinHeapTuple();

    expect(heap.length).toEqual(0);

    heap.push({ node: 1, dist: 3 });
    heap.push({ node: 2, dist: 1 });
    expect(heap.pop()).toEqual({ node: 2, dist: 1 });
    expect(heap.length).toEqual(1);
    expect(heap.pop()).toEqual({ node: 1, dist: 3 });
    expect(heap.length).toEqual(0);
    heap.push({ node: 69, dist: 69 });
    heap.push({ node: 420, dist: 420 });
    heap.push({ node: 4, dist: 4 });
    heap.push({ node: 1, dist: 1 });
    heap.push({ node: 8, dist: 8 });
    heap.push({ node: 7, dist: 7 });

    expect(heap.length).toEqual(6);
    expect(heap.pop()).toEqual({ node: 1, dist: 1 });
    expect(heap.pop()).toEqual({ node: 4, dist: 4 });
    expect(heap.length).toEqual(4);
    expect(heap.data.length).toEqual(4);
    expect(heap.pop()).toEqual({ node: 7, dist: 7 });
    expect(heap.pop()).toEqual({ node: 8, dist: 8 });
    expect(heap.pop()).toEqual({ node: 69, dist: 69 });
    expect(heap.pop()).toEqual({ node: 420, dist: 420 });
    expect(heap.length).toEqual(0);
});



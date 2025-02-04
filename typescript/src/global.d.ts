declare type Point = {
    x: number;
    y: number;
}

declare type ListNode<T> = {
    value: T,
    nxt?: ListNode<T>,
    prev?: ListNode<T>,
}

declare interface List<T> {
    get length(): number;
    removeAt(index: number): T | undefined;
    remove(item: T): T | undefined;
    get(index: number): T | undefined;
    prepend(item: T): void;
    append(item: T): void;
    insertAt(item: T, idx: number): void;
    reverse(): void;
    reverseRec(): void;
    deleteRec(): void;
}

declare type CompleteGraphEdge = { from: number; to: number; weight: number };
declare type GraphEdge = { to: number; weight: number };
declare type WeightedAdjacencyList = GraphEdge[][];
declare type WeightedAdjacencyMatrix = number[][]; // A number means weight
declare type HeapNode = { node: number; dist: number };

declare type AdjacencyList = number[][];
declare type AdjacencyMatrix = number[][]; // A 1 means connected

declare type BinaryNode<T> = {
    value: T;
    left: BinaryNode<T> | null;
    right: BinaryNode<T> | null;
};

declare type GeneralNode<T> = {
    value: T;
    children: GeneralNode<T>[];
};

declare interface ILRU<K, V> {
    update(key: K, value: V): void;
    get(key: K): V | undefined;
}

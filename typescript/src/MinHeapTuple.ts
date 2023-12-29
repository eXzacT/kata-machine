declare type HeapNode = { node: number; dist: number };
export default class MinHeap {
    public length: number;
    public data: HeapNode[];

    constructor() {
        this.length = 0;
        this.data = [];
    }

    private parent(idx: number): number {
        return Math.floor((idx - 1) / 2);
    }

    private leftChild(idx: number): number {
        return idx * 2 + 1;
    }

    private rightChild(idx: number): number {
        return idx * 2 + 2;
    }

    private heapifyUp(idx: number): void {
        if (idx === 0) {
            return;
        }

        const p = this.parent(idx);
        const pNode = this.data[p];
        const currNode = this.data[idx];

        if (currNode.dist < pNode.dist) {
            [this.data[p], this.data[idx]] = [currNode, pNode];
            this.heapifyUp(p);
        }
    }

    private heapifyDown(idx: number): void {
        const lIdx = this.leftChild(idx);
        const rIdx = this.rightChild(idx);

        //Reached the end
        if (lIdx >= this.length || rIdx >= this.length) {
            return;
        }

        const smallerChildIdx = this.data[lIdx].dist > this.data[rIdx].dist ? rIdx : lIdx;

        if (this.data[smallerChildIdx].dist < this.data[idx].dist) {
            [this.data[smallerChildIdx], this.data[idx]] = [this.data[idx], this.data[smallerChildIdx]];
            this.heapifyDown(smallerChildIdx);
        }
    }

    push(value: HeapNode): void {
        this.data.push(value);
        this.heapifyUp(this.length++);
    }

    pop(): HeapNode | null {
        if (this.length === 0) {
            return null;
        }
        const out = this.data[0];
        this.length--;

        if (this.length === 0) {
            this.data = [];
            return out;
        }

        this.data[0] = this.data.pop()!;
        this.heapifyDown(0);

        return out;
    }
}
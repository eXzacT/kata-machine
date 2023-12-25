export default class MinHeap {
    public length: number;
    public data: number[];

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
        const parentVal = this.data[p];
        const val = this.data[idx];

        if (val < parentVal) {
            [this.data[idx], this.data[p]] = [parentVal, val];
            this.heapifyUp(p);
        }
    }

    private heapifyDown(idx: number): void {
        const lIdx = this.leftChild(idx);
        const rIdx = this.rightChild(idx);

        if (lIdx >= this.length || rIdx >= this.length) {
            return;
        }

        const smallerChildIdx = this.data[lIdx] > this.data[rIdx] ? rIdx : lIdx;

        if (this.data[smallerChildIdx] < this.data[idx]) {
            [this.data[idx], this.data[smallerChildIdx]] = [this.data[smallerChildIdx], this.data[idx]];
            this.heapifyDown(smallerChildIdx);
        }
    }


    insert(value: number): void {
        this.data.push(value);
        this.heapifyUp(this.length++);
    }

    delete(): number {
        if (this.length === 0) {
            return -1;
        }

        const out = this.data[0];
        this.length--;

        if (this.length === 0) {
            this.data = [];
            return out;
        }

        this.data[0] = this.data[this.length];
        this.heapifyDown(0);

        return out;
    }
}
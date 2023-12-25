type Node<T> = {
    value: T;
    next?: Node<T>;
};

export default class Queue<T> {
    public length: number;
    private head?: Node<T> | undefined;
    private tail?: Node<T> | undefined;

    constructor() {
        this.head = this.tail = undefined;
        this.length = 0;
    }

    enqueue(item: T): void {
        this.length++;
        const node = { value: item } as Node<T>;
        if (!this.tail) {
            this.tail = this.head = node;
            return;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
    }

    deque(): T | undefined {
        if (!this.head) {
            return undefined;
        }
        // Edge case when we only have 1 item, so both head and tail point to it
        if (this.head == this.tail) {
            this.tail = undefined;
        }

        this.length--;

        const head = this.head;
        this.head = this.head.next;

        // unecessary
        head.next = undefined;

        return head.value;
    }
    peek(): T | undefined {
        return this.head?.value;
    }
}

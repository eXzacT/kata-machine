export default class DoublyLinkedList<T> {
    public length: number;
    private head: ListNode<T> | undefined;
    private tail: ListNode<T> | undefined;

    constructor() {
        this.length = 0;
        this.head = undefined;
        this.tail = undefined;
    }

    private createNode(
        item: T,
        prev?: ListNode<T>,
        nxt?: ListNode<T>,
    ): ListNode<T> {
        return { value: item, prev, nxt };
    }

    private getNodeAt(idx: number): ListNode<T> | undefined {
        if (idx < 0 || idx >= this.length) {
            throw new Error("Index out of bounds");
        }

        let curr: ListNode<T> | undefined;

        // If idx is in the first half of the list
        if (idx < this.length / 2) {
            curr = this.head;
            for (let i = 0; i < idx; i++) {
                curr = curr!.nxt;
            }
        }
        // If idx is in the second half of the list
        else {
            curr = this.tail;
            for (let i = this.length - 1; i > idx; i--) {
                curr = curr!.prev;
            }
        }

        return curr;
    }

    private removeNode(node: ListNode<T>): T {
        if (node.prev) {
            node.prev.nxt = node.nxt;
        } else {
            this.head = node.nxt; // Update head if removing the first node
        }

        if (node.nxt) {
            node.nxt.prev = node.prev;
        } else {
            this.tail = node.prev; // Update tail if removing the last node
        }

        this.length--;
        return node.value;
    }

    prepend(item: T): void {
        const node = this.createNode(item, undefined, this.head);
        if (this.head) {
            this.head.prev = node;
        } else {
            this.tail = node; // If list was empty, new node is also the tail
        }
        this.head = node;
        this.length++;
    }

    append(item: T): void {
        const node = this.createNode(item, this.tail, undefined);
        if (this.tail) {
            this.tail.nxt = node;
        } else {
            this.head = node; // If list was empty, new node is also the head
        }
        this.tail = node;
        this.length++;
    }

    insertAt(item: T, idx: number): void {
        if (idx < 0 || idx > this.length) {
            throw new Error("Index out of bounds");
        }

        if (idx === 0) {
            this.prepend(item);
            return;
        }

        if (idx === this.length) {
            this.append(item);
            return;
        }

        const prevNode = this.getNodeAt(idx - 1);
        const newNode = this.createNode(item, prevNode, prevNode!.nxt);
        prevNode!.nxt = newNode;
        newNode.nxt!.prev = newNode;

        this.length++;
    }

    remove(item: T): T | undefined {
        let curr = this.head;
        while (curr) {
            if (curr.value === item) {
                return this.removeNode(curr);
            }
            curr = curr.nxt;
        }
        return undefined;
    }

    get(idx: number): T | undefined {
        return this.getNodeAt(idx)?.value;
    }

    removeAt(idx: number): T | undefined {
        const nodeToRemove = this.getNodeAt(idx);
        if (nodeToRemove) {
            return this.removeNode(nodeToRemove);
        }
        return undefined;
    }
}

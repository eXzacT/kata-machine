export default class SinglyLinkedList<T> {
    public length: number;
    private head: ListNode<T> | undefined;

    constructor() {
        this.length = 0;
        this.head = undefined;
    }

    private createNode(item: T, nxt?: ListNode<T>): ListNode<T> {
        return { value: item, nxt };
    }

    private removeNxtOf(node: ListNode<T>): T {
        // Helper function to delete(skip) node passed here
        const toDelete = node.nxt;
        node.nxt = toDelete!.nxt;
        this.length--;

        return toDelete!.value;
    }

    private getNodeAt(idx: number): ListNode<T> | undefined {
        if (idx >= this.length || idx < 0) {
            throw new Error("Index out of bounds");
        }

        let curr = this.head;
        for (let i = 0; i < idx; i++) {
            curr = curr!.nxt;
        }
        return curr;
    }

    prepend(item: T): void {
        let node = this.createNode(item, this.head);
        this.head = node;
        this.length++;
    }

    append(item: T): void {
        let curr = this.head;
        const newNode = this.createNode(item);

        // When list is empty point the head to the appended node
        if (!curr) {
            this.head = newNode;
        } else {
            // Go to the end and change the next pointer to new node
            while (curr!.nxt) {
                curr = curr!.nxt;
            }
            curr!.nxt = newNode;
        }
        this.length++;
    }

    insertAt(item: T, idx: number): void {
        if (idx > this.length || idx < 0) {
            throw new Error("Index out of bounds");
        }

        // Edge case when we're inserting at the beginning
        if (idx === 0) {
            this.prepend(item);
            return;
        }

        const prevNode = this.getNodeAt(idx - 1);
        const newNode = this.createNode(item, prevNode!.nxt);
        prevNode!.nxt = newNode;
        this.length++;

    }

    remove(item: T): T | undefined {
        let curr = this.head;
        // List is empty
        if (!curr) {
            return undefined;
        }

        // Item to remove is the head
        if (curr.value === item) {
            return this.removeAt(0);
        }

        while (curr!.nxt) {
            if (curr!.nxt.value === item) {
                const deletedVal = this.removeNxtOf(curr);
                return deletedVal;
            }
            curr = curr!.nxt;
        }
        return undefined;
    }

    get(idx: number): T | undefined {
        return this.getNodeAt(idx)?.value;
    }

    removeAt(idx: number): T | undefined {
        if (idx < 0 || idx >= this.length) {
            throw new Error("Index out of bounds");
        }

        if (idx === 0) {
            const nodeToRemove = this.head;
            this.head = nodeToRemove?.nxt;
            this.length--;
            return nodeToRemove!.value;
        }

        const prevNode = this.getNodeAt(idx - 1);

        if (prevNode) {
            return this.removeNxtOf(prevNode);
        }
        return undefined;
    }

    reverse() {
        let prev = undefined;
        let curr = this.head;
        while (curr) {
            const tmp = curr.nxt
            curr.nxt = prev;
            [prev, curr] = [curr, tmp];
        }
        this.head = prev;
    }

    reverseRec() {
        function helper(curr: ListNode<T> | undefined, prev: ListNode<T> | undefined): ListNode<T> | undefined {
            if (!curr) {
                return prev;
            }
            const tmp = curr.nxt;
            curr.nxt = prev;
            return helper(tmp, curr);
        }
        this.head = helper(this.head, undefined);
    }
}
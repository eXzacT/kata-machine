export default class SinglyLinkedList<T> {
    private head: ListNode<T> | undefined
    public length: number

    constructor() {
        this.length = 0
    }

    private createNode(item: T, nxt?: ListNode<T>): ListNode<T> {
        return {
            value: item,
            nxt: nxt
        }
    }

    private deleteNxtOf(node: ListNode<T>): T {
        // Changing the curr next to be nexts next (09/11/2023)
        const toDelete = node.nxt
        node.nxt = toDelete!.nxt
        this.length--

        return toDelete!.value
    }

    private getNodeAt(idx: number): ListNode<T> | undefined {
        if (idx >= this.length || idx < 0) {
            throw new Error("Index out of bounds")
        }

        let curr = this.head;
        for (let i = 0; i < idx; i++) {
            curr = curr!.nxt
        }
        return curr
    }

    prepend(item: T): void {
        let node = this.createNode(item, this.head)
        this.head = node
        this.length++
    }

    insertAt(item: T, idx: number): void {
        if (idx > this.length || idx < 0) {
            throw new Error("Index out of bounds")
        }

        // Edge case when we're inserting at the beginning (09/11/2023)
        if (idx === 0) {
            this.prepend(item)
            return
        }

        const prevNode = this.getNodeAt(idx - 1)
        const newNode = this.createNode(item, prevNode!.nxt)
        prevNode!.nxt = newNode
        this.length++

    }

    append(item: T): void {
        let node = this.createNode(item)

        // When list is empty point the head to the appended node (09/11/2023)
        if (!this.head) {
            this.head = node
        } else {
            // Go to the end and change the next pointer to new node (09/11/2023)
            let current = this.getNodeAt(this.length - 1)
            current!.nxt = node
        }
        this.length++
    }

    remove(item: T): T | undefined {
        let curr = this.head
        // List is empty (09/11/2023)
        if (!curr) {
            return undefined
        }

        // Item to remove is the head (09/11/2023)
        if (curr.value === item) {
            return this.removeAt(0)
        }
        while (curr!.nxt) {
            if (curr!.nxt.value === item) {
                const deletedVal = this.deleteNxtOf(curr!.nxt)
                return deletedVal
            }
            curr = curr!.nxt
        }
        return undefined
    }

    get(idx: number): T | undefined {
        const node = this.getNodeAt(idx)

        return node ? node.value : undefined
    }

    removeAt(idx: number): T | undefined {
        if (idx < 0 || idx >= this.length) {
            throw new Error("Index out of bounds")
        }

        if (idx === 0) {
            const toRemove = this.head
            this.head = this.head?.nxt
            this.length--
            return toRemove!.value
        }

        const prevNode = this.getNodeAt(idx - 1)
        if (prevNode) {
            const deletedVal = this.deleteNxtOf(prevNode)
            return deletedVal
        }
        return undefined
    }
}
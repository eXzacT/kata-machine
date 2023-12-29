type Node<T> = {
    value: T;
    prev?: Node<T>;
    next?: Node<T>;
};

export default class LRU<K, V> {
    private length: number;
    private head?: Node<V>;
    private tail?: Node<V>;

    private lookup: Map<K, Node<V>>;
    private reverseLookup: Map<Node<V>, K>;

    constructor(private capacity: number = 10) {
        this.length = 0;
        this.lookup = new Map<K, Node<V>>();
        this.reverseLookup = new Map<Node<V>, K>();
    }

    update(key: K, value: V): void {
        let node = this.lookup.get(key);
        if (!node) {
            node = { value };
            this.length++;
            this.lookup.set(key, node);
            this.reverseLookup.set(node, key);
        } else {
            this.detach(node);
            node.value = value;
        }
        this.prepend(node);
        this.trimCache();
    }

    get(key: K): V | undefined {
        const node = this.lookup.get(key);
        if (!node) {
            return undefined;
        }

        this.detach(node);
        this.prepend(node);
        return node.value;
    }

    private detach(node: Node<V>): void {
        if (node === this.head) {
            this.head = node.next;
        }
        if (node === this.tail) {
            this.tail = node.prev;
        }
        if (node.prev) {
            node.prev.next = node.next;
        }
        if (node.next) {
            node.next.prev = node.prev;
        }
    }

    private prepend(node: Node<V>): void {
        if (!this.head) {
            this.head = this.tail = node;
        } else {
            node.next = this.head;
            this.head.prev = node;
            this.head = node;
        }
    }

    private trimCache(): void {
        if (this.length <= this.capacity) return;
        if (this.tail) {
            const key = this.reverseLookup.get(this.tail);
            this.lookup.delete(key!);
            this.reverseLookup.delete(this.tail);
            this.detach(this.tail);
            this.length--;
        }
    }
}
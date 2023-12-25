class TrieNode {
    children: { [key: string]: TrieNode };
    isEndOfWord: boolean;

    constructor() {
        this.children = {};
        this.isEndOfWord = false;
    }
}

export default class Trie {
    root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    insert(word: string): void {
        let current = this.root;
        for (const c of word) {
            if (!current.children[c]) {
                current.children[c] = new TrieNode();
            }
            current = current.children[c];
        }
        current.isEndOfWord = true;
    }

    find(prefix: string): string[] {
        let current = this.root;
        for (const char of prefix) {
            if (!current.children[char]) {
                return [];
            }
            current = current.children[char];
        }
        return this._findWords(current, prefix);
    }

    private _findWords(node: TrieNode, prefix: string): string[] {
        let results: string[] = [];
        if (node.isEndOfWord) {
            results.push(prefix);
        }
        for (const char in node.children) {
            results = results.concat(this._findWords(node.children[char], prefix + char));
        }
        return results;
    }

    delete(word: string): void {
        this._deleteNode(this.root, word, 0);
    }

    private _deleteNode(node: TrieNode, word: string, index: number): boolean {
        if (index === word.length) {
            if (!node.isEndOfWord) return false;
            node.isEndOfWord = false;
            return Object.keys(node.children).length === 0;
        }

        const char = word[index];
        const childNode = node.children[char];
        if (!childNode) {
            return false;
        }

        const shouldDeleteChild = this._deleteNode(childNode, word, index + 1);

        if (shouldDeleteChild) {
            delete node.children[char];
            return Object.keys(node.children).length === 0 && !node.isEndOfWord;
        }

        return false;
    }
}

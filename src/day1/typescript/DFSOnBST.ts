export function dfs_rec(head: BinaryNode<number>, needle: number): boolean {
    function helper(node: BinaryNode<number> | null): boolean {
        if (!node) {
            return false;
        }
        if (node.value === needle) {
            return true;
        }
        if (needle < node.value) {
            return helper(node.left);
        }

        return helper(node.right);
    }
    return helper(head);
}

export function dfs_iter(head: BinaryNode<number>, needle: number): boolean {
    const stack: [BinaryNode<number> | null] = [head];
    while (stack.length) {
        const node = stack.pop()
        if (!node) {
            continue
        }
        if (node.value == needle) {
            return true;
        }
        if (needle > node.value) {
            stack.push(node.right)
        }
        else {
            stack.push(node.left)
        }
    }
    return false;
}
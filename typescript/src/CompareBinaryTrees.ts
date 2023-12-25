export function compare_iter(a: BinaryNode<number> | null, b: BinaryNode<number> | null): boolean {
    const q1 = [a];
    const q2 = [b];

    while (q1.length === q2.length && q1.length > 0) {
        const node1 = q1.pop();
        const node2 = q2.pop();
        if (!node1 && !node2) {
            continue;
        }
        if (node1 !== node2) {
            return false;
        }
        q1.push(node1!.left)
        q2.push(node2!.left)
        q1.push(node1!.right)
        q2.push(node2!.right)
    }
    return true;
}

export function compare_rec(a: BinaryNode<number> | null, b: BinaryNode<number> | null): boolean {
    if (a && b && a.value === b.value) {
        return compare_rec(a.left, b.left) && compare_rec(a.right, b.right);
    }
    if (!a && !b) {
        return true;
    }
    return false;
}
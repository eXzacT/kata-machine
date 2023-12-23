export default function in_order_search(head: BinaryNode<number>): number[] {
    const path: number[] = [];

    function helper(node: BinaryNode<number> | null) {
        if (!node) {
            return;
        }
        helper(node.left);
        path.push(node.value);
        helper(node.right);
    }
    helper(head);
    return path;
}

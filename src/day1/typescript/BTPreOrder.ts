export default function pre_order_search(head: BinaryNode<number>): number[] {
    const path: number[] = [];

    function helper(node: BinaryNode<number> | null) {
        if (!node) {
            return;
        }
        path.push(node.value);
        helper(node.left);
        helper(node.right);
    }
    helper(head);
    return path;
}
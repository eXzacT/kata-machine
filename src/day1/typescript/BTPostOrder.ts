export default function post_order_search(head: BinaryNode<number>): number[] {
    const path: number[] = [];

    function helper(node: BinaryNode<number> | null) {
        if (!node) {
            return;
        }
        helper(node.left);
        helper(node.right);
        path.push(node.value);
    }
    helper(head);
    return path;
}
import Queue from "./Queue";

export function bfs_arr_q(head: BinaryNode<number>, needle: number): [boolean, number] {
    const arrQ: (BinaryNode<number> | null)[] = [head];
    let iterations = 0;
    while (arrQ.length) {
        const node = arrQ.shift();
        iterations++;
        if (node!.value === needle) {
            return [true, iterations];
        }
        if (node!.left) {
            arrQ.push(node!.left);
        }
        if (node!.right) {
            arrQ.push(node!.right);
        }
    }
    return [false, -1];
}

export function bfs_q(head: BinaryNode<number>, needle: number): [boolean, number] {
    const q: Queue<BinaryNode<number>> = new Queue<BinaryNode<number>>();
    q.enqueue(head);
    let iterations = 0;
    while (q.length) {
        const node = q.deque();
        iterations++;
        if (node!.value === needle) {
            return [true, iterations];
        }
        if (node!.left) {
            q.enqueue(node!.left);
        }
        if (node!.right) {
            q.enqueue(node!.right);
        }
    }
    return [false, -1];
}
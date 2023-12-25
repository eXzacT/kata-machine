function walk(maze: string[], wall: string, curr: Point, end: Point): Point[] {
    const HEIGHT = maze.length;
    const WIDTH = maze[0].length;
    const seen: boolean[][] = Array.from({ length: HEIGHT }, () => Array(WIDTH).fill(false));
    let path: Point[] = []

    function helper(curr: Point): boolean {
        if (curr.x < 0 || curr.x >= HEIGHT ||
            curr.y < 0 || curr.y >= WIDTH) {
            return false;
        }

        if (maze[curr.x][curr.y] === wall) {
            return false;
        }

        if (seen[curr.x][curr.y]) {
            return false;
        }

        if (curr.x === end.x && curr.y === end.y) {
            path.push(curr)
            return true
        }

        path.push(curr)
        seen[curr.x][curr.y] = true;
        for (let d of [[1, 0], [-1, 0], [0, -1], [0, 1]]) {
            const point: Point = { x: curr.x + d[0], y: curr.y + d[1] };
            if (helper(point)) {
                return true
            }
        }
        path.pop()
        return false
    }
    helper(curr);
    return path
}

export default function solve(maze: string[], wall: string, start: Point, end: Point): Point[] {
    return walk(maze, wall, start, end);
}
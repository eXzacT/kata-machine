export default function two_crystal_balls(breaks: boolean[]): number {
    const jump = Math.floor(Math.sqrt(breaks.length));
    let i = jump;

    for (; i < breaks.length; i += jump) {
        if (breaks[i]) {
            break;
        }
    }

    // After finding true jumping back by sqrt(n)
    i -= jump;

    // Start checking from the point we jumped back to, up to
    // and including the original truthy index
    for (let j = i; j < i + jump + 1 && j < breaks.length; j++)
        if (breaks[j]) return j;
    return -1;
}

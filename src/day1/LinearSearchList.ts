export default function linear_search(haystack: number[], needle: number): boolean {
    for (let idx = 0; idx < haystack.length; idx++) {
        if (haystack[idx] === needle)
            return true
    }
    return false
}
export default function two_crystal_balls(breaks: boolean[]): number {
    const jump = Math.floor(Math.sqrt(breaks.length))
    let i = jump
    for (;i<breaks.length;i+=jump)
        if (breaks[i])
            break
    
    // After finding true jumping back by sqrt(n) (06/11/2023)
    i-=jump

    // Then walking from that point until the previous jump (06/11/2023)
    for(let j=i; j<breaks.length && j<i+jump; j++)
        if (breaks[j])
            return j
    return -1
}
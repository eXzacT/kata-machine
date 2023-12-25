import two_crystal_balls from "../TwoCrystalBalls";

test("two crystal balls", function () {
    let idx = Math.floor(Math.random() * 10000);
    const data = new Array(10000).fill(false);

    for (let i = idx; i < 10000; ++i) {
        data[i] = true;
    }

    const data2 = new Array(10).fill(false)
    data2[9] = true

    const data3 = new Array(9).fill(false)
    data3[6] = true

    expect(two_crystal_balls(data)).toEqual(idx);
    expect(two_crystal_balls(new Array(821).fill(false))).toEqual(-1);
    expect(two_crystal_balls(data2)).toEqual(9);
    expect(two_crystal_balls(data3)).toEqual(6);
});


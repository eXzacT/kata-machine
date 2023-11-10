export function test_list(list: List<number>): void {
    list.append(5);
    list.append(7);
    list.append(9);

    expect(list.get(2)).toEqual(9);
    expect(list.removeAt(1)).toEqual(7);
    expect(list.length).toEqual(2);

    list.append(11);
    expect(list.get(2)).toEqual(11);
    expect(list.removeAt(1)).toEqual(9);
    expect(list.remove(9)).toEqual(undefined);
    expect(list.removeAt(0)).toEqual(5);
    expect(list.removeAt(0)).toEqual(11);
    expect(list.length).toEqual(0);

    list.prepend(5);
    list.prepend(7);
    list.prepend(9);

    expect(list.get(2)).toEqual(5);
    expect(list.get(0)).toEqual(9);
    expect(list.remove(9)).toEqual(9);
    expect(list.length).toEqual(2);
    expect(list.get(0)).toEqual(7);
    expect(list.remove(7)).toEqual(7);
    expect(list.removeAt(0)).toEqual(5);
    expect(list.length).toEqual(0);

    list.append(9);
    list.prepend(5);
    expect(() => list.get(5)).toThrowError("Index out of bounds");
    expect(list.get(0)).toEqual(5);
    expect(list.get(1)).toEqual(9);
    expect(list.removeAt(1)).toEqual(9);
    expect(list.removeAt(0)).toEqual(5);
    expect(() => list.removeAt(5)).toThrowError("Index out of bounds");
    expect(list.length).toEqual(0);
    list.append(9);
    list.append(5);
    list.insertAt(9, 2);
    expect(list.get(2)).toEqual(9);
    list.append(10);
    list.append(10);
    list.append(10);
    list.append(10);
    list.append(10);
    list.append(10);
    list.append(10);
    list.append(4);
    list.append(4);
    list.append(3);
    list.append(3);
    list.append(3);
    list.append(2);
    list.prepend(1);
    expect(list.get(0)).toEqual(1);
    list.append(7);
    expect(list.get(list.length - 1)).toEqual(7);
}

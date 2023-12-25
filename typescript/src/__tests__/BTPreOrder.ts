import pre_order from "../BTPreOrder";
import { tree } from "./tree";

test("Pre order search", function () {
    expect(pre_order(tree)).toEqual([
        20,
        10,
        5,
        7,
        15,
        50,
        30,
        29,
        45,
        100,
    ]);
});
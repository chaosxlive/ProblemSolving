// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

/**
 * @param {number} label
 * @return {number[]}
 */
var pathInZigZagTree = function (label) {
    const result = [label];
    while (true) {
        label >>= 1;
        if (label < 1) break;

        const level = Math.floor(Math.log2(label)) + 1;
        const end = Math.pow(2, level);
        const start = end / 2;
        label = end - 1 - label + start;
        result.push(label);
    }
    return result.reverse();
};
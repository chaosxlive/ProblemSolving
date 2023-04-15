// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
    const result = [];
    for (const [i, v] of arr.entries()) {
        result.push(fn(v, i));
    }
    return result;
};
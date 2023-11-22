// https://leetcode.com/problems/filter-elements-from-array/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
    const result = [];
    for (let [i, v] of arr.entries()) {
        if (fn(v, i)) {
            result.push(v);
        }
    }
    return result;
};
// https://leetcode.com/problems/chunk-array/

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function (arr, size) {
    const result = [];
    let idx = 0;
    while (true) {
        const chunk = arr.slice(idx, idx + size);
        if (chunk.length === 0) {
            return result;
        }
        result.push(chunk);
        idx += size;
    }
};
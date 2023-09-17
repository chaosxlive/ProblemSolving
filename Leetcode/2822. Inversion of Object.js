// https://leetcode.com/problems/inversion-of-object/

/**
 * @param {Object|Array} obj
 * @return {Object}
 */
var invertObject = function (obj) {
    const result = {};
    Object.entries(obj).forEach(([k, v]) => {
        if (result[v] === undefined) {
            result[v] = k;
        } else if (Array.isArray(result[v])) {
            result[v].push(k);
        } else {
            result[v] = [result[v], k];
        }
    });
    return result;
};
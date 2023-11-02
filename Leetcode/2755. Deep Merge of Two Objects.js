// https://leetcode.com/problems/deep-merge-of-two-objects/

/**
 * @param {null|boolean|number|string|Array|Object} obj1
 * @param {null|boolean|number|string|Array|Object} obj2
 * @return {null|boolean|number|string|Array|Object}
 */
var deepMerge = function (obj1, obj2) {
    if (Array.isArray(obj1) && Array.isArray(obj2)) {
        const l = Math.max(obj1.length, obj2.length);
        const result = [];
        for (let i = 0; i < l; i++) {
            if (i >= obj1.length) {
                result.push(obj2[i]);
            } else if (i >= obj2.length) {
                result.push(obj1[i]);
            } else {
                result.push(deepMerge(obj1[i], obj2[i]));
            }
        }
        return result;
    }
    if (Array.isArray(obj1) || Array.isArray(obj2)) {
        return obj2;
    }
    if (typeof obj1 === 'object' && typeof obj2 === 'object') {
        if (obj1 === null || obj2 === null) {
            return obj2;
        }
        const keys = [...new Set([...Object.keys(obj1), ...Object.keys(obj2)]).values()];
        const result = {};
        for (const k of keys) {
            if (obj1[k] === undefined) {
                result[k] = obj2[k];
            } else if (obj2[k] === undefined) {
                result[k] = obj1[k];
            } else {
                result[k] = deepMerge(obj1[k], obj2[k]);
            }
        }
        return result;
    }
    return obj2;
};

/**
 * let obj1 = {"a": 1, "c": 3}, obj2 = {"a": 2, "b": 2};
 * deepMerge(obj1, obj2); // {"a": 2, "c": 3, "b": 2}
 */

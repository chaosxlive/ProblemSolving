// https://leetcode.com/problems/compact-object/

/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {
    if (Array.isArray(obj)) {
        const result = [];
        for (const v of obj) {
            if (Boolean(v)) {
                if (typeof v === 'object') {
                    result.push(compactObject(v));
                } else {
                    result.push(v);
                }
            }
        }
        return result;
    } else {
        const result = {};
        for (const k in obj) {
            const v = obj[k];
            if (Boolean(v)) {
                if (typeof v === 'object') {
                    result[k] = compactObject(v);
                } else {
                    result[k] = v;
                }
            }
        }
        return result;
    }
};
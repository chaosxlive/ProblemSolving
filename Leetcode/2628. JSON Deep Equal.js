// https://leetcode.com/problems/json-deep-equal/

/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function (o1, o2) {
    if (typeof o1 !== typeof o2) {
        return false;
    }
    if (['string', 'boolean', 'number', 'undefined'].includes(typeof o1)) {
        return o1 === o2;
    }
    if (o1 === null && o2 === null) {
        return true;
    }
    if (Array.isArray(o1) || Array.isArray(o2)) {
        if (!Array.isArray(o1) || !Array.isArray(o2) || o1.length !== o2.length) {
            return false;
        }
        return o1.every((v, i) => areDeeplyEqual(v, o2[i]));
    }
    return Object.keys(o1).length === Object.keys(o2).length && Object.keys(o1).every(k => Object.prototype.hasOwnProperty.call(o2, k) && areDeeplyEqual(o1[k], o2[k]));
};
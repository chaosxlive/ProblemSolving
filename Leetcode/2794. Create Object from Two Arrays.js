// https://leetcode.com/problems/create-object-from-two-arrays/

/**
 * @param {Array} keysArr
 * @param {Array} valuesArr
 * @return {Object}
 */
var createObject = function (keysArr, valuesArr) {
    const result = {};
    for (let i = 0; i < keysArr.length; i++) {
        const k = '' + keysArr[i];
        const v = valuesArr[i];
        if (!Object.prototype.hasOwnProperty.call(result, k)) {
            result[k] = v;
        }
    }
    return result;
};
// https://leetcode.com/problems/repeat-string/

/**
 * @param {number} times
 * @return {string}
 */
String.prototype.replicate = function (times) {
    const result = [];
    for (let i = 0; i < times; i++) {
        result.push(this);
    }
    return result.join('');
}
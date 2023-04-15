// https://leetcode.com/problems/curry/

/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function (fn) {
    const savedArgs = [];
    return function curried(...args) {
        savedArgs.push(...args);
        if (savedArgs.length < fn.length) {
            return curried;
        }
        return fn(...savedArgs);
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
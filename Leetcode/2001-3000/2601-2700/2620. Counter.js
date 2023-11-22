// https://leetcode.com/problems/counter/

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function (n) {
    this.v = undefined;
    return function () {
        if (this.v === undefined) {
            this.v = n;
        }
        return this.v++;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
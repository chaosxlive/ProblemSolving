// https://leetcode.com/problems/memoize/

/**
 * @param {Function} fn
 */
function memoize(fn) {
    this.map = undefined;
    return function (...args) {
        const key = args.length === 1 ? `${args[0]}` : `${args[0]}_${args[1]}`;
        if (!this.map) {
            this.map = {};
        }
        if (!(key in this.map)) {
            this.map[key] = fn(...args);
        }
        return this.map[key];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
// https://leetcode.com/problems/memoize-ii/

/**
 * @param {Function} fn
 */
function memoize(fn) {
    const argCaches = [];
    const argIds = [];
    const dataCache = {};

    return function (...args) {
        for (let i = argCaches.length; i < args.length; i++) {
            argCaches.push(new Map());
            argIds.push(0);
        }
        const ids = args.map((arg, i) => {
            const argCache = argCaches[i];
            if (!argCache.has(arg)) {
                argCache.set(arg, argIds[i]++);
            }
            return argCache.get(arg);
        });
        const key = JSON.stringify(ids);
        if (!(key in dataCache)) {
            dataCache[key] = fn(...args);
        }
        return dataCache[key];
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
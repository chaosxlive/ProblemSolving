/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function (fn, t) {
    let latest = 0;
    let last = null;
    let next = null;

    const f = function (...args) {
        last = args;
        const curr = new Date().getTime();
        if (curr >= latest + t) {
            fn(...last);
            latest = curr;
            last = null;
        } else {
            clearTimeout(next);
            next = setTimeout(() => f(...args), latest + t - curr);
        }
    };
    return f;
};


/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
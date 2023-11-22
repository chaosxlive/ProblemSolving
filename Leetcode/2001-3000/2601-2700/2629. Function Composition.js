// https://leetcode.com/problems/function-composition/

/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
    return (v) => {
        for (let i = functions.length - 1; i >= 0; i--) {
            const f = functions[i];
            v = f(v);
        }
        return v;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
// https://leetcode.com/problems/counter-ii/

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {

    defaultVal = init;
    val = init;

    return {
        increment: () => {
            return ++val;
        },
        decrement: () => {
            return --val;
        },
        reset: () => {
            val = defaultVal;
            return val;
        },
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
// https://leetcode.com/problems/custom-interval/

var intervalSaved = [];

/**
 * @param {Function} fn
 * @param {number} delay
 * @param {number} period
 * @return {number} id
 */

function customInterval(fn, delay, period) {
    const id = intervalSaved.length;
    intervalSaved.push(false);
    let currentDelay = delay;
    setTimeout(() => {
        if (intervalSaved[id] === true) {
            return;
        }
        inner();
    }, delay)
    return id;

    function inner() {
        fn();
        currentDelay += period;
        setTimeout(() => {
            if (intervalSaved[id] === true) {
                return;
            }
            inner();
        }, currentDelay);
    }
}

/**
 * @param {number} id
 */
function customClearInterval(id) {
    intervalSaved[id] = true;
}
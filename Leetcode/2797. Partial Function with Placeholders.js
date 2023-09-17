// https://leetcode.com/problems/partial-function-with-placeholders/

/**
 * @param {Function} fn
 * @param {Array} args
 * @return {Function}
 */
var partial = function (fn, args) {

    return function (...restArgs) {
        const realArgs = [];
        let i = 0;
        args.forEach(arg => {
            if (arg === '_') {
                realArgs.push(restArgs[i++]);
            } else {
                realArgs.push(arg);
            }
        });
        for (; i < restArgs.length; i++) {
            realArgs.push(restArgs[i]);
        }
        return fn(...realArgs);
    }
};
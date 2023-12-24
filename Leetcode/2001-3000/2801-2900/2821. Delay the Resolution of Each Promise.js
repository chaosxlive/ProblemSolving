/**
 * @param {Array<Function>} functions
 * @param {number} ms
 * @return {Array<Function>}
 */
var delayAll = function (functions, ms) {
    return functions.map(f => {
        return () => {
            return new Promise((resolve, reject) => {
                setTimeout(() => f()
                    .then(res => resolve(res))
                    .catch(err => reject(err)), ms);
            });
        };
    });
};


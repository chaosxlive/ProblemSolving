// https://leetcode.com/problems/promise-pool/

/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function (functions, n) {
    let restJobCnt = functions.length;
    return new Promise((resolve, _reject) => {
        if (functions.length === 0) {
            resolve('empty');
            return;
        }
        for (let i = 0; i < Math.min(functions.length, n); i++) {
            setTimeout(() => {
                newJob(functions.shift());
            });
        }

        function newJob(job) {
            if (!job) {
                return;
            }
            job().then(() => {
                restJobCnt--;
                if (restJobCnt === 0) {
                    resolve('done');
                }
                newJob(functions.shift());
            });
        }
    });
};


/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */
// https://leetcode.com/problems/add-two-promises/

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {
    return new Promise(async (resolve, _reject) => {
        resolve(await promise1 + await promise2);
    });
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
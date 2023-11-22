// https://leetcode.com/problems/group-by/

/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function (fn) {
    const result = {};
    this.forEach(v => {
        const key = fn(v);
        if (!result[key]) {
            result[key] = [];
        }
        result[key].push(v);
    });
    return result;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
// https://leetcode.com/problems/join-two-arrays-by-id/

/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
    const resMap = {};
    arr1.forEach(item => {
        resMap[item.id] = item;
    });
    arr2.forEach(item => {
        if (!resMap[item.id]) {
            resMap[item.id] = item;
            return;
        }
        Object.keys(item).forEach(k => {
            if (k === 'id') return;
            resMap[item.id][k] = item[k];
        });
    });
    return Object.values(resMap).sort((a, b) => a.id - b.id);
};
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var getWinner = function (arr, k) {
    if (k === 1) {
        return Math.max(arr[0], arr[1]);
    }
    let a = arr[0];
    let winCnt = 0;
    for (let i = 1; i < arr.length; i++) {
        const b = arr[i];
        if (a > b) {
            winCnt++;
            if (winCnt === k) {
                return a;
            }
        } else {
            a = b;
            winCnt = 1;
        }
    }
    return Math.max(...arr);
};
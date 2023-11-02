// https://leetcode.com/problems/array-upper-bound/

/** 
 * @param {number} target
 * @return {number}
 */
Array.prototype.upperBound = function (target) {
    let left = 0;
    let right = this.length;
    let result = -1
    while (left < right) {
        const mid = Math.floor(left + (right - left) / 2);
        if (this[mid] > target) {
            right = mid;
        } else if (this[mid] < target) {
            left = mid + 1;
        } else {
            result = Math.max(result, mid);
            left = mid + 1;
        }
    }
    return result;
};


// [3,4,5].upperBound(5); // 2
// [1,4,5].upperBound(2); // -1
// [3,4,6,6,6,6,7].upperBound(6) // 5
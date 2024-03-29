// https://leetcode.com/problems/generate-circular-array-values/

/**
 * @param {Array<number>} arr
 * @param {number} startIndex
 * @yields {number}
 */
var cycleGenerator = function* (arr, startIndex) {
    let idx = startIndex;
    const l = arr.length;
    let step = 0;
    while (true) {
        idx = (((idx + step) % l) + l) % l
        step = yield arr[idx];
    }
};

/**
 *  const gen = cycleGenerator([1,2,3,4,5], 0);
 *  gen.next().value  // 1
 *  gen.next(1).value // 2
 *  gen.next(2).value // 4
 *  gen.next(6).value // 5
 */
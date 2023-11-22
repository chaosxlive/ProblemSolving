// https://leetcode.com/problems/snail-traversal/

/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function (rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) {
        return [];
    }
    const result = [];
    for (let r = 0; r < rowsCount; r++) {
        result.push([]);
    }
    this.forEach((v, i) => {
        const r = i % rowsCount;
        const c = Math.floor(i / rowsCount);
        result[c % 2 === 0 ? r : (rowsCount - r - 1)].push(v);
    });
    return result;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
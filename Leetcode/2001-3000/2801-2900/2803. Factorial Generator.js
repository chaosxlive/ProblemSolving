// https://leetcode.com/problems/factorial-generator/

/**
 * @param {number} n
 * @yields {number}
 */
function* factorial(n) {
    if (n === 0) {
        n = 1;
    }
    let v = 1;
    let step = 1;
    while (n > 0) {
        v *= step;
        step++;
        n--;
        yield v;
    }
    return;
};


/**
 * const gen = factorial(2);
 * gen.next().value; // 1
 * gen.next().value; // 2
 */
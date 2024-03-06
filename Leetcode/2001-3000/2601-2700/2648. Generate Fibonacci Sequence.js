// https://leetcode.com/problems/generate-fibonacci-sequence/

/**
 * @return {Generator<number>}
 */
var fibGenerator = function* () {
    yield 0;
    yield 1;
    yield 1;
    let prev1 = 1;
    let prev2 = 1;
    while (true) {
        const result = prev1 + prev2;
        yield result
        prev2 = prev1;
        prev1 = result;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
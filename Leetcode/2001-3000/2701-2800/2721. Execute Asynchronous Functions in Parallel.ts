// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

type Fn2721<T> = () => Promise<T>

function promiseAll<T>(functions: Fn2721<T>[]): Promise<T[]> {
    return new Promise((resolve, reject) => {
        let rest = functions.length;
        const results: T[] = Array(functions.length);
        const checkDone = () => {
            rest--;
            if (rest === 0) {
                resolve(results);
            }
        };
        functions.forEach((func, i) => {
            func()
                .then(res => {
                    results[i] = res;
                    checkDone();
                })
                .catch(res => {
                    reject(res);
                });
        });
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */ 
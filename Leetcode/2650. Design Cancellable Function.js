// https://leetcode.com/problems/design-cancellable-function/

/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function (generator) {
    let resolve, reject;
    let isCancelled = false;

    const promise = new Promise((resolveFunc, rejectFunc) => {
        resolve = resolveFunc;
        reject = rejectFunc;
    });

    const cancel = () => {
        isCancelled = true;
        try {
            resolve(generator.throw('Cancelled').value);
        } catch (error) {
            reject(error);
        }
    };

    function handle(value, error) {
        if (isCancelled) {
            return;
        }
        try {
            const resp = error ? generator.throw(error) : generator.next(value);
            if (resp.done) {
                resolve(resp.value);
                return;
            }
            Promise.resolve(resp.value)
                .then(r => handle(r))
                .catch(e => handle(undefined, e));
        } catch (error) {
            reject(error);
        }
    }

    handle();

    return [cancel, promise];
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */

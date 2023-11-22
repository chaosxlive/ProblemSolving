// https://leetcode.com/problems/infinite-method-object/

/**
 * @return {Object}
 */
var createInfiniteObject = function () {
    return new Proxy({}, {
        get: (_target, propKey) => {
            return () => {
                return propKey.toString();
            };
        }
    })
};

/**
 * const obj = createInfiniteObject();
 * obj['abc123'](); // "abc123"
 */
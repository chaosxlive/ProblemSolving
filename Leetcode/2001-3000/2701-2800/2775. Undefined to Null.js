/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var undefinedToNull = function (obj) {
    if (obj === undefined || obj === null) {
        return null;
    }
    if (typeof obj === 'object') {
        if (Array.isArray(obj)) {
            return obj.map(v => undefinedToNull(v));
        }
        return Object.fromEntries(
            Object.entries(obj)
                .map(([key, value]) => {
                    if (typeof value === 'undefined') {
                        return [key, null];
                    }
                    if (typeof value === 'object') {
                        return [key, undefinedToNull(value)];
                    }
                    return [key, value];
                }));
    }
    return obj;
};

/**
 * undefinedToNull({"a": undefined, "b": 3}) // {"a": null, "b": 3}
 * undefinedToNull([undefined, undefined]) // [null, null] 
 */
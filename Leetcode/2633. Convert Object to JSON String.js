// https://leetcode.com/problems/convert-object-to-json-string/

/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function (object) {
    if (object === null) {
        return 'null';
    }
    switch (typeof object) {
        case 'string':
            return `"${object}"`;
        case 'number':
            return object.toString();
        case 'boolean':
            return object ? 'true' : 'false';
    }
    if (Array.isArray(object)) {
        return `[${object.map(v => jsonStringify(v)).join(',')}]`;
    }
    return `{${Object.entries(object).map(([k, v]) => `"${k}":${jsonStringify(v)}`).join(',')}}`;
};
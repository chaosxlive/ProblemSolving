// https://leetcode.com/problems/array-of-objects-to-matrix/

/**
 * @param {Array} arr
 * @return {(string | number | boolean | null)[][]}
 */
var jsonToMatrix = function (arr) {
    const keys = new Set();

    /**
     * @param {any} obj
     * @return {Set<string>}
     */
    function getKeys(obj) {
        const retkeys = new Set();
        Object.entries(obj)
            .forEach(([key, value]) => {
                if (typeof value === 'object' && value !== null) {
                    getKeys(value).forEach(k => {
                        retkeys.add(key + '.' + k);
                    });
                } else {
                    retkeys.add(key);
                }
            });
        return retkeys;
    }

    arr.forEach(obj => getKeys(obj).forEach(k => keys.add(k)));
    const sortedKeys = [...keys.values()];
    sortedKeys.sort();

    const result = [];
    result.push(sortedKeys);

    arr.forEach(obj => {
        if (obj === undefined) {
            result.push(sortedKeys.map(_ => ''));
        }
        result.push(sortedKeys.map(ks => {
            const steps = ks.split('.');
            let iter = obj;
            for (const step of steps) {
                if (iter === null || typeof iter === 'string') {
                    return '';
                }
                iter = iter[step];
                if (iter === undefined) {
                    return '';
                }
            }
            return iter === null || ['number', 'string', 'boolean'].includes(typeof iter) ? iter : '';
        }));
    });

    return result;
};
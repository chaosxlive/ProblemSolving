// https://leetcode.com/problems/differences-between-two-objects/

/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */
function objDiff(obj1, obj2) {
    if ((Array.isArray(obj1) && !Array.isArray(obj2)) ||
        (!Array.isArray(obj1) && Array.isArray(obj2))) {
        return [obj1, obj2];
    }
    const result = {};
    for (const i in obj2) {
        const o1 = obj1[i];
        const o2 = obj2[i];
        if (o1 === undefined) {
            continue;
        }
        if (o1 === o2) {
            continue;
        }
        if (Array.isArray(o1) && Array.isArray(o2)) {
            const ret = objDiff(o1, o2);
            result[i] = ret;
            continue;
        }
        if (o1 === null || o2 === null) {
            result[i] = [o1, o2];
            continue;
        }
        if (typeof o1 === 'object' && typeof o2 === 'object') {
            const ret = objDiff(o1, o2);
            result[i] = ret;
            continue;
        }
        result[i] = [o1, o2];
    }
    for (const k in result) {
        if (Object.keys(result[k]).length === 0) {
            delete result[k];
        }
    }
    return result;
};
// https://leetcode.com/problems/cache-with-time-limit/

var TimeLimitedCache = function () {
    this.c = {}
    this.n = 0;
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
    const self = this;
    let ret = false;
    if (self.c[key]) {
        ret = true;
        clearTimeout(self.c[key].timer);
    } else {
        self.n++;
    }
    self.c[key] = {
        v: value,
        timer: setTimeout(() => {
            delete self.c[key];
            self.n--;
        }, duration),
    };
    return ret;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
    return this.c[key] ? this.c[key].v : -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
    return this.n;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
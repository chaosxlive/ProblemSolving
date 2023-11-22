// https://leetcode.com/problems/next-day/

/** 
 * @return {string}
 */
Date.prototype.nextDay = function () {
    const date = new Date(this)
    date.setDate(date.getDate() + 1)
    return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`;
}

/**
 * const date = new Date("2014-06-20");
 * date.nextDay(); // "2014-06-21"
 */
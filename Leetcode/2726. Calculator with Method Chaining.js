// https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator {

    /** 
     * @param {number} value
     */
    constructor(value) {
        this.v = value;
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value) {
        this.v += value;
        return this;
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value) {
        this.v -= value;
        return this;
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    multiply(value) {
        this.v *= value;
        return this;
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if (value === 0) {
            throw new Error("Division by zero is not allowed");
        }
        this.v /= value;
        return this;
    }

    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        this.v = Math.pow(this.v, value);
        return this;
    }

    /** 
     * @return {number}
     */
    getResult() {
        return this.v;
    }
}
//2726. Calculator with Method Chaining
/**
 * @param {number} value
 */
var Calculator = function (value) {
  this.result = value;
};

/** 
 * @param {number} value
 * @return {Calculator}
 */
Calculator.prototype.add = function (value) {
  this.result += value;
  return this;
};

/** 
 * @param {number} value
 * @return {Calculator}
 */
Calculator.prototype.subtract = function (value) {
  this.result -= value;
  return this;
};

/** 
 * @param {number} value
 * @return {Calculator}
 */
Calculator.prototype.multiply = function (value) {
  this.result *= value;
  return this;
};

/** 
 * @param {number} value
 * @return {Calculator}
 */
Calculator.prototype.divide = function (value) {
  if (value === 0) {
    throw new Error("Division by zero is not allowed");
  }
  this.result /= value;
  return this;
};

/** 
 * @param {number} value
 * @return {Calculator}
 */
Calculator.prototype.power = function (value) {
  this.result **= value;
  return this;
};

/** 
 * @return {number}
 */
Calculator.prototype.getResult = function () {
  return this.result;
};
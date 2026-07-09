//2635. Apply Transform Over Each Element in Array//
var map = function (arr, fn) {
  let NewArr = [];
  for (let i = 0; i < arr.length; i++) {

    NewArr[i] = fn(arr[i], i);
  }
  return NewArr;
};
//Take the element at position i from arr, pass it to the function fn along with its index i, then store the function's result in the same position i of NewArr.
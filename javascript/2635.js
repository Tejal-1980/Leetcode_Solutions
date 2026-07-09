//2635. Apply Transform Over Each Element in Array//
var map = function (arr, fn) {
  let NewArr = [];
  for (let i = 0; i < arr.length; i++) {

    NewArr[i] = fn(arr[i], i);
  }
  return NewArr;
};
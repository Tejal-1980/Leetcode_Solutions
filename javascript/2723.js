// 2723- Adding 2 promises
let promiseVal1 = Promise.resolve(Number(prompt("enter a number")));
let promiseVal2 = Promise.resolve(Number(prompt("enter a number")));
const finalVal = Val1 + Val2;
console.log(finalVal)
return finalVal;


addTwoPromises(promiseVal1, promiseVal2).then(Result => {
  console.log(" then final val :", Result);
});
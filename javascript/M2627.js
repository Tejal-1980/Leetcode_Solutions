//2627. Debounce

var debounce = function (fn, t) {
  let timer;
  return function (...args) {
    clearTimeout(Timer)
    Timer = setTimeout(() => fn(...args), t)

  }
};
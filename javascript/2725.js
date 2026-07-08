//2725. Interval Cancellation//
add
const cancellable = function (fn, args, t) {
  const timer = setTimeout(() => {
    fn(...args);
  }, t);

  return function () {
    clearTimeout(timer);
  };
};


// 2715 Timeout Cancellation//
const cancellable = function (fn, args, t) {
  const timer = setTimeout(() => {
    fn(...args);
  }, t);

  return function () {
    clearTimeout(timer);
  };
};

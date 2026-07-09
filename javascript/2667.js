//2667. Create Hello World Function//
var createHelloWorld = function (...args) {

  return function (...args) {
    return "Hello World";

  }
};


//arguments are not discarded—they're stored in args. They're simply never read afterward.//
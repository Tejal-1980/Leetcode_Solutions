//2727. Is Object Empty //
// sourcery skip: avoid-using-var
var isEmpty = function (obj) {
  if (Object.keys(obj).length === 0)
    return true;
  else
    return false;
};
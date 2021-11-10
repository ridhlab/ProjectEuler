// Smallest Multiple

function getSmallestMultiple(num) {
  let res = 2;
  let isMultiples = false;
  while (true) {
    for (let i = 2; i <= num; i++) {
      if (res % i === 0) {
        if (i === num) {
          isMultiples = true;
          break;
        }
        continue;
      }
      break;
    }
    if (isMultiples) {
      break;
    }
    res++;
  }
  return res;
}
const num = 18;
console.log(getSmallestMultiple(num));

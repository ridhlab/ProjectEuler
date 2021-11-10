// Smallest Multiple
const num = 16;
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
console.log(res);

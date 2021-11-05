// Multiples 3 and 5

const max = 1000;
const inputNum1 = 12;
const inputNum2 = 20;

let sum1 = 0;
let sum2 = 0;
for (let i = 0; i < maks; i++) {
  if (i % inputNum1 === 0) {
    sum1 += i;
    if (i % inputNum2 === 0) {
      continue;
    }
  }
  if (i % inputNum2 === 0) {
    sum2 += i;
  }
}
console.log(sum1 + sum2);

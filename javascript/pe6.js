// Sum Square Difference

const num = 100;

function getSumOfSquare(num) {
  let sumOfSquare = 0;
  for (let i = 1; i <= num; i++) {
    sumOfSquare += i ** 2;
  }
  return sumOfSquare;
}
function getSquareOfSum(num) {
  let sum = 0;
  for (let i = 1; i <= num; i++) {
    sum += i;
  }
  return sum ** 2;
}

const sumOfSquare = getSumOfSquare(num);
const squareOfSum = getSquareOfSum(num);

console.log(Math.abs(sumOfSquare - squareOfSum));

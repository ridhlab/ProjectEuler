// 10001st Prime

const num = 10001;
let listPrimeNumbers = [];
let temp = 2;
while (true) {
  if (temp === 2) {
    listPrimeNumbers.push(temp);
  }
  for (let i = 2; i < temp; i++) {
    if (i === temp - 1) {
      listPrimeNumbers.push(temp);
    }
    if (temp % i === 0) {
      break;
    } else {
      continue;
    }
  }
  if (listPrimeNumbers.length === num) {
    break;
  }
  temp++;
}
console.log(listPrimeNumbers.slice(-1)[0]);

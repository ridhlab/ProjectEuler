// Summaton of Primes

function getListPrimeNumbers(max) {
  let listPrimeNumbers = [];
  for (let i = 2; i <= max; i++) {
    if (i === 2) {
      listPrimeNumbers.push(i);
      continue;
    }
    for (let j = 2; j < i; j++) {
      if (j === i - 1) {
        listPrimeNumbers.push(i);
      }
      if (i % j === 0) {
        break;
      } else {
        continue;
      }
    }
  }
  return listPrimeNumbers;
}

function getSummationOfPrime(listPrimeNumbers) {
  let res = 0;
  for (let i = 0; i < listPrimeNumbers.length; i++) {
    res += listPrimeNumbers[i];
  }
  return res;
}

const num = 17;
const listPrimeNumbers = getListPrimeNumbers(num);

console.log(getSummationOfPrime(listPrimeNumbers));

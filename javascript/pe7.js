// 10001st Prime

function getNthPrime(num) {
  let listPrimeNumbers = [];
  let tempNum = 2;
  while (true) {
    if (tempNum === 2) {
      listPrimeNumbers.push(tempNum);
    }
    for (let i = 2; i < tempNum; i++) {
      if (i === tempNum - 1) {
        listPrimeNumbers.push(tempNum);
      }
      if (tempNum % i === 0) {
        break;
      } else {
        continue;
      }
    }
    if (listPrimeNumbers.length === num) {
      break;
    }
    tempNum++;
  }
  return listPrimeNumbers;
}

const num = 123;
console.log(getNthPrime(num).slice(-1)[0]);

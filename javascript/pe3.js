// Largest Prima Factor

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
function getlistPrimeFactor(listPrimeNumbers, num) {
  let listPrimeFactor = [];
  listPrimeNumbers.forEach((element) => {
    if (num % element === 0) {
      listPrimeFactor.push(element);
    }
  });
  return listPrimeFactor;
}

const num = 1000;

const listPrimeNumbers = getListPrimeNumbers(num);

const listPrimeFactor = getlistPrimeFactor(listPrimeNumbers, num);

console.log(listPrimeNumbers);

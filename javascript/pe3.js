// Largest Prima Factor

function getListPrimeNumbers(max) {
  let listPrimeFactor = [];
  for (let i = 2; i <= max; i++) {
    if (i === 2) {
      listPrimeFactor.push(i);
      continue;
    }
    for (let j = 2; j < i; j++) {
      if (j === i - 1) {
        listPrimeFactor.push(i);
      }
      if (i % j === 0) {
        break;
      } else {
        continue;
      }
    }
  }
  return listPrimeFactor;
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

const num = 99870;

const listPrimeNumbers = getListPrimeNumbers(num);

const listPrimeFactor = getlistPrimeFactor(listPrimeNumbers, num);

console.log(listPrimeFactor);

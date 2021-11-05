// Even Fibonacci Numbers
function fibonacci(num) {
  if (num === 0) {
    return 1;
  }
  if (num === 1) {
    return 2;
  } else {
    return fibonacci(num - 2) + fibonacci(num - 1);
  }
}

function getListFibonacci() {
  let listFibonacci = [];
  i = 0;
  while (true) {
    listFibonacci.push(fibonacci(i));
    if (listFibonacci[listFibonacci.length - 1] > max) {
      break;
    }
    i++;
  }
  return listFibonacci.slice(0, -1);
}
function getSumEven(listFibonacci) {
  sumEven = 0;
  listFibonacci.forEach((element) => {
    if (element % 2 === 0) {
      sumEven += element;
    }
  });
  return sumEven;
}

const max = 4000000;
listFibonacci = getListFibonacci();
console.log(getSumEven(listFibonacci));

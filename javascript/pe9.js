// Special Pythagorean Triplet

function getPythagoreanTriplet(num) {
  let res;
  for (let a = 1; a < num; a++) {
    for (let b = 1; b < num; b++) {
      let c = num - a - b;
      if (a ** 2 + b ** 2 === c ** 2) {
        res = a * b * c;
      }
    }
  }
  return res;
}

const num = 1000;
console.log(getPythagoreanTriplet(num));

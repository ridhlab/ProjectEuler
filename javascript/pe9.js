// Special Pythagorean Triplet

const num = 1000;
let res;
for (let a = 1; a < num; a++) {
  for (let b = 1; b < num; b++) {
    let c = num - a - b;
    if (a ** 2 + b ** 2 === c ** 2) {
      res = a * b * c;
    }
  }
}

console.log(res);

// Largest Palindrome Product
const digit = 3;

const minRes = 10 ** digit;

function checkPalindrome(num) {
  strNum = num.toString();
  let check = false;
  for (let i = 0; i < parseInt(strNum.length / 2); i++) {
    if (strNum[i] === strNum[strNum.length - 1 - i]) {
      check = true;
    } else {
      check = false;
      break;
    }
  }
  return check;
}

const temp = [];
for (let i = 10 ** (digit - 1); i < minRes; i++) {
  for (let j = i; j < minRes; j++) {
    temp.push(i * j);
  }
}

const palindrome = [];
temp.forEach((element) => {
  if (checkPalindrome(element)) {
    palindrome.push(element);
  }
});

console.log(
  palindrome.sort(function (a, b) {
    return b - a;
  })
);

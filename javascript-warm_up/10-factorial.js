#!/usr/bin/node

function factorial (n) {
  if (Number.isNaN(n)) {
    return 1;
  }

  if (n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const input = Number(process.argv[2]);
if (!Number.isNaN(input)) {
  console.log(factorial(input));
} else {
  console.log(1);
}

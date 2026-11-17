#!/usr/bin/node

const numList = [];

for (let i = 2; i < process.argv.length; i++) {
  numList.push(Number(process.argv[i]));
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  numList.sort((a, b) => b - a);
  console.log(numList[1]);
}

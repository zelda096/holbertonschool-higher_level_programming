#!/usr/bin/node
// this script compute and print a factorial that pass for the command line

function factorial (x) {
  if (x === 0) {
    return (1);
  } else {
    return x * factorial(x - 1);
  }
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}

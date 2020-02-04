#!/usr/bin/node
// this script search the second argument that pass in the command line

if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const intArgs = args.sort((a, b) => a - b);
  console.log(intArgs[intArgs.length - 2]);
}

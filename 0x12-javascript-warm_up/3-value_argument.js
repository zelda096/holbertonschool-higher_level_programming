#!/usr/bin/node
// this print the argv pass in the command line
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}

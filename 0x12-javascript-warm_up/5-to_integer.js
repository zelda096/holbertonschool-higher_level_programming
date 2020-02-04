#!/usr/bin/node
//this parsed or not the args in the commands line
if (isNaN(process.argv[2]))
{
    console.log('Not a number');
} else {
    console.log('My number: ' + parseInt(process.argv[2]));
}

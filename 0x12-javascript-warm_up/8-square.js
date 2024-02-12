#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) console.log('Missing size');
else {
  for (let r = 0; r < Number(process.argv[2]); r++) {
    let row = '';
    for (let c = 0; c < Number(process.argv[2]); c++) row += 'X';
    console.log(row);
  }
}

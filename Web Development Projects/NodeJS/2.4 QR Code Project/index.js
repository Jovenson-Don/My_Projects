/* 
1. Use the inquirer npm package to get user input.
2. Use the qr-image npm package to turn the user entered URL into a QR code image.
3. Create a txt file to save the user input using the native fs node module.
*/

import { input } from '@inquirer/prompts';
const answer = await input({ message: 'Enter url code' });

import  qr  from "qr-image";
import  fs  from "fs";

var qr_code = qr.image(answer, { type: 'png'})
qr_code.pipe(fs.createWriteStream('qr_img.png'));


import { writeFile } from 'node:fs';
writeFile('URL.txt', answer, (err) => {
    if (err) throw err;
    console.log('The file has been saved!');
  }); 
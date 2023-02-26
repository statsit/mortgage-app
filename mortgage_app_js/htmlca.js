
let outerClass = document.getElementsByClassName('outer')
outerClass.textContent = 'Hello World';

let canvas = document.getElementById('canvas');
let ctx = canvas.getContext("2d");
ctx.font = '30px Arial';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';
ctx.fillStyle = '#FFF';
ctx.fillText('Hello World', 150, 150);
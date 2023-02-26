
// let canvas = document.getElementById('myCanvas');
// let ctx = canvas.getContext('2d');
// ctx.font = '30px Arial';


// canvas.addEventListener('mousemove', function(event) {
//     let cRect = canvas.getBoundingClientRect();
//     let canvasX = Math.round(event.clientX - cRect.left);
//     let canvasY = Math.round(event.clientY - cRect.top);
//     ctx.clearRect(0, 0, canvas.width, canvas.height);
//     ctx.fillText("X: " + canvasX + " Y: " + canvasY, 10, 50);
// });

const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
var ox = canvas.width/2;
var oy = canvas.height/2;
ctx.font = '42px Arial';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';
ctx.fillStyle = '#FFF';
ctx.fillText('Hello World', ox, oy);

rotate_ctx = ()=>{
    ctx.translate(ox, oy);
    ctx.rotate(Math.PI/180 * 15);
    ctx.fillStyle = 'red';
    ctx.fillText('Hello World', 0, 0);
    ctx.translate(-ox, -oy);
}

download_img =(el)=>{
    let imageURI = canvas.toDataURL("image/png");
    el.href = imageURI;
};


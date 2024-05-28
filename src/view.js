import Two from 'https://cdn.skypack.dev/two.js@latest';
//https://two.js.org/docs/two

class View {
    container;
    canvas;
    colours = {
        background:"rgb(10,10,10)", 
        pointfill:[255,255,240],
        pointstroke:[106,90,205],
        black:[10,10,10],
        darkCyanBlue:[10,30,41],
        ivory:[255,255,240],
        slateblue:[106,90,205],
    }
    height = 150;
    width = 300;

    canvasOptions =  {
        type: Two.Types.webgl, 
        // vs type: Two.Types.Canvas/svg/webgl
        // vs type: Two.Types.canvas
        fullscreen: true,
        autostart: true,
        height: this.height,
        width: this.width,
        //domElement : this.container
    }

    constructor() {
        this.container = document.getElementById("canvas");
        this.canvas = this.createCanvas()
    }


    static getRandomArbitrary(min, max) {
        return Math.random() * (max - min) + min;
    }

    createCanvas() {
        var canvas = new Two(this.canvasOptions).appendTo(this.container)
        canvas.renderer.domElement.style.backgroundColor = 
            this.colours.background; 
        return canvas;
    }

    clearCanvas() {
        this.canvas.clear()
    }

    paintRectangle(x, y, width, height) {
        const rectangle = new Two.Rectangle(x, y, width, height)
        rectangle.position.x = x + Math.random();
        rectangle.position.y = y + Math.random();
        rectangle.rotation = Math.random() * Math.PI * 2;
        rectangle.fill = this.getRandomColor();
        rectangle.stroke = "white";
        this.canvas.add(rectangle)
    }

    paintTriangle(){
        let radius = 20
        let triangle = new Two.Polygon(100, 200, radius, 30)
        this.canvas.add(triangle) 
    }

    getRandomColor() {
      var red = Math.floor(Math.random() * 255);
      var green = Math.floor(Math.random() * 255);
      var blue = Math.floor(Math.random() * 255);
      return `rgb(${red}, ${green}, ${blue})`;
    }
}


//twoCanvas.bind('update', function() {
//    stars.forEach( star => {
//        star.edges();
//        star.updatePosition();
//    });
//}); 


const view = new View()
view.clearCanvas()
const x = view.canvas.width / 2
const y = view.canvas.height / 2
const width = 25
const height = 50;
view.paintRectangle(x, y, width, height)
view.paintTriangle()
//view.clearCanvas()

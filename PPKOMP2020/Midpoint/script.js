// Define Input
process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;
});

process.stdin.on("end", function () {
   main(stdin_input);
});

// Main Function
function main(input) {
    //Enter your code here
    var arr = input.split("\n");
    var [x1,y1] = Object.values(arr)[0].split(" ").map(Number);
    var [x2,y2] = Object.values(arr)[1].split(" ").map(Number);
    var A = (x1+x2)/2;
    var B = (y1+y2)/2;
    process.stdout.write(A.toString() + " " + B.toString());
    
}


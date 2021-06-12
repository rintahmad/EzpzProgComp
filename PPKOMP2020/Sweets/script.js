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
    var x = parseInt(input);
    ((x % 2 == 0) && (x > 5)) ? process.stdout.write("boleh") : process.stdout.write("tidak boleh");
    
}


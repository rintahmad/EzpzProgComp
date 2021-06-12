process.stdin.resume();
process.stdin.setEncoding('utf-8');

// Define Input
let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Main Function
function main() {
    const n = parseInt(readLine());
    let output = 1;
    let counter = 0;
    
    for (var i = 0; i < 1000000; i++)
    {
        output += i;
        counter += 1;
        if (n == counter){
            break;
        }
    }
    console.log(output);
}

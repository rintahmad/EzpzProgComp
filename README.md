# EzpzProgComp

This repo will not have much explanation but will be use to store any tricks and solutions for any programing questions whether local or international events.

I want to improve on different programming languages, so this repo would have different solutions consists of:

- Python
- C
- C++
- Node JS
- Rust (Hopefully)

## Python

```bash
# Input
arr = [int(x) for x in input().split()]
x,y = map(int,input().split())
x = int(input())
M = list(map(int,input().split()))

# One Liner
print("boleh") if (x % 2 == 0) and (x > 5) else print("tidak boleh")

# Sort List & Sum (Top 5)
sum(sorted(M)[-5:])

# Floor Div
x = 6 // 4
```

# Node js

```bash
# Input (Define1)
// Define Input
process.stdin.resume();
process.stdin.setEncoding("utf-8");
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

# Input (Define2)
process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;
});

process.stdin.on("end", function () {
   main(stdin_input);
});


# Input Usage
const n = parseInt(readLine());

# Assign (Split)
var arr = input.split("\n");
var [x1,y1] = Object.values(arr)[0].split(" ").map(Number);
var [x2,y2] = Object.values(arr)[1].split(" ").map(Number);

# Convert
B.toString()

# One Liner
((x % 2 == 0) && (x > 5)) ? process.stdout.write("boleh") : process.stdout.write("tidak boleh");
```

# References

```bash
#==Python==
- https://gist.github.com/jenthone/300e6fbbd9d5ba39fe6cd4fa107b4477

#==Algorithm==
- https://www.techiedelight.com/
```

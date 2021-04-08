const readline = require("readline");

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    const n = parseInt(input[0]);

    let numbers = [];
    for (let i = 1; i <= n; i++) {
        numbers.push(input[i]);
    }

    const len = numbers.length;

    if (len > 1) {
        numbers = numbers.sort((a, b) => {
            console.log(a, b)
            return a - b;
        });
    }

    for (let i = 0; i < len; i++){
        console.log(numbers[i]);
    }
    process.exit();
});
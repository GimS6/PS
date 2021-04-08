let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    let n = parseInt(input[0]);

    for (let i = -n + 1; i < n; i++) {
        let result = "*".repeat(n - Math.abs(i)) + " ".repeat(Math.abs(i));
        console.log(result + result.split('').reverse().join(''))
    }

    process.exit();
});
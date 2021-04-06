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

    console.log(n * (n + 1) / 2)

    process.exit();
});
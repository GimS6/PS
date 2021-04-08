let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {

    let n = input[0];

    for (let i = 0; i < n; i++) {
        console.log(' '.repeat(i) + "*".repeat(n - i));
    }

    process.exit();
});
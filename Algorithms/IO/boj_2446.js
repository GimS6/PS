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
    let maxStarsNum = n * 2 - 1;

    for (let i = -n + 1; i < n; i++) {
        let stars = "*".repeat(Math.abs(Math.abs(i) * 2 + 1));
        let space = " ".repeat((maxStarsNum - stars.length) / 2);

        console.log(space + stars);
    }

    process.exit();
});
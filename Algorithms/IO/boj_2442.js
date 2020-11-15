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
    let lastStarsNum = n * 2 - 1

    for (let i = 1; i <= n; i++) {
        let stars = "*".repeat(i * 2 - 1);
        let space = " ".repeat((lastStarsNum - stars.length) / 2);

        console.log(space + stars);
    }

    process.exit();
});
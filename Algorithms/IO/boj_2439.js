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
    let space = ' ';
    let star = "*";

    for (let i = 1; i  <= n; i++) {
        let result = space.repeat(n-i) + star.repeat(i);
        console.log(result);
    }

    process.exit();
});
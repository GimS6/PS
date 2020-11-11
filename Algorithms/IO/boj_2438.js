let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    outpu: process.stdout
})

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    let n = input[0];

    let stars = "*";
    for (let i = 1; i <= n; i++) {
        console.log(stars.repeat(i))
    }

    process.exit();
})
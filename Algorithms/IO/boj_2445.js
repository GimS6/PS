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

    for (let i = 1; i <= n; i++) {
        let stars = '*'.repeat(i);
        let space = ' '.repeat(n * 2 - i * 2);

        console.log(stars + space + stars);
    }

    for (let i = n - 1; i > 0; i--) {
        let stars = '*'.repeat(i);
        let space = ' '.repeat(n * 2 - i * 2);

        console.log(stars + space + stars);
    }

    process.exit();
});
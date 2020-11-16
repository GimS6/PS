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

    for (let i = 1; i <= n; i++) {
        let space = " ".repeat(n - i);
        let stars = "* ".repeat(i).trimEnd();

        console.log(space + stars)
    }

    process.exit();
});
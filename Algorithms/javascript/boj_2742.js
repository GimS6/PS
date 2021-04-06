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
    let result = [];

    for (let i = n; i >= 1; i--) {
        result.push(i + '');
    }
    console.log(result.join('\n'));

    process.exit();
});
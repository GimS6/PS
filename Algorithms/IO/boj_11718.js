let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {

    let length = input.length;
    for (let i = 0; i < length; i++) {
        console.log(input[i]);
    }
    process.exit();
});
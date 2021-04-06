let readlien = require("readline");

let r = readlien.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {

    let unit = input[0];
    let numbers = input[1];
    let result = 0;

    for (let i = 0; i < unit; i++) {
        result += parseInt(numbers.charAt(i));
    }
    console.log(result);

    process.exit();
});
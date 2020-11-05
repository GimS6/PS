let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {

    let str = input[0];
    let length = str.length;
    let unit = parseInt(length / 10) + 1;

    for (let i = 0; i < unit; i++) {
        let start = i * 10;
        let end = start + 10;

        if (i == unit - 1) {
            console.log(str.slice(start, length));
            break
        }
        console.log(str.slice(start, end));
    }
    process.exit();
})
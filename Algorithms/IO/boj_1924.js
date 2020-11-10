let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    let date = input[0]
        .split(" ")
        .map((a) => {
            return a * 1
        });

    let m = date[0];
    let d = date[1];

    let day = new Date(2007, m - 1, d)

    console.log(
        new Intl.DateTimeFormat('en-US', { weekday: 'short' })
            .format(day)
            .toUpperCase()
    );

    process.exit();
});
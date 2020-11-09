let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {

    let md = input[0]
        .split(" ")
        .map((a) => {
            return a * 1
        });

    let m = md[0];
    let d = md[1];

    // new Date(2007, m, d) 형식으로 넣으면 원하는 날짜가 안 나옴.
    let date = new Date(`2007-${m}-${d}`).toLocaleString("en-us", { weekday: 'short' });
    console.log(date.toUpperCase())

    process.exit();
});

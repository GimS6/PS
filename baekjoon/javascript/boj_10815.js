const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let cnt = 0;
let cards;

r.on("line", (line) => {
    if (cnt == 0) {
        n = parseInt(line);
    } else if (cnt == 1) {
        cards = new Set(line.split(' ').map((a) => { return a * 1 }));
    } else if (cnt == 2) {
        m = parseInt(line);
    } else {
        console.log(line.split(" ").map((a) => { return cards.has(a*1) ? "1" : "0" }).join(" "));
        r.close();
    }
    cnt++;
});


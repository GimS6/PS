const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let xy = [];

r.on("line", (line) => {
    if (!n) {
        n = parseInt(line);
    } else {
        xy.push(line);
    }
}).on("close", () => {
    let mapped = xy.map((el, i) => {
        return { index: i, x: el.split(" ")[0], y: el.split(" ")[1] };
    });

    mapped.sort((a, b) => {
        if (a.x - b.x == 0) {
            return a.y - b.y
        }
        return a.x - b.x
    });

    let result = mapped.map((a) => {
        return a.x + " " + a.y
    });
    
    console.log(result.join("\n"));
    process.exit();
});
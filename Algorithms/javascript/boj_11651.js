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
    let mapped = xy.map((el) => {
        return { x: el.split(" ")[0], y: el.split(" ")[1] }
    });

    mapped.sort((a, b) => {
        if (a.y - b.y == 0) {
            return a.x - b.x
        }
        return a.y - b.y;
    });

    let result = mapped.map((el) => {
        return el.x + " " + el.y;
    });

    console.log(result.join("\n"));
    process.exit();
})
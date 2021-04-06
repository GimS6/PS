let editMax = 600000
let text = new Array(editMax).fill(0);
let prev = new Array(editMax).fill(-1);
let next = new Array(editMax).fill(-1);

let c = 0;
let unused = 1;

function insert(c, s) {
    text[unused] = s;
    prev[unused] = c;
    next[unused] = next[c];

    if (next[c] != -1) {
        prev[next[c]] = unused;
    }
    next[c] = unused;
    unused++;
}

function removeAt(c) {
    next[prev[c]] = next[c]
    if (next[c] != -1) {
        prev[next[c]] = prev[c]
    }
}

const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let s;
let n;

r.on("line", (line) => {
    if (!s) {
        s = line.split("");
        for (let i = 0; i < s.length; i++) {
            insert(c, s[i]);
            c++;
        }
    } else if (!n) {
        n = line;
    } else if (line == "L") {
        if (prev[c] != -1) {
            c = prev[c];
        }
    } else if (line == "D") {
        if (next[c] != -1) {
            c = next[c];
        }
    } else if (line == "B") {
        if (prev[c] != -1) {
            removeAt(c);
            c = prev[c];
        }
    } else {
        insert(c, line.split(" ")[1]);
        c = next[c];
    }
}).on("close", () => {
    let result = "";
    for (let i = next[0]; i != -1; i = next[i]) {
        result += text[i];
    }
    console.log(result);
    
    process.exit();
});
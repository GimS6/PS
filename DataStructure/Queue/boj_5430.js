// AC
class AC {
    constructor(arr, len) {
        this.arr = arr;
        this.front = 0;
        this.back = len - 1;
        this.size = len;
        this.order = true;
    }
    R() {
        this.order ? this.order = false : this.order = true;
    }
    D() {
        if (this.size == 0) {
            return false
        }
        this.order ? this.front++ : this.back--;
        this.size--;
        return true;
    }
    print() {
        let str = [];
        if (this.order) {
            for (let i = this.front; i < this.back + 1; i++) {
                str.push(this.arr[i]);
            }
            return str.join(",")
        }
        for (let i = this.back; i >= this.front; i--) {
            str.push(this.arr[i]);
        }
        return str.join(",");
    }
}

const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let T;
let C = [];

r.on("line", (line) => {
    !T ? T = parseInt(line) : C.push(line);
}).on("close", () => {
    let result = [];

    for (let i = 0; i < T * 3; i += 3) {
        let p = C[i].split("");
        let n = parseInt(C[i + 1]);
        let l = C[i + 2].slice(1, -1).split(",")

        let ac = new AC(l, n);

        let ok = true;
        p.forEach(element => {
            element == "R" ? ac.R() : ok = ac.D();
        });
        !ok ? result.push("error") : result.push(`[${ac.print()}]`);
    }

    console.log(result.join("\n"));
    process.exit();
});
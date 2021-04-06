const { time } = require("console");

// 요세푸스 문제
class CircularQueue {
    constructor(arr, point) {
        this.arr = arr;
        this.point = point - 1;
        this.unit = point-1;
        this.size = this.arr.length;
    }

    dequeue() {
        while(1) {
            let e = this.arr[this.point];
            this.arr.splice(this.point, 1)
            this.size--;
            this.rotate();
            return e
        }
    }
    rotate() {
        this.point = (this.point + this.unit) % this.arr.length;
    }
}

const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let result = [];

r.on("line", (line) => {
    const [n, K] = line.split(" ").map((a) => a*1);
    let N = [];
    for (i = 1; i <= n; i++) {
        N.push(i);
    }

    let cq = new CircularQueue(N, K);
    while(cq.size > 0) {
        result.push(cq.dequeue());
    }
}).on("close", () => {
    console.log(`<${result.join(", ")}>`);
    process.exit();
})
// 프린터 큐
class CircularQueue {
    constructor(arr, len) {
        this.arr = arr;
        this.size = len;
        this.cursor = 0;
    }
    dequeue() {
        const maxPrior = Math.max(...this.arr);
        while (1) {
            if (this.arr[this.cursor] == maxPrior) {
                this.arr[this.cursor] = 0;
                return this.cursor;
            }
            this.rotate();
        }
    }
    rotate() {
        this.cursor = (this.cursor + 1) % this.size;
    }
}

const readline = require('readline');
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

    for (let i = 0; i < T * 2; i += 2) {
        const [N, M] = C[i].split(" ").map((a) => { return a * 1 });
        let p = C[i + 1].split(" ").map((a) => { return a * 1 });

        let cq = new CircularQueue(p, N);

        let order = 1;
        while (cq.dequeue() !== M) {
            order++;
        }
        result.push(order);
    }

    console.log(result.join("\n"));
    process.exit();
});
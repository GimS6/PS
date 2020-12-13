// 요세푸스 문제
class CircularQueue {
    constructor(size) {
        this.element = [];
        this.size = size;
        this.length = 0;
        this.front = 0;
        this.back = -1;
    }

    isEmpty() {
        return (this.length == 0)
    }

    enqueue(element) {
        if (this.length >= this.size) throw (new Error("Maximum length exceeded"));
        this.back++;
        this.element[this.back % this.size] = element;
        this.length++;
    }

    dequeue() {
        if (this.isEmpty()) throw (new Error("No elements in the queue"));
        const value = this.getFront();
        this.element[this.front % this.size] = null;
        this.front++;
        this.length--;
        return value
    }

    getFront() {
        if (this.isEmpty()) throw (new Error("No elements in the queue"));
        return this.element[this.front % this.size];
    }
}

const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const max = 5000;
let cq = new CircularQueue(max);
let n;
let k;

r.on("line", (line) => {
    n = line.split(" ")[0];
    k = line.split(" ")[1];

}).on("close", () => {
    for (let i = 1; i <= n; i++) {
        cq.enqueue(i);
    }

    let permutation = [];
    for (let i = 0; i < n; i++) {
        let next = k % cq.length != 0 ? k % cq.length : cq.length;
        let removed;
        let cnt = 1;
        while (cnt <= k) {
            removed = cq.dequeue();
            if (cnt == next) { break }
            cnt++;
            cq.enqueue(removed);
        }
        permutation.push(removed);
    }

    console.log(`<${permutation.join(", ")}>`);
    process.exit();
});
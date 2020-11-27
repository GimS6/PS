function Deck() { this.initialize.apply(this, arguments); };
Deck.prototype.initialize = function () { return this._queue = []; };
Deck.prototype.pushFront = function (n) { return this._queue.unshift(n); };
Deck.prototype.pushBack = function (n) { return this._queue.push(n); };
Deck.prototype.popFront = function () { return this._queue.shift(); };
Deck.prototype.popBack = function () { return this._queue.pop(); };
Deck.prototype.size = function() { return this._queue.length; };
Deck.prototype.empty = function () { return !this._queue.length; };
Deck.prototype.front = function () { return this._queue[0]; };
Deck.prototype.back = function () { return this._queue[this._queue.length - 1]; };


const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let d = new Deck();
let result = [];

r.on("line", (line) => {
    if (!n) {
        n = line;
    } else if (line.startsWith("push_front")) {
        d.pushFront(parseInt(line.split(' ')[1]));
    } else if (line.startsWith("push_back")) {
        d.pushBack(parseInt(line.split(' ')[1]));
    } else if (line == "pop_front") {
        result.push(d.popFront() || "-1");
    } else if (line == "pop_back") {
        result.push(d.popBack() || "-1");
    } else if (line == "size") {
        result.push(d.size());
    } else if (line == "empty") {
        result.push(d.empty() ? "1" : "0");
    } else if (line == "front") {
        result.push(d.front() || "-1");
    } else if (line == "back") {
        result.push(d.back() || "-1");
    }
}).on("close", () => {
    console.log(result.join("\n"));
    process.exit();
});
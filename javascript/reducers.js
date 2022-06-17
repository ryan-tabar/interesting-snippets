const reducers = {
  odds: (acc, cur) => (cur % 2 ? acc + 1 : acc),
  evens: (acc, cur) => (cur % 2 ? acc : acc + 1),
  primes: (acc, cur) => {
    if (cur < 0) return acc;
    for (let i = 2; i <= cur; i++) {
      if (cur % i === 0) {
        return acc;
      }
    }
    return acc + 1;
  },
  perfectSquares: (acc, cur) =>
    cur < 0 ? acc : Math.sqrt(cur) % 1 === 0 ? acc + 1 : acc,
  perfectCubes: (acc, cur) => (Math.pow(cur, 1 / 3) % 1 === 0 ? acc + 1 : acc),
};

// add a map method to Objects to map the values
Object.prototype.map = function (callback) {
  return Object.values(this).map(callback);
};

const anArray = [25, 29, 16, 1, 2, 100, 11, 0, -25, -6];
const counts = reducers.map((reducer) => anArray.reduce(reducer, 0));
console.log(counts);
// 5, 5, 2, 5

// console.log([2, 4, 6, 8].every((num) => num % 2 === 0));
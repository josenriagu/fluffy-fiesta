var yourself = {
  // recursive, fails at higher values, unless memoization is implemented
  fibonacci: function (n) {
    if (n === 0) {
      return 0;
    } else if (n === 1) {
      return 1;
    } else {
      return this.fibonacci(n - 1) + this.fibonacci(n - 2);
    }
  },
  // a faster solution to beat time complexities
  fibo: function (n) {
    if (n < 2) {
      if (n < 0) return this.fibo(-n);
      return n;
    }
    let a = 0,
      b = 1,
      c;
    for (i = 2; i <= n; i++) {
      c = b + a;
      a = b;
      b = c;
    }
    return c;
  },
  // similar to fibo but with a while loop
  fib: function (n) {
    var a = 0,
      b = 1,
      c;
    if (n < 3) {
      if (n < 0) return this.fib(-n);
      if (n === 0) return 0;
      return 1;
    }
    while (--n) {
      c = a + b;
      a = b;
      b = c;
    }
    return c;
  },
};

console.log(yourself.fibonacci(4));
console.log(yourself.fibo(-2));
console.log(yourself.fibo(-1));
console.log(yourself.fibo(0));
console.log(yourself.fibo(100));
console.log(yourself.fib(-2));
console.log(yourself.fib(-1));
console.log(yourself.fib(0));
console.log(yourself.fib(100));

// Higher Order Function
function add(x){
    return function(y){
        return x+y
    }
}

console.log(add(5)(4))

// Callback Function
function callback(x, cb){
    return cb(x)
}

function compare(x){
    if (x > 100) return true
    return false
}
// using arrow function
// const compare = (x) => (x > 100 ? true : false);

console.log(callback(101, compare))
console.log(callback(20, compare))
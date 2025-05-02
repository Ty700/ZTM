// function addTo80(n){
//      console.log('Pretending to take forever to computer return value');
//      return n + 80
// }

// console.log(addTo80(5))

// console.log(addTo80(5))

// console.log(addTo80(5))

// console.log(addTo80(5))


/*
    Now what happens if we have a function that takes forever to return?

    We can cache the n value, that way if we call the same function with the same n value, we return the cached result rather than recomputing the return value
*/

function memizedAddTo80(){
    let cache = {};

    return function (n){
        if ( n in cache ) {
            console.log('n found in cache. Not recomputing');
            return cache[n]
        } else {
            console.log('... Long time to compute return value ...');
            cache[n] = n + 80;
            return cache[n];
        }
    }
}

const memoized = memizedAddTo80();

console.log(memoized(5));

console.log(memoized(6));

console.log(memoized(5));

// Thus memoization is just remembering 
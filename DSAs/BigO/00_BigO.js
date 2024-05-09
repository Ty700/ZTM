const nemo = ['nemo'];

const nemoCharacters = [
    "Marlin",
    "Dory",
    "Gill",
    "Bloat",
    "Peach",
    "Bubbles",
    "Deb / Flo",
    "Jacques",
    "Gurgle",
    "Nigel",
    "Crush",
    "Squirt",
    "Bruce",
    "Anchor",
    "Chum",
    "Mr. Ray",
    "Sheldon",
    "Tad",
    "Pearl",
    "Sheldon",
    "Crush",
    "Peach",
    "Jacques",
    "Nemo",
  ];

const large = new Array(10000).fill('nemo');

const {performance} = require('perf_hooks');

function findNemo(array){
    let t0 = performance.now();
    for(let i = 0; i < array.length; i++){
        if (array[i] === 'nemo'){
            console.log('Found Nemo!');
        }
    }
    let t1 = performance.now();

    return (t1 - t0);
}

small_array_time = findNemo(nemo);
medium_array_time = findNemo(nemoCharacters);
large_array_time = findNemo(large);

console.log('Small: ' + small_array_time + '\n');
console.log('Medium: ' + medium_array_time + '\n');
console.log('Large: ' + large_array_time + '\n');
/*  
    We see that as the input grows, the runtime increases pretty linearly. 
    So indexing an array is O(n) 
    I am not sure why the small one takes 3 milliseconds... but running it elsewhere shows it naught 0.0000000001
*/

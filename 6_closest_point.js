// https://www.codewars.com/kata/5376343a003bf6e034000c56/train/javascript

// Calculate a pair of closest points
function closestPair(points) {
  const pairsWithDistances = points.reduce((acc, curr, i) => [
    ...acc, 
    ...points.filter((x, j) => j > i).map(x => [curr, x])
  ], []).map(x => [x, (x[1][0]-x[0][0])**2 + (x[1][1]-x[0][1])**2]);
  const minDistance = Math.min(...pairsWithDistances.map(x => x[1]));
  return pairsWithDistances.filter(x => x[1] == minDistance).map(x => x[0]);
}


console.log(closestPair([
  [2,2], // A
  [2,8], // B
  [5,5], // C
  [6,3], // D
  [6,7], // E
  [7,4], // F
  [7,8]  // G
]));

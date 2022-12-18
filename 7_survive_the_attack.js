function hasSurvived(attackers, defenders) {
  let numbers = [attackers, defenders].map(x => x.length);
  const powers = [attackers, defenders].map(x => x.reduce((acc, curr) => acc + curr, 0));
  const counter = Math.max(...numbers);
  for (let i = 0; i < counter; i++) {
    const [a, d] = [attackers[i], defenders[i]];
    if (a >= d) numbers[1]--;
    if (a <= d) numbers[0]--;
    console.log([a, d])
    console.log(numbers)
  }
  return (numbers[1] > numbers[0])
    || ((numbers[1] === numbers[0]) && (powers[1] >= powers[0]))
}


console.log(
  hasSurvived([], [1, 2, 3])
);

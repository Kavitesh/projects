fn main() {
    let numbers = vec![1, 2, 3, 4, 5]; // Define a vector (dynamic array)
    let sum: i32 = numbers.iter().sum(); // Sum all elements
    println!("The sum of {:?} is {}", numbers, sum);
}

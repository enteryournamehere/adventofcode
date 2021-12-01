use std::env;
use std::fs;
use std::collections::VecDeque;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let contents = fs::read_to_string(filename)
        .expect("Could not read file");
    
    let mut increments: i32 = 0;
    let mut last_4 = VecDeque::with_capacity(4);
    for line in contents.lines() {
        let cur = line.parse::<i32>().unwrap();
        last_4.push_back(cur);
        if last_4.len() > 4 {
            last_4.pop_front();
        }
        if last_4.len() < 4 {
            continue;
        }
        let sum: i32 = last_4.iter().sum();
        let sum_1 = sum - last_4[3];
        let sum_2 = sum - last_4[0];
        if sum_2 > sum_1 {
            increments += 1;
        }
    }
    println!("{}", increments);
}

use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let contents = fs::read_to_string(filename)
        .expect("Could not read file");
    
    let mut increments: i32 = 0;
    let mut prev_opt: Option<i32> = None;
    for line in contents.lines() {
        let cur = line.parse::<i32>().unwrap();
        if let Some(prev) = prev_opt {
            if cur > prev {
                increments += 1;
            }
        }
        prev_opt = Some(cur);
    }
    println!("{}", increments);
}

use std::collections::btree_map::Range;
use std::io;


fn main() {
    let symbols = ["△", "□", "◇", "◯"];
    for symbol in symbols {
        println!("{}", symbol);
    }

    let amount:u32 = 1;
    for  i in 0..amount {
        println!("{i}");
    }

    println!("Please enter something:");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    println!("You entered: {}", input);

    // Tajusin tässä vaiheessa, että ei tämä ole hyvä idea.
}

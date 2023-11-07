use rand::random;
use rand::Rng;

// Arpoo 10 lukua väliltä 0-100 ja tulostaa montako niistä on tietyillä väleillä.

fn montako(lista: &[i32], alaraja: i32, ylaraja: i32) -> i32 {
    let mut laskuri = 0;
    for i in 0..lista.len() {
        if lista[i] >= alaraja && lista[i] <= ylaraja {
            laskuri += 1;
        }
    }
    return laskuri;
}


fn main() {
    let mut lista = [0; 10];
    for i in 0..lista.len() {
        // random i32 väliltä 0-100
        let mut rng = rand::thread_rng();
        lista[i] = rng.gen_range(0..=100);
        println!("{}", lista[i]);
    }

    println!("Montako lukua on välillä 0-10: {}", montako(&lista, 0, 10));
    println!("Montako lukua on välillä 50-100: {}", montako(&lista, 50, 100));
    println!("Montako lukua on välillä 67-75: {}", montako(&lista, 67, 75));
    
}
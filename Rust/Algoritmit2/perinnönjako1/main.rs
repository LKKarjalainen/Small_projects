use std::{fs::File, io::{self, BufRead}};

struct Person {
    id: i32,
    name: String,
    parents: (i32, i32),
    children: Vec<i32>,
    portion: f32,
    amount: i32,
}

fn format_input(input: String) -> (String, Vec<String>){
    let mut input_string = String::new();
    for line in input.lines() {
        input_string.push_str(line);
        input_string.push_str(" ");
    }
    input_string = {
        let mut new = input_string.trim().to_owned();
        while new.contains("  ") {
            new = new.replace("  ", " ");
        }
        new
    };
    let input_vec: Vec<String> = input_string.split(" ").map(|s| s.to_string()).collect();
    return (input_string, input_vec);
}

fn find_ends(input: &Vec<String>) -> Vec<usize> {
    let mut counter: i32 = 1;
    let mut iter: usize = 2;
    let mut ends: Vec<usize> = Vec::new();
    while iter < input.len() {
        if input[iter].parse::<i32>().unwrap().abs() != counter {
            ends.push(iter);
            if iter+1 < input.len() && input[iter+1].parse::<i32>().unwrap() == 0 {
                break;
            }
            counter = 1;
            iter += 3;
        }
        else {
            counter += 1;
            iter += 4; 
        }
    }
    return ends;
}

fn get_person(info: &[String], people: &Vec<Person>) -> Person {
    let id = info[0].parse::<i32>().unwrap();
    let name = info[1].to_string();
    let parent_a = {
        let info_number = info[2].parse::<i32>().unwrap();
        let mut id = info_number;
        if people[(info_number) as usize].id.is_negative() { id = -info_number; }
        id
    };
    let parent_b = {
        let info_number = info[3].parse::<i32>().unwrap();
        let mut id = info_number;
        if people[(info_number) as usize].id.is_negative() { id = -info_number; }
        id
    };
    let parents = (parent_a, parent_b);
    let children: Vec<i32> = Vec::new();
    return Person{id, name, parents, children, portion: 0.0, amount: 0};
}

fn find_descendants_alive(person_id: i32, people: &Vec<Person>) -> (i32, Vec<&Person>) {
    let person_index: usize = (person_id.abs()) as usize;
    let mut descendants = (0, Vec::new());
    if person_id > 0 {
        descendants.0 += 1;
        descendants.1.push(&people[person_index]);
    }
    else {
        for child_id in &people[person_index].children {
            let child_descendants = find_descendants_alive(*child_id, people);
            descendants.0 += child_descendants.0; 
            descendants.1.extend(child_descendants.1);
        }
    }
    return descendants;
}

fn distribute_portion(dead_id: i32, people: &mut Vec<Person>, portion: f32) {
    let dead_index: usize = (dead_id.abs()) as usize;
    let dead_descendants = find_descendants_alive(dead_id, people);
    if dead_id > 0 {
        people[dead_index].portion += portion;
        return;
    }
    if dead_descendants.0 == 0 {
        let parent_a_descendants = find_descendants_alive(people[dead_index].parents.0, people);
        let parent_b_descendants = find_descendants_alive(people[dead_index].parents.1, people);
        if parent_a_descendants.0 == 0 && parent_b_descendants.0 == 0 {
            people[0].portion += portion;
        }
        else {
            if parent_a_descendants.0 > 0 && parent_b_descendants.0 <= 0 {
                distribute_portion(people[dead_index].parents.0, people, portion);
            }
            else if parent_a_descendants.0 <= 0 && parent_b_descendants.0 > 0 {
                distribute_portion(people[dead_index].parents.1, people, portion);
            }
            else {
                distribute_portion(people[dead_index].parents.0, people, portion/2.0);
                distribute_portion(people[dead_index].parents.1, people, portion/2.0);
            }
        }
    }
    else {
        let mut children_with_descendants: Vec<i32> = Vec::new();
        for child in &people[dead_index].children {
            let child_descendants = find_descendants_alive(*child, people);
            if child_descendants.0 != 0 {
                children_with_descendants.push(*child);
            }
        }
        for child in &children_with_descendants {
            distribute_portion(*child, people, portion/children_with_descendants.len() as f32);
        }
    }
}

fn main() -> io::Result<()> {
    let start = std::time::Instant::now();
    let stdin = File::open("s4_3.txt")?;
    let input_source = io::BufReader::new(stdin).lines();
    //let stdin = io::stdin();
    //let input_source = stdin.lock().lines();
    let input: String = {
        let mut input: String = String::new();
        for line in input_source {
            input.push_str(&line.unwrap());
            input.push_str(" ");
        }
        input
    };
    let input: (String, Vec<String>) = format_input(input);
    if input.1.len() < 6 {
        return Ok(());
    }
    let ends: Vec<usize> = find_ends(&input.1);
    let mut dead_and_amounts: Vec<(i32, i32)> = Vec::new();
    dead_and_amounts.push((input.1[0].parse::<i32>().unwrap(), input.1[1].parse::<i32>().unwrap()));
    for i in 0..ends.len()-1 {
        dead_and_amounts.push((input.1[ends[i]+1].parse::<i32>().unwrap(), input.1[ends[i]+2].parse::<i32>().unwrap()));
    }

    let info = (&dead_and_amounts, &ends);
    
    let mut beneficiaries_global: Vec<Vec<Person>> = Vec::new();

    let tasks = info.0.len();
    for i in 0..tasks {
        let mut task_people: Vec<Person> = Vec::new();
        task_people.push(Person { id: 0, name: "Valtio".to_string(), parents: (0, 0), children: Vec::new(), portion: 0.0, amount: 0});
        let mut dead_id_and_amount: (i32, i32) = info.0[i];
        let end = info.1[i];
        let mut info_vec: Vec<String> = input.1[2..end].to_vec();
        if i != 0 {
            let start = ends[i-1]+3;
            let end = ends[i];
            info_vec = input.1[start..end].to_vec();
        }
        if info_vec.len() < 8 {
            task_people[0].portion += 1.0;
        }
        else {
            for i in 0..info_vec.len()/4 {
                let person = get_person(&info_vec[i*4..i*4+4], &task_people);
                task_people.push(person);
            }
            task_people[dead_id_and_amount.0.abs() as usize].portion += 1.0;
            dead_id_and_amount.0 = task_people[dead_id_and_amount.0 as usize].id;
    
            for i in 0..task_people.len()-1{
                let mut children: Vec<i32> = Vec::new();
                for j in i+1..task_people.len(){
                    if task_people[j].parents.0.abs() == task_people[i].id.abs() || task_people[j].parents.1.abs() == task_people[i].id.abs() {
                        children.push(task_people[j].id);
                    }
                }
                task_people[i].children.extend(children)
            }
    
            let dead_portion: f32 = task_people[dead_id_and_amount.0.abs() as usize].portion;
            distribute_portion(dead_id_and_amount.0, &mut task_people, dead_portion);
        }
        
        let mut beneficiaries: Vec<Person> = Vec::new();
        for person in task_people {
            if person.portion > 0.0 && (person.id > 0 || person.name == "Valtio"){
                let amount = (dead_id_and_amount.1 as f32 * person.portion) as i32;
                beneficiaries.push(Person { id: person.id, name: person.name, parents: person.parents, children: person.children, portion: person.portion, amount: amount});
            }
        }
        beneficiaries_global.push(beneficiaries);
    }

    for i in 0..beneficiaries_global.len() {
        let jaettavaa = dead_and_amounts[i].1;
        let mut jaettu = 0;
        for person in &beneficiaries_global[i] {
            println!("{} saa {}", person.name, person.amount);
            jaettu += person.amount;
        }
        println!("Jakamatta jää {}", jaettavaa - jaettu);
    }

    let end = std::time::Instant::now();
    println!("Time: {:?}", end-start);
    Ok(())
}

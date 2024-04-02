use std::{fs::File, io::{self, BufRead}};

struct Person {
    id: i32,
    name: String,
    parents: (i32, i32),
    children: Vec<i32>,
    amount: i32,
    benefactors: Vec<i32>,
    beneficiaries: Vec<i32>,
    has_distributed: bool,
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
        if people[info_number as usize].id.is_negative() { id = -info_number; }
        id
    };
    let parent_b = {
        let info_number = info[3].parse::<i32>().unwrap();
        let mut id = info_number;
        if people[info_number as usize].id.is_negative() { id = -info_number; }
        id
    };
    let parents = (parent_a, parent_b);
    let children: Vec<i32> = Vec::new();
    return Person{id, name, parents, children, amount: 0, benefactors: Vec::new(), beneficiaries: Vec::new(), has_distributed: false};
}

fn find_benefactors<'a> (people: &'a mut Vec<Person>, person_id: i32) {
    let person_index: usize = (person_id.abs()) as usize;
    let dead_descendants = find_descendants_alive(person_id, people, &mut (Vec::new(), false));
    if !dead_descendants {
        let parent_a = people[person_index].parents.0;
        let parent_a_descendants = find_descendants_alive(parent_a, people, &mut (Vec::new(), false));
        let parent_a_index: usize = (parent_a.abs()) as usize;

        let parent_b = people[person_index].parents.1;
        let parent_b_descendants = find_descendants_alive(parent_b, people, &mut (Vec::new(), false));
        let parent_b_index: usize = (parent_b.abs()) as usize;
        if !parent_a_descendants && !parent_b_descendants {
            people[0].benefactors.push(person_id);
            people[person_index].beneficiaries.push(0);
            return;
        }
        match parent_a_descendants {
            false => {

            },
            _ => {
                people[parent_a_index].benefactors.push(person_id);
                people[person_index].beneficiaries.push(parent_a);
            }
        }
        match parent_b_descendants {
            false => {

            },
            _ => {
                people[parent_b_index].benefactors.push(person_id);
                people[person_index].beneficiaries.push(parent_b);
            }
        }
        return;
    }
    else {
        for i in 0..people[person_index].children.len() {
            let child_id = people[person_index].children[i];
            let child_descendants = find_descendants_alive(child_id, people, &mut (Vec::new(), false));
            if child_descendants {
                if person_id <= 0 {
                    people[person_index].beneficiaries.push(child_id);
                    people[child_id.abs() as usize].benefactors.push(person_id);
                }
            }
        }
    }

}

fn find_descendants_alive<'a>(person_id: i32, people: &'a Vec<Person>, found: &'a mut (Vec<i32>, bool)) -> bool {
    if person_id == 0 {
        return false;
    }
    let person_index: usize = (person_id.abs()) as usize;
    let mut descendants = false;
    if person_id > 0 {
        found.0.push(person_id);
        descendants = true;
    }
    else {
        for child_id in &people[person_index].children {
            if !found.0.contains(child_id) {
                let child_descendants = find_descendants_alive(*child_id, people, found);
                if child_descendants == true {
                    descendants = true;
                }
            }
        }
        found.0.push(person_id);
    }
    return descendants;
}

fn distribute_money(person_id: i32, people: &mut Vec<Person>) {
    let person_index: usize = (person_id.abs()) as usize;
    let benefactors = people[person_index].benefactors.clone();
    for i in 0..benefactors.len() {
        let benefactor = benefactors[i];
        let benefactor_index: usize = (benefactor.abs()) as usize;
        let has_distributed = people[benefactor_index].has_distributed;
        if has_distributed == false {
            distribute_money(benefactor, people);
            people[benefactor_index].has_distributed = true;
        }
    }
    let beneficiaries = people[person_index].beneficiaries.clone();
    let amount = people[person_index].amount;
    let amount_per_beneficiary = (amount as f64 / beneficiaries.len() as f64).floor() as i32;
    for i in 0..beneficiaries.len() {
        let beneficiary = beneficiaries[i];
        let beneficiary_index: usize = (beneficiary.abs()) as usize;
        people[beneficiary_index].amount += amount_per_beneficiary;
        people[person_index].amount = 0;
    }
}

fn main() -> io::Result<()> {
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
        task_people.push(Person { id: 0, name: "Valtio".to_string(), parents: (0, 0), children: Vec::new(), amount: 0, benefactors: Vec::new(), beneficiaries: Vec::new(), has_distributed: false});
        let mut dead_id_and_amount: (i32, i32) = info.0[i];
        let end = info.1[i];
        let mut info_vec: Vec<String> = input.1[2..end].to_vec();
        if i != 0 {
            let start = ends[i-1]+3;
            let end = ends[i];
            info_vec = input.1[start..end].to_vec();
        }
        if info_vec.len() < 8 {
            task_people[0].amount += dead_id_and_amount.1;
        }
        else {
            for i in 0..info_vec.len()/4 {
                let person = get_person(&info_vec[i*4..i*4+4], &task_people);
                task_people.push(person);
            }
            dead_id_and_amount.0 = task_people[dead_id_and_amount.0 as usize].id;
            task_people[dead_id_and_amount.0.abs() as usize].amount = dead_id_and_amount.1;
    
            for i in 1..task_people.len()-1{
                let mut children: Vec<i32> = Vec::new();
                for j in i+1..task_people.len(){
                    if task_people[j].parents.0.abs() == task_people[i].id.abs() || task_people[j].parents.1.abs() == task_people[i].id.abs() {
                        children.push(task_people[j].id);
                    }
                }
                task_people[i].children.extend(children)
            }
    
            for i in 1..task_people.len() {
                let person_id = task_people[i].id;
                find_benefactors(&mut task_people, person_id);
            }
            let mut task_beneficiaries: Vec<i32> = Vec::new();
            for i in 0..task_people.len() {
                for j in 0..task_people[i].beneficiaries.len() {
                    let beneficiary = task_people[i].beneficiaries[j];
                    if !task_beneficiaries.contains(&beneficiary) {
                        task_beneficiaries.push(task_people[i].beneficiaries[j]);
                    }
                }
            }
            for task_beneficiary in task_beneficiaries {
                distribute_money(task_beneficiary, &mut task_people);
            }
        }
        
        let mut beneficiaries: Vec<Person> = Vec::new();
        for person in task_people {
            if person.amount > 0 && (person.id > 0 || person.name == "Valtio"){
                beneficiaries.push(Person { id: person.id, name: person.name, parents: person.parents, children: person.children, amount: person.amount, benefactors: person.benefactors, beneficiaries: person.beneficiaries, has_distributed: person.has_distributed});
            }
        }
        beneficiaries_global.push(beneficiaries);
    }

    for i in 0..beneficiaries_global.len() {
        let jaettavaa: i32 = dead_and_amounts[i].1;
        let mut jaettu: i32 = 0;
        for person in &beneficiaries_global[i] {
            let amount = person.amount;
            println!("{} saa {}", person.name, amount);
            jaettu += amount;
        }
        println!("Jakamatta jää {}", jaettavaa - jaettu);
    }

    Ok(())
}

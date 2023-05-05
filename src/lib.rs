use colored::Colorize;
 
pub fn info(message: &str) {
    println!("        {:#} {:#}", String::from("Info").blue().bold(), message);
}

pub fn warning(message: &str) {
    println!("     {:#} {:#}", String::from("Warning").yellow().bold(), message);
}

pub fn error(message: &str) {
    println!("       {:#} {:#}", String::from("Error").red().bold(), message);
}
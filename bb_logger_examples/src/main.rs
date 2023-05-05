extern crate bb_logger;

fn main() {
    bb_logger::info("This is some information!");
    bb_logger::warning("Be careful!");
    bb_logger::error("Something went wrong!");
}

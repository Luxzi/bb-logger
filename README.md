# bb-logger
![](https://badgen.net/github/checks/luxzi/bb-logger/) ![](https://badgen.net/github/last-commit/luxzi/bb-logger) ![](https://badgen.net/github/stars/luxzi/bb-logger)

Barebones logger for Rust.

This crate is in very early development, so watch out for bugs! Please also keep in mind that this `README.md` may be not be up to date due to rapid updates.

Report bugs [here](https://github.com/Luxzi/bb-logger/issues)

## Usage example

```rust
extern crate bb_logger;

fn main() {
    bb_logger::info("This is some information!");
    bb_logger::warning("Be careful!");
    bb_logger::error("Something went wrong!");
}

```

### Expected output:

![](https://i.imgur.com/a8A9tEu.png)

## Building & including:

Place the snippet below into your `Cargo.toml` under `[dependencies]` and make sure to swap out `"PATH TO CRATE HERE"` with the actual path to where you downloaded the crate. <b>Once this crate is considered "feature complete", it will be on crates.io instead but this is the temporary solution.</b>

```
bb_logger = { path = "PATH TO CRATE HERE" }
```

to reference the crate in your project use:

```rust
extern crate bb_logger;
```

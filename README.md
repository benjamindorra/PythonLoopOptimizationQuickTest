A quick test to compare pure Python, Numba, Numpy vectorization, and Rust binding for a simple sum over the squares of an array.
Extending https://www.linkedin.com/posts/mariuskwemou_datascience-python-numba-activity-7308089718397632513-3Fnq?utm_source=share&utm_medium=member_desktop&rcm=ACoAACKKBKQB_a44WE-RxIjA1thEBodf9qlnDHw

## Installation

### Clone the repo & cd in the directory

### Create the virtual environment
    1) $ python3 -m venv venv
    2) $ source venv/bin/activate
    3) $ pip install -r requirements.txt

### Compile the rust module
    1) $ cd rust_module
    2) $ maturin develop --release

## Run
    $ cd src
    $ python3 main.py --num_iters <number of times testing each module>

## Test
    $ pytest tests
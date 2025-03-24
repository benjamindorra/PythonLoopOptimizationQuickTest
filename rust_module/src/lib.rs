use pyo3::prelude::*;

// Sum of squares
#[pyfunction]
fn square_sum(x: Vec<i64>) -> PyResult<i64> {
    let mut result: i64 = 0;
    for i in x.iter() {
        result += i.pow(2);
    }
    Ok(result)
}

// Module to interface with Python
#[pymodule]
fn square_sum_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(square_sum, m)?)
}

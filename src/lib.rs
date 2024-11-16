use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use std::collections::HashMap;
use std::fs::File;
use zip::ZipArchive;
use std::io::Read;
use std::path::Path;
use quick_xml::reader::Reader;
use quick_xml::events::Event;


/// Extract comments from a Word (.docx) file.
///
/// Parameters
/// ----------
/// file_name : str
///     The path to the .docx file.
///
/// Returns
/// -------
/// list[dict[str, str]]
///     A list of comments, where each comment is a dictionary containing:
///     - "author": The author of the comment.
///     - "date": The date of the comment.
///     - "text": The text content of the comment.
///
/// Raises
/// ------
/// IOError
///     If the file cannot be opened or `comments.xml` is not found.
/// XMLParseError
///     If the `comments.xml` file cannot be parsed.
#[pyfunction]
fn get_comments(file_name: &str) -> PyResult<Vec<HashMap<String, String>>> {
    // Open the .docx file as a ZIP archive
    let file = File::open(file_name).map_err(|e| PyErr::new::<pyo3::exceptions::PyIOError, _>(format!("Failed to open file: {}", e)))?;
    let mut zip = ZipArchive::new(file).map_err(|e| PyErr::new::<pyo3::exceptions::PyIOError, _>(format!("Failed to read ZIP archive: {}", e)))?;

    // Extract the `comments.xml` file
    let mut comments_xml = String::new();
    if let Ok(mut comments_file) = zip.by_name("word/comments.xml") {
        comments_file.read_to_string(&mut comments_xml).map_err(|e| PyErr::new::<pyo3::exceptions::PyIOError, _>(format!("Failed to read comments.xml: {}", e)))?;
    } else {
        return Err(PyErr::new::<pyo3::exceptions::PyIOError, _>("comments.xml not found in the .docx file"));
    }

    // Parse the XML
    let mut reader = Reader::from_str(&comments_xml);
    reader.trim_text(true);
    let mut buf = Vec::new();

    let mut comments = Vec::new();
    let mut current_comment = HashMap::new();
    let mut inside_comment = false;

    loop {
        match reader.read_event(&mut buf) {
            Ok(Event::Start(ref e)) if e.name() == b"w:comment" => {
                inside_comment = true;
                current_comment.clear();

                for attr in e.attributes() {
                    let attr = attr.map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("Failed to read attribute: {}", e)))?;
                    match attr.key {
                        b"w:author" => {
                            current_comment.insert("author".to_string(), attr.unescape_and_decode_value(&reader).map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("Failed to decode author: {}", e)))?);
                        }
                        b"w:date" => {
                            current_comment.insert("date".to_string(), attr.unescape_and_decode_value(&reader).map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("Failed to decode date: {}", e)))?);
                        }
                        _ => {}
                    }
                }
            }
            Ok(Event::Text(e)) if inside_comment => {
                let text = e.unescape_and_decode(&reader).map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("Failed to decode text: {}", e)))?;
                current_comment.insert("text".to_string(), text);
            }
            Ok(Event::End(ref e)) if e.name() == b"w:comment" => {
                inside_comment = false;
                comments.push(current_comment.clone());
            }
            Ok(Event::Eof) => break,
            Err(e) => return Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("Error reading XML: {}", e))),
            _ => {}
        }
        buf.clear();
    }

    Ok(comments)
}

/// A Python module implemented in Rust.
#[pymodule]
fn _core(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_comments, m)?)?;
    Ok(())
}

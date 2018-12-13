# Dontpad API

This is an unofficial Dontpad Python API. 

## What is Dontpad?

Dontpad is an online notepad. Anyone can use it to share notes via web. All pages are public and it supports hierarchical note structures.

For a complete list of functionalities, please refer to the official website: 
www.dontpad.com

## Usage
### Python
To use the Python API simply import `dontpad.py` and proceed to using its methods.
```python
import dontpad
```
#### Methods
- `read`

    The `read` method receives a URL extension to look for in the Dontpad domain. It retrives the contents present at the location and returns a string. Optionally, you can set the `full_json` argument to `True` and receive a dictionary as a result. This dictionary contains the timestamp of the last update at this URL extension, its contents and a flag saying that the content was changed.

    Example code
    ```python
    >>> import dontpad
    >>> dontpad.read("url_extension")
    'This is a sample read response'
    >>> dontpad.read("url_extension", full_json=True)
    {'lastUpdate': 1519359497000, 'body': 'This is a sample read response', 'changed': True}
    ```
    
- `write`

    The `write` method stores a string to a given URL extension. Its first argument is the URL extension to which to upload the content. The following argument is a string containing the contents to be uploaded.

    Example code
    ```python
    >>> import dontpad
    >>> dontpad.write("url_extension", "Changed the contents of this note.")
    >>> dontpad.read("url_extension")
    'Changed the contents of this note.'
    ```
    
### CLI
This API also comes with a CLI. To use it, simply use the folloing formats.
- `reading`

    Uses the `read` method from the python API to retrieve data from the given URL extension. To use this mode, simply pass the `-r` flag to the CLI followed by the `url extension`. It's the default option if no flags are passed.

    Example code
    ```bash
    $ dontpad -r url_extension
    {'lastUpdate': 1519360432000, 'body': 'Changed the contents of this note.', 'changed': True}
    ```
    
- `writing`

    Analogously to the read argument, this uses the `write` method from the python API to update the contents of a given URL extension. To use this mode pass the `-w` flag followed by the `url extension`. All arguments passed henceforth are treated as a string to be uploaded.
    Example code
    ```bash
    $ dontpad -w url_extension Updating URL extension contents via CLI
    $ dontpad url_extension
    {'lastUpdate': 1519361155000, 'body': 'Updating URL extension contents via CLI', 'changed': True}
    ```






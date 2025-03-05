# Logs Module Documentation

## Overview
The `logs.py` module provides a `Logs` class that handles logging for various processes. It creates log directories and files based on the process name and date, and configures logging handlers.

## Class: Logs

### `__init__(self, process_name: str)`
Initializes the `Logs` class with the given process name.

- **Parameters:**
  - `process_name` (str): The name of the process for which logs are being created.

- **Example:**
  ```python
  log = Logs("my_process")



### `log.processDateTime(self)`
Creates a date directory based on the current date.

- **Examples:**
  ```python
  log.processDateTime()

\


### `log.setLoggerDate(self)`
Creates a date directory based on the current date.

- **Example:**
    ```python
    log.setHandlers()



### `log.initializeLogger(self, level_name:str)`
Initializes the logger with the specified log level.

- **Parameters:**=
    - `level_name` (str): The log level to be set (e.g., "DEBUG", "ERROR", "INFO", "WARNING", "CRITICAL").
    
- **Example:**
  ```python
  log.initializeLogger("DEBUG")




## Usage Example

```python
from logs import Logs

# Initialize the Logs class
log = Logs("my_process")

# Set the log level and initialize the logger
log.initializeLogger("DEBUG")
```

### Notes
- Ensure that the logs directory exists or will be created in the current working directory.
- The log files will be created in the format ./logs/<process_name>/<current_date>/<process_name>.log.

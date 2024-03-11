## Building

    poetry install --no-root

    cd src/js
    npm install
    npm run build

### Running examples

Examples can be found in the *./examples* folder.

    export PYTHONPATH=./src

    python -m examples.simple


### Debugging

Python VSCODE launch configurations are provided for each of the 
examples and for the pytest tests.

Javascript VSCODE launch configuration is provided for debugging the
browser code. For this to work the test application needs to be 
started with the env variable **REACTPY_DEBUG_MODE** set prior to 
running the application, eg:

    export REACTPY_DEBUG_MODE_JS=1 
    python -m examples.simple

Select the launch configuration **3a. Launch Chrome/Py**. You will
now be able to set breakpoints from within VSCODE. The javascript
source code is in **./src/js/src/*.js**

In addition, a simple react.js demo app *js\src\demo\App.jsx* is used to
debug the reactpy component without having to run python. The built-in
Vite server is used:

    npm run dev

Select the launch configuration **3b. Launch Chrome/JS**. You will
now be able to set breakpoints from within VSCODE.

## Testing

    playwright install

*Then:*

    pytest [--headed]

## Publish 

    rm -rf dist && poetry build
    poetry publish

Or publish to local repo

    poetry publish -r pypicloud

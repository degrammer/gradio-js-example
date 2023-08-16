---
title: Mlops Demo
emoji: 🏃
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 3.40.1
app_file: app.py
pinned: false
license: mit
---

![Hugging Face Logo](https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo.svg)

# How Runme elevates your Machine Learning Ops

This demo showcases the utilization of [Runme](https://runme.dev/), highlighting a combination of a Runbook Runner and the Runme CLI to enhance Machine Learning Operations through Continuous Integration (CI).

## Features

This is a [Hugging Face Space](https://huggingface.co/spaces) using the basic Gradio [example to customize JavaScript code](https://www.gradio.app/guides/custom-CSS-and-JS).
This project primarily aims to demonstrate the usage of Runme as a Runbook, coupled with a potent Runner for enhancing Runbook pipeline scripting. Specifically, we'll offer simple testable JavaScript functions in this example, accessible both locally and through CI. These functions are integrated within Gradio, with the advantage of maintaining separate JavaScript files to enhance discoverability and streamline development workflows.

Install dependencies

```sh
pip install gradio
```

## Prepare Injected JavaScript functions (requires [Node.js installed](https://nodejs.org/en/download))

All the required JavaScript files should be added as part of the out folder, the following script will generate the files automatically.
If you need to update or generate new functions, run the following script:

```javascript { name=inject-js }
const fs = require('fs')
const functions = require('./js')

Object.keys(functions).forEach((fn) => {
    fs.writeFile(`out/${fn}.js`,functions[fn].toString(), (error) => {
        if (error) {
            return console.error(`Failed to save function ${fn}`)
        }
        console.log(`Function saved ${fn}`)
    })
})
```

## Test JavaScript functions

To ensure an optimal developer experience, it's essential to validate the functionality of your custom JavaScript code reliably. Repeatedly manually running your Gradio app for testing can be cumbersome. By automating unit tests, you not only alleviate this burden but also enable the early identification of integration issues and bugs. This contributes significantly to a smoother development process.

Prior to testing your JavaScript functions within your Gradio app, it's advisable to create unit tests. This proactive approach ensures the correct functioning of your functions and helps you identify errors in advance, saving valuable time that would otherwise be spent on app debugging. Let's use again Node.js test runner to ensure everything works as expected, this can be used too as part of your CI process.

```javascript { name=test-js }
const { describe, it } = require('node:test')
const assert = require('node:assert')
const { reverseWords } = require('./js')

describe('Reverse words function', () => {
   it('Should reverse as expected', () => {
    assert.strictEqual(reverseWords(1,2,3), '3*2*1')
   })
})
```

You can also run the test suite using Runme CLI

```sh
runme run test-js
```

## Adding JavaScript functions to your Python code

Ensure you add all the required JavaScript functions to your app.py file

Start running your Gradio app

Ensure the previous cell is executed, otherwise your JavaScript functions will fail or the web app is not going to be executed at all

```sh
python app.py
```

Load the app with reload mode

```sh
gradio app.py
```

# Deploy to Hugging Face Space

Just use Git to push to main

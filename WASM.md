# TinyTapeout WASM Interface Documentation

All projects compiled to WebAssembly (WASM) in this repository share a common interface. This allows for a consistent way to interact with the simulations from JavaScript.

## Common Interface (C++)

The interface is defined in `src/scripts/wasm_top.cpp` and exposed via Emscripten's `EMSCRIPTEN_BINDINGS`.

### `ProjectWasm` Class

| Method | Type | Description |
|--------|------|-------------|
| `eval()` | `void` | Evaluates the model logic for the current state of inputs. |
| `set_ui_in(uint8_t val)` | `void` | Sets the 8-bit `ui_in` port. |
| `set_uio_in(uint8_t val)` | `void` | Sets the 8-bit `uio_in` port. |
| `set_ena(bool val)` | `void` | Sets the `ena` (enable) signal. |
| `set_clk(bool val)` | `void` | Sets the `clk` (clock) signal. |
| `set_rst_n(bool val)` | `void` | Sets the `rst_n` (active-low reset) signal. |
| `get_uo_out()` | `uint8_t` | Returns the current value of the 8-bit `uo_out` port. |
| `get_uio_out()` | `uint8_t` | Returns the current value of the 8-bit `uio_out` port. |
| `get_uio_oe()` | `uint8_t` | Returns the current value of the 8-bit `uio_oe` (output enable) port. |

## JavaScript Usage Example

Each WASM module is compiled with `MODULARIZE=1` and its `EXPORT_NAME` matches the project ID (e.g., `tt3404`).

### Loading a Module

In a Node.js or browser environment, you can load and use a project module as follows:

```javascript
// Import the module (assuming you are using Node.js or a bundler)
const tt3404 = require('./wasm/tt3404.js');

async function runSimulation() {
    // Instantiate the module
    const module = await tt3404();

    // Create an instance of the project
    const project = new module.ProjectWasm();

    // Initialize the project (Reset)
    project.set_rst_n(false);
    project.set_clk(false);
    project.eval();

    // Release reset
    project.set_rst_n(true);
    project.eval();

    // Set some inputs
    project.set_ui_in(0x55);
    project.eval();

    // Toggle clock
    project.set_clk(true);
    project.eval();
    project.set_clk(false);
    project.eval();

    // Read outputs
    const uo_out = project.get_uo_out();
    console.log(`uo_out: 0x${uo_out.toString(16)}`);

    // Clean up
    project.delete();
}

runSimulation();
```

## Compilation Details

The WASM modules are generated using `verilator` to create a C++ model of the Verilog/SystemVerilog source and `emcc` (Emscripten) to compile the wrapper and model into WASM.

- **Prefix**: `Vtop`
- **Output Files**: `wasm/ttXXXX.js`, `wasm/ttXXXX.wasm`
- **Emscripten Flags**: `-O3`, `--bind`, `-s MODULARIZE=1`, `-s EXPORT_NAME='ttXXXX'`, `-s ENVIRONMENT='web,node'`.

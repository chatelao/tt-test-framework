
#include <emscripten/bind.h>
#include <verilated.h>
#include <string>
#include "Vtop.h"
#include "metadata.h"

using namespace emscripten;

class ProjectWasm {
public:
    ProjectWasm() {
        top = new Vtop;
    }

    ~ProjectWasm() {
        delete top;
    }

    void eval() {
        top->eval();
    }

    void set_ui_in(uint8_t val) { top->ui_in = val; }
    void set_uio_in(uint8_t val) { top->uio_in = val; }
    void set_ena(bool val) { top->ena = val; }
    void set_clk(bool val) { top->clk = val; }
    void set_rst_n(bool val) { top->rst_n = val; }

    uint8_t get_uo_out() { return top->uo_out; }
    uint8_t get_uio_out() { return top->uio_out; }
    uint8_t get_uio_oe() { return top->uio_oe; }

    std::string get_description() { return PROJECT_DESCRIPTION; }
    std::string get_info_link() { return PROJECT_INFO_LINK; }
    std::string get_repo_link() { return PROJECT_REPO_LINK; }

private:
    Vtop* top;
};

EMSCRIPTEN_BINDINGS(project_wasm) {
    class_<ProjectWasm>("ProjectWasm")
        .constructor<>()
        .function("eval", &ProjectWasm::eval)
        .function("set_ui_in", &ProjectWasm::set_ui_in)
        .function("set_uio_in", &ProjectWasm::set_uio_in)
        .function("set_ena", &ProjectWasm::set_ena)
        .function("set_clk", &ProjectWasm::set_clk)
        .function("set_rst_n", &ProjectWasm::set_rst_n)
        .function("get_uo_out", &ProjectWasm::get_uo_out)
        .function("get_uio_out", &ProjectWasm::get_uio_out)
        .function("get_uio_oe", &ProjectWasm::get_uio_oe)
        .function("get_description", &ProjectWasm::get_description)
        .function("get_info_link", &ProjectWasm::get_info_link)
        .function("get_repo_link", &ProjectWasm::get_repo_link);
}

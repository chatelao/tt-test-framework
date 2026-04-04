// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See Vtop.h for the primary calling header

#ifndef VERILATED_VTOP___024ROOT_H_
#define VERILATED_VTOP___024ROOT_H_  // guard

#include "verilated.h"


class Vtop__Syms;

class alignas(VL_CACHE_LINE_BYTES) Vtop___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    VL_IN8(clk,0,0);
    VL_IN8(rst_n,0,0);
    VL_IN8(ui_in,7,0);
    VL_OUT8(uo_out,7,0);
    VL_IN8(uio_in,7,0);
    VL_OUT8(uio_out,7,0);
    VL_OUT8(uio_oe,7,0);
    VL_IN8(ena,0,0);
    CData/*7:0*/ tt_um_fir_filter__DOT__uart_data;
    CData/*0:0*/ tt_um_fir_filter__DOT__uart_valid;
    CData/*7:0*/ tt_um_fir_filter__DOT__coeff0;
    CData/*7:0*/ tt_um_fir_filter__DOT__coeff1;
    CData/*0:0*/ tt_um_fir_filter__DOT__coeff_we;
    CData/*0:0*/ tt_um_fir_filter__DOT__out_valid;
    CData/*7:0*/ tt_um_fir_filter__DOT__filtered_out;
    CData/*0:0*/ tt_um_fir_filter__DOT__u_uart_rx__DOT__rx_d1;
    CData/*0:0*/ tt_um_fir_filter__DOT__u_uart_rx__DOT__rx_d2;
    CData/*1:0*/ tt_um_fir_filter__DOT__u_uart_rx__DOT__state;
    CData/*2:0*/ tt_um_fir_filter__DOT__u_uart_rx__DOT__bit_idx;
    CData/*7:0*/ tt_um_fir_filter__DOT__u_uart_rx__DOT__shift_reg;
    CData/*2:0*/ tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state;
    CData/*7:0*/ tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__c0_buf;
    CData/*7:0*/ tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__c1_buf;
    CData/*7:0*/ tt_um_fir_filter__DOT__u_fir__DOT__d1;
    CData/*0:0*/ __VstlFirstIteration;
    CData/*0:0*/ __VicoFirstIteration;
    CData/*0:0*/ __Vtrigprevexpr___TOP__clk__0;
    CData/*0:0*/ __Vtrigprevexpr___TOP__rst_n__0;
    CData/*0:0*/ __VactContinue;
    SData/*15:0*/ tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt;
    IData/*17:0*/ tt_um_fir_filter__DOT__u_fir__DOT__shifted;
    IData/*31:0*/ __VactIterCount;
    VlTriggerVec<1> __VstlTriggered;
    VlTriggerVec<1> __VicoTriggered;
    VlTriggerVec<1> __VactTriggered;
    VlTriggerVec<1> __VnbaTriggered;

    // INTERNAL VARIABLES
    Vtop__Syms* const vlSymsp;

    // CONSTRUCTORS
    Vtop___024root(Vtop__Syms* symsp, const char* v__name);
    ~Vtop___024root();
    VL_UNCOPYABLE(Vtop___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard

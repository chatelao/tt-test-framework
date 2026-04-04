// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"
#include "Vtop___024root.h"

VL_INLINE_OPT void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ico_sequent__TOP__0\n"); );
    // Body
    vlSelf->tt_um_fir_filter__DOT__u_fir__DOT__shifted
        = (0x3ffffU & VL_SHIFTRS_III(18,18,32, (0x3ffffU
                                                & (VL_EXTENDS_II(18,16,
                                                                 (0xffffU
                                                                  & VL_MULS_III(16,
                                                                                (0xffffU
                                                                                & VL_EXTENDS_II(16,8, (IData)(vlSelf->tt_um_fir_filter__DOT__coeff0))),
                                                                                (0xffffU
                                                                                & VL_EXTENDS_II(16,8, (IData)(vlSelf->ui_in))))))
                                                   +
                                                   VL_EXTENDS_II(18,16,
                                                                 (0xffffU
                                                                  & VL_MULS_III(16,
                                                                                (0xffffU
                                                                                & VL_EXTENDS_II(16,8, (IData)(vlSelf->tt_um_fir_filter__DOT__coeff1))),
                                                                                (0xffffU
                                                                                & VL_EXTENDS_II(16,8, (IData)(vlSelf->tt_um_fir_filter__DOT__u_fir__DOT__d1)))))))), 7U));
}

void Vtop___024root___eval_ico(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_ico\n"); );
    // Body
    if ((1ULL & vlSelf->__VicoTriggered.word(0U))) {
        Vtop___024root___ico_sequent__TOP__0(vlSelf);
    }
}

void Vtop___024root___eval_triggers__ico(Vtop___024root* vlSelf);

bool Vtop___024root___eval_phase__ico(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__ico\n"); );
    // Init
    CData/*0:0*/ __VicoExecute;
    // Body
    Vtop___024root___eval_triggers__ico(vlSelf);
    __VicoExecute = vlSelf->__VicoTriggered.any();
    if (__VicoExecute) {
        Vtop___024root___eval_ico(vlSelf);
    }
    return (__VicoExecute);
}

void Vtop___024root___eval_act(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_act\n"); );
}

VL_INLINE_OPT void Vtop___024root___nba_sequent__TOP__0(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___nba_sequent__TOP__0\n"); );
    // Init
    CData/*1:0*/ __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state;
    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state = 0;
    SData/*15:0*/ __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt;
    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt = 0;
    CData/*2:0*/ __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state;
    __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state = 0;
    // Body
    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt
        = vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt;
    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state
        = vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__state;
    __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state
        = vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state;
    vlSelf->tt_um_fir_filter__DOT__out_valid = ((IData)(vlSelf->rst_n)
                                                && (1U
                                                    & ((IData)(vlSelf->uio_in)
                                                       >> 2U)));
    if (vlSelf->rst_n) {
        if ((4U & (IData)(vlSelf->uio_in))) {
            vlSelf->tt_um_fir_filter__DOT__filtered_out
                = (VL_LTS_III(18, 0x7fU, vlSelf->tt_um_fir_filter__DOT__u_fir__DOT__shifted)
                    ? 0x7fU : (VL_GTS_III(18, 0x3ff80U, vlSelf->tt_um_fir_filter__DOT__u_fir__DOT__shifted)
                                ? 0x80U : (0xffU & vlSelf->tt_um_fir_filter__DOT__u_fir__DOT__shifted)));
            vlSelf->tt_um_fir_filter__DOT__u_fir__DOT__d1
                = vlSelf->ui_in;
        }
        vlSelf->tt_um_fir_filter__DOT__coeff_we = 0U;
        if (vlSelf->tt_um_fir_filter__DOT__uart_valid) {
            if ((4U & (IData)(vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state))) {
                if ((2U & (IData)(vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state))) {
                    __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state = 0U;
                } else if ((1U & (IData)(vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state))) {
                    __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state = 0U;
                } else {
                    vlSelf->tt_um_fir_filter__DOT__coeff0
                        = vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__c0_buf;
                    vlSelf->tt_um_fir_filter__DOT__coeff1
                        = vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__c1_buf;
                    vlSelf->tt_um_fir_filter__DOT__coeff_we = 1U;
                    __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state = 0U;
                }
            } else if ((2U & (IData)(vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state))) {
                if ((1U & (IData)(vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state))) {
                    __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state = 4U;
                } else {
                    vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__c1_buf
                        = vlSelf->tt_um_fir_filter__DOT__uart_data;
                    __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state = 3U;
                }
            } else if ((1U & (IData)(vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state))) {
                vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__c0_buf
                    = vlSelf->tt_um_fir_filter__DOT__uart_data;
                __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state = 2U;
            } else if ((0xa5U == (IData)(vlSelf->tt_um_fir_filter__DOT__uart_data))) {
                __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state = 1U;
            }
        }
        vlSelf->tt_um_fir_filter__DOT__uart_valid = 0U;
        if ((2U & (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__state))) {
            if ((1U & (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__state))) {
                if ((0U == (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt))) {
                    if (vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__rx_d2) {
                        vlSelf->tt_um_fir_filter__DOT__uart_data
                            = vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__shift_reg;
                        vlSelf->tt_um_fir_filter__DOT__uart_valid = 1U;
                    }
                    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state = 0U;
                } else {
                    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt
                        = (0xffffU & ((IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt)
                                      - (IData)(1U)));
                }
            } else if ((0U == (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt))) {
                vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__shift_reg
                    = (((IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__rx_d2)
                        << 7U) | (0x7fU & ((IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__shift_reg)
                                           >> 1U)));
                if ((7U == (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__bit_idx))) {
                    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt = 0xa2cU;
                    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state = 3U;
                } else {
                    vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__bit_idx
                        = (7U & ((IData)(1U) + (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__bit_idx)));
                    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt = 0xa2cU;
                }
            } else {
                __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt
                    = (0xffffU & ((IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt)
                                  - (IData)(1U)));
            }
        } else if ((1U & (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__state))) {
            if ((0U == (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt))) {
                if (vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__rx_d2) {
                    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state = 0U;
                } else {
                    vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__bit_idx = 0U;
                    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt = 0xa2cU;
                    __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state = 2U;
                }
            } else {
                __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt
                    = (0xffffU & ((IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt)
                                  - (IData)(1U)));
            }
        } else if ((1U & (~ (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__rx_d2)))) {
            __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt = 0x516U;
            __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state = 1U;
        }
    } else {
        vlSelf->tt_um_fir_filter__DOT__filtered_out = 0U;
        vlSelf->tt_um_fir_filter__DOT__u_fir__DOT__d1 = 0U;
        __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state = 0U;
        vlSelf->tt_um_fir_filter__DOT__coeff_we = 0U;
        vlSelf->tt_um_fir_filter__DOT__coeff0 = 0x40U;
        vlSelf->tt_um_fir_filter__DOT__coeff1 = 0x40U;
        vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__c0_buf = 0U;
        vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__c1_buf = 0U;
        vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__bit_idx = 0U;
        vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__shift_reg = 0U;
        __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state = 0U;
        __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt = 0U;
        vlSelf->tt_um_fir_filter__DOT__uart_data = 0U;
        vlSelf->tt_um_fir_filter__DOT__uart_valid = 0U;
    }
    vlSelf->tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state
        = __Vdly__tt_um_fir_filter__DOT__u_coeff_ctrl__DOT__state;
    vlSelf->uo_out = vlSelf->tt_um_fir_filter__DOT__filtered_out;
    vlSelf->uio_out = (4U | (((IData)(vlSelf->tt_um_fir_filter__DOT__coeff_we)
                              << 4U) | ((IData)(vlSelf->tt_um_fir_filter__DOT__out_valid)
                                        << 3U)));
    vlSelf->tt_um_fir_filter__DOT__u_fir__DOT__shifted
        = (0x3ffffU & VL_SHIFTRS_III(18,18,32, (0x3ffffU
                                                & (VL_EXTENDS_II(18,16,
                                                                 (0xffffU
                                                                  & VL_MULS_III(16,
                                                                                (0xffffU
                                                                                & VL_EXTENDS_II(16,8, (IData)(vlSelf->tt_um_fir_filter__DOT__coeff0))),
                                                                                (0xffffU
                                                                                & VL_EXTENDS_II(16,8, (IData)(vlSelf->ui_in))))))
                                                   +
                                                   VL_EXTENDS_II(18,16,
                                                                 (0xffffU
                                                                  & VL_MULS_III(16,
                                                                                (0xffffU
                                                                                & VL_EXTENDS_II(16,8, (IData)(vlSelf->tt_um_fir_filter__DOT__coeff1))),
                                                                                (0xffffU
                                                                                & VL_EXTENDS_II(16,8, (IData)(vlSelf->tt_um_fir_filter__DOT__u_fir__DOT__d1)))))))), 7U));
    vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__state
        = __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__state;
    vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt
        = __Vdly__tt_um_fir_filter__DOT__u_uart_rx__DOT__baud_cnt;
    vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__rx_d2
        = ((1U & (~ (IData)(vlSelf->rst_n))) || (IData)(vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__rx_d1));
    vlSelf->tt_um_fir_filter__DOT__u_uart_rx__DOT__rx_d1
        = ((1U & (~ (IData)(vlSelf->rst_n))) || (1U
                                                 & (IData)(vlSelf->uio_in)));
}

void Vtop___024root___eval_nba(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_nba\n"); );
    // Body
    if ((1ULL & vlSelf->__VnbaTriggered.word(0U))) {
        Vtop___024root___nba_sequent__TOP__0(vlSelf);
    }
}

void Vtop___024root___eval_triggers__act(Vtop___024root* vlSelf);

bool Vtop___024root___eval_phase__act(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__act\n"); );
    // Init
    VlTriggerVec<1> __VpreTriggered;
    CData/*0:0*/ __VactExecute;
    // Body
    Vtop___024root___eval_triggers__act(vlSelf);
    __VactExecute = vlSelf->__VactTriggered.any();
    if (__VactExecute) {
        __VpreTriggered.andNot(vlSelf->__VactTriggered, vlSelf->__VnbaTriggered);
        vlSelf->__VnbaTriggered.thisOr(vlSelf->__VactTriggered);
        Vtop___024root___eval_act(vlSelf);
    }
    return (__VactExecute);
}

bool Vtop___024root___eval_phase__nba(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__nba\n"); );
    // Init
    CData/*0:0*/ __VnbaExecute;
    // Body
    __VnbaExecute = vlSelf->__VnbaTriggered.any();
    if (__VnbaExecute) {
        Vtop___024root___eval_nba(vlSelf);
        vlSelf->__VnbaTriggered.clear();
    }
    return (__VnbaExecute);
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(Vtop___024root* vlSelf);
#endif  // VL_DEBUG
#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__nba(Vtop___024root* vlSelf);
#endif  // VL_DEBUG
#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__act(Vtop___024root* vlSelf);
#endif  // VL_DEBUG

void Vtop___024root___eval(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval\n"); );
    // Init
    IData/*31:0*/ __VicoIterCount;
    CData/*0:0*/ __VicoContinue;
    IData/*31:0*/ __VnbaIterCount;
    CData/*0:0*/ __VnbaContinue;
    // Body
    __VicoIterCount = 0U;
    vlSelf->__VicoFirstIteration = 1U;
    __VicoContinue = 1U;
    while (__VicoContinue) {
        if (VL_UNLIKELY((0x64U < __VicoIterCount))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__ico(vlSelf);
#endif
            VL_FATAL_MT("temp_tt3576/src/tt_um_fir_filter.v", 20, "", "Input combinational region did not converge.");
        }
        __VicoIterCount = ((IData)(1U) + __VicoIterCount);
        __VicoContinue = 0U;
        if (Vtop___024root___eval_phase__ico(vlSelf)) {
            __VicoContinue = 1U;
        }
        vlSelf->__VicoFirstIteration = 0U;
    }
    __VnbaIterCount = 0U;
    __VnbaContinue = 1U;
    while (__VnbaContinue) {
        if (VL_UNLIKELY((0x64U < __VnbaIterCount))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__nba(vlSelf);
#endif
            VL_FATAL_MT("temp_tt3576/src/tt_um_fir_filter.v", 20, "", "NBA region did not converge.");
        }
        __VnbaIterCount = ((IData)(1U) + __VnbaIterCount);
        __VnbaContinue = 0U;
        vlSelf->__VactIterCount = 0U;
        vlSelf->__VactContinue = 1U;
        while (vlSelf->__VactContinue) {
            if (VL_UNLIKELY((0x64U < vlSelf->__VactIterCount))) {
#ifdef VL_DEBUG
                Vtop___024root___dump_triggers__act(vlSelf);
#endif
                VL_FATAL_MT("temp_tt3576/src/tt_um_fir_filter.v", 20, "", "Active region did not converge.");
            }
            vlSelf->__VactIterCount = ((IData)(1U)
                                       + vlSelf->__VactIterCount);
            vlSelf->__VactContinue = 0U;
            if (Vtop___024root___eval_phase__act(vlSelf)) {
                vlSelf->__VactContinue = 1U;
            }
        }
        if (Vtop___024root___eval_phase__nba(vlSelf)) {
            __VnbaContinue = 1U;
        }
    }
}

#ifdef VL_DEBUG
void Vtop___024root___eval_debug_assertions(Vtop___024root* vlSelf) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_debug_assertions\n"); );
    // Body
    if (VL_UNLIKELY((vlSelf->ena & 0xfeU))) {
        Verilated::overWidthError("ena");}
    if (VL_UNLIKELY((vlSelf->clk & 0xfeU))) {
        Verilated::overWidthError("clk");}
    if (VL_UNLIKELY((vlSelf->rst_n & 0xfeU))) {
        Verilated::overWidthError("rst_n");}
}
#endif  // VL_DEBUG

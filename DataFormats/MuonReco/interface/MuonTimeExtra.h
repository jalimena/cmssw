#ifndef MuonReco_MuonTimeExtra_h
#define MuonReco_MuonTimeExtra_h

/** \class reco::MuonTimeExtra MuonTimeExtra.h DataFormats/MuonReco/interface/MuonTimeExtra.h
 *  
 * A class holding timing information calculated for a muon. 
 *
 * \author Piotr Traczyk, CERN
 *
 * \version $Id: MuonTimeExtra.h,v 1.1 2009/03/27 02:35:08 ptraczyk Exp $
 *
 */

namespace reco {
 
  class MuonTimeExtra {
    public:
      MuonTimeExtra();

      enum Direction { OutsideIn = -1, Undefined = 0, InsideOut = 1 };

      /// number of measurements used in timing calculation
      int nDof() const { return nDof_; };
      void setNDof( const int nDof ) { nDof_=nDof; };
       
      /// 1/beta for prompt particle hypothesis 
      /// (time is constraint to the bunch crossing time)
      float inverseBeta()    const { return inverseBeta_; };
      float inverseBetaErr() const { return inverseBetaErr_; };
      void setInverseBeta( const float iBeta ) { inverseBeta_=iBeta; };
      void setInverseBetaErr( const float iBetaErr) { inverseBetaErr_=iBetaErr; };
       
      /// unconstrained 1/beta (time is free)
      /// Sign convention:
      ///   positive - outward moving particle
      ///   negative - inward moving particle
      float freeInverseBeta()    const { return freeInverseBeta_; };
      float freeInverseBetaErr() const { return freeInverseBetaErr_; };
      void setFreeInverseBeta( const float iBeta ) { freeInverseBeta_=iBeta; };
      void setFreeInverseBetaErr( const float iBetaErr) { freeInverseBetaErr_=iBetaErr; };

      /// time of arrival at the IP for the Beta=1 hypothesis
      ///  a) particle is moving from inside out
      float timeAtIpInOut()    const { return timeAtIpInOut_; }; 
      float timeAtIpInOutErr() const { return timeAtIpInOutErr_; };
      void setTimeAtIpInOut( const float timeIp )     { timeAtIpInOut_=timeIp; }; 
      void setTimeAtIpInOutErr( const float timeErr ) { timeAtIpInOutErr_=timeErr; };
      ///  b) particle is moving from outside in
      float timeAtIpOutIn()    const { return timeAtIpOutIn_; };
      float timeAtIpOutInErr() const { return timeAtIpOutInErr_; };
      void setTimeAtIpOutIn( const float timeIp )     { timeAtIpOutIn_=timeIp; }; 
      void setTimeAtIpOutInErr( const float timeErr ) { timeAtIpOutInErr_=timeErr; };
       
      /// direction estimation based on time dispersion
      Direction direction() const
      {
        if (nDof_<2) return Undefined;
        if ( timeAtIpInOutErr_ > timeAtIpOutInErr_ ) return OutsideIn;
        return InsideOut;
      }

      float aveHitTimeError()    const { return aveHitTimeError_; };
      float invbetaLS()    const { return invbetaLS_; };
      float yIntercept()    const { return yIntercept_; };
      float invbetaLSError()    const { return invbetaLSError_; };
      float yInterceptError()    const { return yInterceptError_; };
      float chi2Dof()    const { return chi2Dof_; };
      void setAveHitTimeError( const float aveHitTimeError ) { aveHitTimeError_=aveHitTimeError; };
      void setInvbetaLS( const float invbetaLS ) { invbetaLS_=invbetaLS; };
      void setYIntercept( const float yIntercept ) { yIntercept_=yIntercept; };
      void setInvbetaLSError( const float invbetaLSError ) { invbetaLSError_=invbetaLSError; };
      void setYInterceptError( const float yInterceptError ) { yInterceptError_=yInterceptError; };
      void setChi2Dof( const float chi2Dof ) { chi2Dof_=chi2Dof; };

      float localT00() const { return  local_t0_0_; };
      float localT01() const { return  local_t0_1_; };
      float localT02() const { return  local_t0_2_; };
      float localT03() const { return  local_t0_3_; };
      float localT04() const { return  local_t0_4_; };
      float localT05() const { return  local_t0_5_; };
      float localT06() const { return  local_t0_6_; };
      float localT07() const { return  local_t0_7_; };
      float localT08() const { return  local_t0_8_; };
      float localT09() const { return  local_t0_9_; };
      float localT010() const { return  local_t0_10_; };
      float localT011() const { return  local_t0_11_; };
      float localT012() const { return  local_t0_12_; };
      float localT013() const { return  local_t0_13_; };
      float localT014() const { return  local_t0_14_; };
      float localT015() const { return  local_t0_15_; };
      float localT016() const { return  local_t0_16_; };
      float localT017() const { return  local_t0_17_; };
      float localT018() const { return  local_t0_18_; };
      float localT019() const { return  local_t0_19_; };
      float localT020() const { return  local_t0_20_; };
      float localT021() const { return  local_t0_21_; };
      float localT022() const { return  local_t0_22_; };
      float localT023() const { return  local_t0_23_; };
      float localT024() const { return  local_t0_24_; };
      float localT025() const { return  local_t0_25_; };
      float localT026() const { return  local_t0_26_; };
      float localT027() const { return  local_t0_27_; };
      float localT028() const { return  local_t0_28_; };
      float localT029() const { return  local_t0_29_; };
      float localT030() const { return  local_t0_30_; };
      float localT031() const { return  local_t0_31_; };

      void setLocalT00(const float local_t0_0) { local_t0_0_=local_t0_0; };
      void setLocalT01(const float local_t0_1) { local_t0_1_=local_t0_1; };
      void setLocalT02(const float local_t0_2) { local_t0_2_=local_t0_2; };
      void setLocalT03(const float local_t0_3) { local_t0_3_=local_t0_3; };
      void setLocalT04(const float local_t0_4) { local_t0_4_=local_t0_4; };
      void setLocalT05(const float local_t0_5) { local_t0_5_=local_t0_5; };
      void setLocalT06(const float local_t0_6) { local_t0_6_=local_t0_6; };
      void setLocalT07(const float local_t0_7) { local_t0_7_=local_t0_7; };
      void setLocalT08(const float local_t0_8) { local_t0_8_=local_t0_8; };
      void setLocalT09(const float local_t0_9) { local_t0_9_=local_t0_9; };
      void setLocalT010(const float local_t0_10) { local_t0_10_=local_t0_10; };
      void setLocalT011(const float local_t0_11) { local_t0_11_=local_t0_11; };
      void setLocalT012(const float local_t0_12) { local_t0_12_=local_t0_12; };
      void setLocalT013(const float local_t0_13) { local_t0_13_=local_t0_13; };
      void setLocalT014(const float local_t0_14) { local_t0_14_=local_t0_14; };
      void setLocalT015(const float local_t0_15) { local_t0_15_=local_t0_15; };
      void setLocalT016(const float local_t0_16) { local_t0_16_=local_t0_16; };
      void setLocalT017(const float local_t0_17) { local_t0_17_=local_t0_17; };
      void setLocalT018(const float local_t0_18) { local_t0_18_=local_t0_18; };
      void setLocalT019(const float local_t0_19) { local_t0_19_=local_t0_19; };
      void setLocalT020(const float local_t0_20) { local_t0_20_=local_t0_20; };
      void setLocalT021(const float local_t0_21) { local_t0_21_=local_t0_21; };
      void setLocalT022(const float local_t0_22) { local_t0_22_=local_t0_22; };
      void setLocalT023(const float local_t0_23) { local_t0_23_=local_t0_23; };
      void setLocalT024(const float local_t0_24) { local_t0_24_=local_t0_24; };
      void setLocalT025(const float local_t0_25) { local_t0_25_=local_t0_25; };
      void setLocalT026(const float local_t0_26) { local_t0_26_=local_t0_26; };
      void setLocalT027(const float local_t0_27) { local_t0_27_=local_t0_27; };
      void setLocalT028(const float local_t0_28) { local_t0_28_=local_t0_28; };
      void setLocalT029(const float local_t0_29) { local_t0_29_=local_t0_29; };
      void setLocalT030(const float local_t0_30) { local_t0_30_=local_t0_30; };
      void setLocalT031(const float local_t0_31) { local_t0_31_=local_t0_31; };

      float correctedTime0() const { return  correctedTime_0_; };
      float correctedTime1() const { return  correctedTime_1_; };
      float correctedTime2() const { return  correctedTime_2_; };
      float correctedTime3() const { return  correctedTime_3_; };
      float correctedTime4() const { return  correctedTime_4_; };
      float correctedTime5() const { return  correctedTime_5_; };
      float correctedTime6() const { return  correctedTime_6_; };
      float correctedTime7() const { return  correctedTime_7_; };
      float correctedTime8() const { return  correctedTime_8_; };
      float correctedTime9() const { return  correctedTime_9_; };
      float correctedTime10() const { return  correctedTime_10_; };
      float correctedTime11() const { return  correctedTime_11_; };
      float correctedTime12() const { return  correctedTime_12_; };
      float correctedTime13() const { return  correctedTime_13_; };
      float correctedTime14() const { return  correctedTime_14_; };
      float correctedTime15() const { return  correctedTime_15_; };
      float correctedTime16() const { return  correctedTime_16_; };
      float correctedTime17() const { return  correctedTime_17_; };
      float correctedTime18() const { return  correctedTime_18_; };
      float correctedTime19() const { return  correctedTime_19_; };
      float correctedTime20() const { return  correctedTime_20_; };
      float correctedTime21() const { return  correctedTime_21_; };
      float correctedTime22() const { return  correctedTime_22_; };
      float correctedTime23() const { return  correctedTime_23_; };
      float correctedTime24() const { return  correctedTime_24_; };
      float correctedTime25() const { return  correctedTime_25_; };
      float correctedTime26() const { return  correctedTime_26_; };
      float correctedTime27() const { return  correctedTime_27_; };
      float correctedTime28() const { return  correctedTime_28_; };
      float correctedTime29() const { return  correctedTime_29_; };
      float correctedTime30() const { return  correctedTime_30_; };
      float correctedTime31() const { return  correctedTime_31_; };

      void setCorrectedTime0(const float correctedTime_0) { correctedTime_0_=correctedTime_0; };
      void setCorrectedTime1(const float correctedTime_1) { correctedTime_1_=correctedTime_1; };
      void setCorrectedTime2(const float correctedTime_2) { correctedTime_2_=correctedTime_2; };
      void setCorrectedTime3(const float correctedTime_3) { correctedTime_3_=correctedTime_3; };
      void setCorrectedTime4(const float correctedTime_4) { correctedTime_4_=correctedTime_4; };
      void setCorrectedTime5(const float correctedTime_5) { correctedTime_5_=correctedTime_5; };
      void setCorrectedTime6(const float correctedTime_6) { correctedTime_6_=correctedTime_6; };
      void setCorrectedTime7(const float correctedTime_7) { correctedTime_7_=correctedTime_7; };
      void setCorrectedTime8(const float correctedTime_8) { correctedTime_8_=correctedTime_8; };
      void setCorrectedTime9(const float correctedTime_9) { correctedTime_9_=correctedTime_9; };
      void setCorrectedTime10(const float correctedTime_10) { correctedTime_10_=correctedTime_10; };
      void setCorrectedTime11(const float correctedTime_11) { correctedTime_11_=correctedTime_11; };
      void setCorrectedTime12(const float correctedTime_12) { correctedTime_12_=correctedTime_12; };
      void setCorrectedTime13(const float correctedTime_13) { correctedTime_13_=correctedTime_13; };
      void setCorrectedTime14(const float correctedTime_14) { correctedTime_14_=correctedTime_14; };
      void setCorrectedTime15(const float correctedTime_15) { correctedTime_15_=correctedTime_15; };
      void setCorrectedTime16(const float correctedTime_16) { correctedTime_16_=correctedTime_16; };
      void setCorrectedTime17(const float correctedTime_17) { correctedTime_17_=correctedTime_17; };
      void setCorrectedTime18(const float correctedTime_18) { correctedTime_18_=correctedTime_18; };
      void setCorrectedTime19(const float correctedTime_19) { correctedTime_19_=correctedTime_19; };
      void setCorrectedTime20(const float correctedTime_20) { correctedTime_20_=correctedTime_20; };
      void setCorrectedTime21(const float correctedTime_21) { correctedTime_21_=correctedTime_21; };
      void setCorrectedTime22(const float correctedTime_22) { correctedTime_22_=correctedTime_22; };
      void setCorrectedTime23(const float correctedTime_23) { correctedTime_23_=correctedTime_23; };
      void setCorrectedTime24(const float correctedTime_24) { correctedTime_24_=correctedTime_24; };
      void setCorrectedTime25(const float correctedTime_25) { correctedTime_25_=correctedTime_25; };
      void setCorrectedTime26(const float correctedTime_26) { correctedTime_26_=correctedTime_26; };
      void setCorrectedTime27(const float correctedTime_27) { correctedTime_27_=correctedTime_27; };
      void setCorrectedTime28(const float correctedTime_28) { correctedTime_28_=correctedTime_28; };
      void setCorrectedTime29(const float correctedTime_29) { correctedTime_29_=correctedTime_29; };
      void setCorrectedTime30(const float correctedTime_30) { correctedTime_30_=correctedTime_30; };
      void setCorrectedTime31(const float correctedTime_31) { correctedTime_31_=correctedTime_31; };

      float distance0() const { return  distance_0_; };
      float distance1() const { return  distance_1_; };
      float distance2() const { return  distance_2_; };
      float distance3() const { return  distance_3_; };
      float distance4() const { return  distance_4_; };
      float distance5() const { return  distance_5_; };
      float distance6() const { return  distance_6_; };
      float distance7() const { return  distance_7_; };
      float distance8() const { return  distance_8_; };
      float distance9() const { return  distance_9_; };
      float distance10() const { return  distance_10_; };
      float distance11() const { return  distance_11_; };
      float distance12() const { return  distance_12_; };
      float distance13() const { return  distance_13_; };
      float distance14() const { return  distance_14_; };
      float distance15() const { return  distance_15_; };
      float distance16() const { return  distance_16_; };
      float distance17() const { return  distance_17_; };
      float distance18() const { return  distance_18_; };
      float distance19() const { return  distance_19_; };
      float distance20() const { return  distance_20_; };
      float distance21() const { return  distance_21_; };
      float distance22() const { return  distance_22_; };
      float distance23() const { return  distance_23_; };
      float distance24() const { return  distance_24_; };
      float distance25() const { return  distance_25_; };
      float distance26() const { return  distance_26_; };
      float distance27() const { return  distance_27_; };
      float distance28() const { return  distance_28_; };
      float distance29() const { return  distance_29_; };
      float distance30() const { return  distance_30_; };
      float distance31() const { return  distance_31_; };

      void setDistance0(const float distance_0) { distance_0_=distance_0; };
      void setDistance1(const float distance_1) { distance_1_=distance_1; };
      void setDistance2(const float distance_2) { distance_2_=distance_2; };
      void setDistance3(const float distance_3) { distance_3_=distance_3; };
      void setDistance4(const float distance_4) { distance_4_=distance_4; };
      void setDistance5(const float distance_5) { distance_5_=distance_5; };
      void setDistance6(const float distance_6) { distance_6_=distance_6; };
      void setDistance7(const float distance_7) { distance_7_=distance_7; };
      void setDistance8(const float distance_8) { distance_8_=distance_8; };
      void setDistance9(const float distance_9) { distance_9_=distance_9; };
      void setDistance10(const float distance_10) { distance_10_=distance_10; };
      void setDistance11(const float distance_11) { distance_11_=distance_11; };
      void setDistance12(const float distance_12) { distance_12_=distance_12; };
      void setDistance13(const float distance_13) { distance_13_=distance_13; };
      void setDistance14(const float distance_14) { distance_14_=distance_14; };
      void setDistance15(const float distance_15) { distance_15_=distance_15; };
      void setDistance16(const float distance_16) { distance_16_=distance_16; };
      void setDistance17(const float distance_17) { distance_17_=distance_17; };
      void setDistance18(const float distance_18) { distance_18_=distance_18; };
      void setDistance19(const float distance_19) { distance_19_=distance_19; };
      void setDistance20(const float distance_20) { distance_20_=distance_20; };
      void setDistance21(const float distance_21) { distance_21_=distance_21; };
      void setDistance22(const float distance_22) { distance_22_=distance_22; };
      void setDistance23(const float distance_23) { distance_23_=distance_23; };
      void setDistance24(const float distance_24) { distance_24_=distance_24; };
      void setDistance25(const float distance_25) { distance_25_=distance_25; };
      void setDistance26(const float distance_26) { distance_26_=distance_26; };
      void setDistance27(const float distance_27) { distance_27_=distance_27; };
      void setDistance28(const float distance_28) { distance_28_=distance_28; };
      void setDistance29(const float distance_29) { distance_29_=distance_29; };
      void setDistance30(const float distance_30) { distance_30_=distance_30; };
      void setDistance31(const float distance_31) { distance_31_=distance_31; };

      float hitChisq0() const { return  hitChisq_0_; };
      float hitChisq1() const { return  hitChisq_1_; };
      float hitChisq2() const { return  hitChisq_2_; };
      float hitChisq3() const { return  hitChisq_3_; };
      float hitChisq4() const { return  hitChisq_4_; };
      float hitChisq5() const { return  hitChisq_5_; };
      float hitChisq6() const { return  hitChisq_6_; };
      float hitChisq7() const { return  hitChisq_7_; };
      float hitChisq8() const { return  hitChisq_8_; };
      float hitChisq9() const { return  hitChisq_9_; };
      float hitChisq10() const { return  hitChisq_10_; };
      float hitChisq11() const { return  hitChisq_11_; };
      float hitChisq12() const { return  hitChisq_12_; };
      float hitChisq13() const { return  hitChisq_13_; };
      float hitChisq14() const { return  hitChisq_14_; };
      float hitChisq15() const { return  hitChisq_15_; };
      float hitChisq16() const { return  hitChisq_16_; };
      float hitChisq17() const { return  hitChisq_17_; };
      float hitChisq18() const { return  hitChisq_18_; };
      float hitChisq19() const { return  hitChisq_19_; };
      float hitChisq20() const { return  hitChisq_20_; };
      float hitChisq21() const { return  hitChisq_21_; };
      float hitChisq22() const { return  hitChisq_22_; };
      float hitChisq23() const { return  hitChisq_23_; };
      float hitChisq24() const { return  hitChisq_24_; };
      float hitChisq25() const { return  hitChisq_25_; };
      float hitChisq26() const { return  hitChisq_26_; };
      float hitChisq27() const { return  hitChisq_27_; };
      float hitChisq28() const { return  hitChisq_28_; };
      float hitChisq29() const { return  hitChisq_29_; };
      float hitChisq30() const { return  hitChisq_30_; };
      float hitChisq31() const { return  hitChisq_31_; };

      void setHitChisq0(const float hitChisq_0) { hitChisq_0_=hitChisq_0; };
      void setHitChisq1(const float hitChisq_1) { hitChisq_1_=hitChisq_1; };
      void setHitChisq2(const float hitChisq_2) { hitChisq_2_=hitChisq_2; };
      void setHitChisq3(const float hitChisq_3) { hitChisq_3_=hitChisq_3; };
      void setHitChisq4(const float hitChisq_4) { hitChisq_4_=hitChisq_4; };
      void setHitChisq5(const float hitChisq_5) { hitChisq_5_=hitChisq_5; };
      void setHitChisq6(const float hitChisq_6) { hitChisq_6_=hitChisq_6; };
      void setHitChisq7(const float hitChisq_7) { hitChisq_7_=hitChisq_7; };
      void setHitChisq8(const float hitChisq_8) { hitChisq_8_=hitChisq_8; };
      void setHitChisq9(const float hitChisq_9) { hitChisq_9_=hitChisq_9; };
      void setHitChisq10(const float hitChisq_10) { hitChisq_10_=hitChisq_10; };
      void setHitChisq11(const float hitChisq_11) { hitChisq_11_=hitChisq_11; };
      void setHitChisq12(const float hitChisq_12) { hitChisq_12_=hitChisq_12; };
      void setHitChisq13(const float hitChisq_13) { hitChisq_13_=hitChisq_13; };
      void setHitChisq14(const float hitChisq_14) { hitChisq_14_=hitChisq_14; };
      void setHitChisq15(const float hitChisq_15) { hitChisq_15_=hitChisq_15; };
      void setHitChisq16(const float hitChisq_16) { hitChisq_16_=hitChisq_16; };
      void setHitChisq17(const float hitChisq_17) { hitChisq_17_=hitChisq_17; };
      void setHitChisq18(const float hitChisq_18) { hitChisq_18_=hitChisq_18; };
      void setHitChisq19(const float hitChisq_19) { hitChisq_19_=hitChisq_19; };
      void setHitChisq20(const float hitChisq_20) { hitChisq_20_=hitChisq_20; };
      void setHitChisq21(const float hitChisq_21) { hitChisq_21_=hitChisq_21; };
      void setHitChisq22(const float hitChisq_22) { hitChisq_22_=hitChisq_22; };
      void setHitChisq23(const float hitChisq_23) { hitChisq_23_=hitChisq_23; };
      void setHitChisq24(const float hitChisq_24) { hitChisq_24_=hitChisq_24; };
      void setHitChisq25(const float hitChisq_25) { hitChisq_25_=hitChisq_25; };
      void setHitChisq26(const float hitChisq_26) { hitChisq_26_=hitChisq_26; };
      void setHitChisq27(const float hitChisq_27) { hitChisq_27_=hitChisq_27; };
      void setHitChisq28(const float hitChisq_28) { hitChisq_28_=hitChisq_28; };
      void setHitChisq29(const float hitChisq_29) { hitChisq_29_=hitChisq_29; };
      void setHitChisq30(const float hitChisq_30) { hitChisq_30_=hitChisq_30; };
      void setHitChisq31(const float hitChisq_31) { hitChisq_31_=hitChisq_31; };
     
    private:

      /// number of measurements used in timing calculation
      int nDof_;
       
      /// 1/beta for prompt particle hypothesis 
      float inverseBeta_;
      float inverseBetaErr_;
       
      /// unconstrained 1/beta (time is free)
      float freeInverseBeta_;
      float freeInverseBetaErr_;

      /// time of arrival at the IP for the Beta=1 hypothesis
      float timeAtIpInOut_;
      float timeAtIpInOutErr_;
      float timeAtIpOutIn_;
      float timeAtIpOutInErr_;

      float aveHitTimeError_;
      float invbetaLS_;
      float yIntercept_;
      float invbetaLSError_;
      float yInterceptError_;
      float chi2Dof_;

      float local_t0_0_;
      float local_t0_1_;
      float local_t0_2_;
      float local_t0_3_;
      float local_t0_4_;
      float local_t0_5_;
      float local_t0_6_;
      float local_t0_7_;
      float local_t0_8_;
      float local_t0_9_;
      float local_t0_10_;
      float local_t0_11_;
      float local_t0_12_;
      float local_t0_13_;
      float local_t0_14_;
      float local_t0_15_;
      float local_t0_16_;
      float local_t0_17_;
      float local_t0_18_;
      float local_t0_19_;
      float local_t0_20_;
      float local_t0_21_;
      float local_t0_22_;
      float local_t0_23_;
      float local_t0_24_;
      float local_t0_25_;
      float local_t0_26_;
      float local_t0_27_;
      float local_t0_28_;
      float local_t0_29_;
      float local_t0_30_;
      float local_t0_31_;

      float correctedTime_0_;
      float correctedTime_1_;
      float correctedTime_2_;
      float correctedTime_3_;
      float correctedTime_4_;
      float correctedTime_5_;
      float correctedTime_6_;
      float correctedTime_7_;
      float correctedTime_8_;
      float correctedTime_9_;
      float correctedTime_10_;
      float correctedTime_11_;
      float correctedTime_12_;
      float correctedTime_13_;
      float correctedTime_14_;
      float correctedTime_15_;
      float correctedTime_16_;
      float correctedTime_17_;
      float correctedTime_18_;
      float correctedTime_19_;
      float correctedTime_20_;
      float correctedTime_21_;
      float correctedTime_22_;
      float correctedTime_23_;
      float correctedTime_24_;
      float correctedTime_25_;
      float correctedTime_26_;
      float correctedTime_27_;
      float correctedTime_28_;
      float correctedTime_29_;
      float correctedTime_30_;
      float correctedTime_31_;

      float distance_0_;
      float distance_1_;
      float distance_2_;
      float distance_3_;
      float distance_4_;
      float distance_5_;
      float distance_6_;
      float distance_7_;
      float distance_8_;
      float distance_9_;
      float distance_10_;
      float distance_11_;
      float distance_12_;
      float distance_13_;
      float distance_14_;
      float distance_15_;
      float distance_16_;
      float distance_17_;
      float distance_18_;
      float distance_19_;
      float distance_20_;
      float distance_21_;
      float distance_22_;
      float distance_23_;
      float distance_24_;
      float distance_25_;
      float distance_26_;
      float distance_27_;
      float distance_28_;
      float distance_29_;
      float distance_30_;
      float distance_31_;

      float hitChisq_0_;
      float hitChisq_1_;
      float hitChisq_2_;
      float hitChisq_3_;
      float hitChisq_4_;
      float hitChisq_5_;
      float hitChisq_6_;
      float hitChisq_7_;
      float hitChisq_8_;
      float hitChisq_9_;
      float hitChisq_10_;
      float hitChisq_11_;
      float hitChisq_12_;
      float hitChisq_13_;
      float hitChisq_14_;
      float hitChisq_15_;
      float hitChisq_16_;
      float hitChisq_17_;
      float hitChisq_18_;
      float hitChisq_19_;
      float hitChisq_20_;
      float hitChisq_21_;
      float hitChisq_22_;
      float hitChisq_23_;
      float hitChisq_24_;
      float hitChisq_25_;
      float hitChisq_26_;
      float hitChisq_27_;
      float hitChisq_28_;
      float hitChisq_29_;
      float hitChisq_30_;
      float hitChisq_31_;
      
  };

}

#endif

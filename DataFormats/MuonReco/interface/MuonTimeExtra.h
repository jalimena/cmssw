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

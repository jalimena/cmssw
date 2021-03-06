#ifndef FWCore_Framework_one_EDFilterBase_h
#define FWCore_Framework_one_EDFilterBase_h
// -*- C++ -*-
//
// Package:     FWCore/Framework
// Class  :     one::EDFilterBase
// 
/**\class one::EDFilterBase EDFilterBase.h "FWCore/Framework/interface/one/EDFilterBase.h"

 Description: Base class for edm::one::EDFilter<>

 Usage:
    <usage>

*/
//
// Original Author:  Chris Jones
//         Created:  Thu, 02 May 2013 21:21:21 GMT
//

// system include files

// user include files
#include "FWCore/Framework/interface/ProducerBase.h"
#include "FWCore/Framework/interface/EDConsumerBase.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DataFormats/Provenance/interface/ModuleDescription.h"
#include "FWCore/ParameterSet/interface/ParameterSetfwd.h"

// forward declarations
namespace edm {
  namespace one {

    class EDFilterBase : public ProducerBase, public EDConsumerBase
    {
      
    public:
      template <typename T> friend class edm::WorkerT;
      typedef EDFilterBase ModuleType;
      typedef WorkerT<EDFilterBase> WorkerType;

      
      EDFilterBase();
      virtual ~EDFilterBase();
      
      static void fillDescriptions(ConfigurationDescriptions& descriptions);
      static void prevalidate(ConfigurationDescriptions& descriptions);
      static const std::string& baseType();

    protected:
      // The returned pointer will be null unless the this is currently
      // executing its event loop function ('produce').
      CurrentProcessingContext const* currentContext() const;
      
    private:
      bool doEvent(EventPrincipal& ep, EventSetup const& c,
                   CurrentProcessingContext const* cpcp);
      void doBeginJob();
      void doEndJob();
      
      void doBeginRun(RunPrincipal& rp, EventSetup const& c,
                      CurrentProcessingContext const* cpc);
      void doEndRun(RunPrincipal& rp, EventSetup const& c,
                    CurrentProcessingContext const* cpc);
      void doBeginLuminosityBlock(LuminosityBlockPrincipal& lbp, EventSetup const& c,
                                  CurrentProcessingContext const* cpc);
      void doEndLuminosityBlock(LuminosityBlockPrincipal& lbp, EventSetup const& c,
                                CurrentProcessingContext const* cpc);
      
      //For now, the following are just dummy implemenations with no ability for users to override
      void doRespondToOpenInputFile(FileBlock const& fb);
      void doRespondToCloseInputFile(FileBlock const& fb);
      void doPreForkReleaseResources();
      void doPostForkReacquireResources(unsigned int iChildIndex, unsigned int iNumberOfChildren);

      
      void registerProductsAndCallbacks(EDFilterBase* module, ProductRegistry* reg) {
        registerProducts(module, reg, moduleDescription_);
      }
      std::string workerType() const {return "WorkerT<EDFilter>";}
      
      virtual bool filter(Event&, EventSetup const&) = 0;
      virtual void beginJob() {}
      virtual void endJob(){}

      virtual void doBeginRun_(Run const& rp, EventSetup const& c);
      virtual void doEndRun_(Run const& rp, EventSetup const& c);
      virtual void doBeginLuminosityBlock_(LuminosityBlock const& lbp, EventSetup const& c);
      virtual void doEndLuminosityBlock_(LuminosityBlock const& lbp, EventSetup const& c);

      virtual void doBeginRunProduce_(Run& rp, EventSetup const& c);
      virtual void doEndRunProduce_(Run& rp, EventSetup const& c);
      virtual void doBeginLuminosityBlockProduce_(LuminosityBlock& lbp, EventSetup const& c);
      virtual void doEndLuminosityBlockProduce_(LuminosityBlock& lbp, EventSetup const& c);

      
      void setModuleDescription(ModuleDescription const& md) {
        moduleDescription_ = md;
      }
      ModuleDescription moduleDescription_;
      CurrentProcessingContext const* current_context_;
      std::vector<BranchID> previousParentage_;
      ParentageID previousParentageId_;

    };
    
  }
}


#endif

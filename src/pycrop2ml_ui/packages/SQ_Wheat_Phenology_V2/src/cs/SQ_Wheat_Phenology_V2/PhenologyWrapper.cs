using System;
using System.Collections.Generic;
using System.Linq;
class PhenologyWrapper
{
    private PhenologyState s;
    private PhenologyRate r;
    private PhenologyAuxiliary a;
    private PhenologyExogenous ex;
    private PhenologyComponent phenologyComponent;

    public PhenologyWrapper()
    {
        s = new PhenologyState();
        r = new PhenologyRate();
        a = new PhenologyAuxiliary();
        ex = new PhenologyExogenous();
        phenologyComponent = new PhenologyComponent();
        loadParameters();
    }

        double aMXLFNO = 24.0d;
    double pNini = 4.0d;
    double sDsa_sh = 1.0d;
    double latitude = 0.0d;
    double kl = 0.45d;
    double lincr = 8.0d;
    double ldecr = 0.0d;
    double pincr = 1.5d;
    double pTQhf = 0.0d;
    double B = 20.0d;
    double areaSL = 0.0d;
    double areaSS = 0.0d;
    double lARmin = 0.0d;
    double sowingDensity = 0.0d;
    double lARmax = 0.0d;
    double lNeff = 0.0d;
    double rp = 0.0d;
    double p = 120.0d;
    double pdecr = 0.4d;
    double maxTvern = 23.0d;
    double tTWindowForPTQ = 70.0d;
    double vBEE = 0.01d;
    int isVernalizable = 1;
    double minTvern = 0.0d;
    double intTvern = 11.0d;
    double vAI = 0.015d;
    double maxDL = 15.0d;
    string choosePhyllUse = "Default";
    double minDL = 8.0d;
    double pFLLAnth = 2.22d;
    double dcd = 100.0d;
    double dgf = 450.0d;
    double degfm = 0.0d;
    bool ignoreGrainMaturation = false;
    double pHEADANTH = 1.0d;
    double sLDL = 0.85d;
    int sowingDay = 1;
    DateTime sowingDate =  new DateTime(2007, 3, 21);
    int sDws = 1;
    double sDsa_nh = 1.0d;
    double der = 300.0d;
    double targetFertileShoot = 600.0d;
    double dse = 105.0d;
    double slopeTSFLN = 0.9d;
    double intTSFLN = 0.9d;

    public double phyllochron{ get { return s.phyllochron;}} 
     
    public double minFinalNumber{ get { return s.minFinalNumber;}} 
     
    public List<DateTime> calendarDates{ get { return s.calendarDates;}} 
     
    public List<string> calendarMoments{ get { return s.calendarMoments;}} 
     
    public double ptq{ get { return s.ptq;}} 
     
    public double leafNumber{ get { return s.leafNumber;}} 
     
    public List<double> listPARTTWindowForPTQ{ get { return s.listPARTTWindowForPTQ;}} 
     
    public List<double> listTTShootWindowForPTQ{ get { return s.listTTShootWindowForPTQ;}} 
     
    public List<double> calendarCumuls{ get { return s.calendarCumuls;}} 
     
    public double vernaprog{ get { return s.vernaprog;}} 
     
    public int hasLastPrimordiumAppeared{ get { return s.hasLastPrimordiumAppeared;}} 
     
    public double phase{ get { return s.phase;}} 
     
    public double finalLeafNumber{ get { return s.finalLeafNumber;}} 
     
    public int hasZadokStageChanged{ get { return s.hasZadokStageChanged;}} 
     
    public string currentZadokStage{ get { return s.currentZadokStage;}} 
     
    public List<double> tilleringProfile{ get { return s.tilleringProfile;}} 
     
    public double canopyShootNumber{ get { return s.canopyShootNumber;}} 
     
    public int numberTillerCohort{ get { return s.numberTillerCohort;}} 
     
    public double averageShootNumberPerPlant{ get { return s.averageShootNumberPerPlant;}} 
     
    public int hasFlagLeafLiguleAppeared{ get { return s.hasFlagLeafLiguleAppeared;}} 
     

    public PhenologyWrapper(PhenologyWrapper toCopy, bool copyAll) : this()
    {
        s = (toCopy.s != null) ? new PhenologyState(toCopy.s, copyAll) : null;
        r = (toCopy.r != null) ? new PhenologyRate(toCopy.r, copyAll) : null;
        a = (toCopy.a != null) ? new PhenologyAuxiliary(toCopy.a, copyAll) : null;
        ex = (toCopy.ex != null) ? new PhenologyExogenous(toCopy.ex, copyAll) : null;
        if (copyAll)
        {
            phenologyComponent = (toCopy.phenologyComponent != null) ? new PhenologyComponent(toCopy.phenologyComponent) : null;
        }
    }

    public void Init(){
        phenologyComponent.Init(s, r, a);
        loadParameters();
    }

    private void loadParameters()
    {
        phenologyComponent.aMXLFNO = aMXLFNO;
        phenologyComponent.pNini = pNini;
        phenologyComponent.sDsa_sh = sDsa_sh;
        phenologyComponent.latitude = latitude;
        phenologyComponent.kl = kl;
        phenologyComponent.lincr = lincr;
        phenologyComponent.ldecr = ldecr;
        phenologyComponent.pincr = pincr;
        phenologyComponent.pTQhf = pTQhf;
        phenologyComponent.B = B;
        phenologyComponent.areaSL = areaSL;
        phenologyComponent.areaSS = areaSS;
        phenologyComponent.lARmin = lARmin;
        phenologyComponent.sowingDensity = sowingDensity;
        phenologyComponent.lARmax = lARmax;
        phenologyComponent.lNeff = lNeff;
        phenologyComponent.rp = rp;
        phenologyComponent.p = p;
        phenologyComponent.pdecr = pdecr;
        phenologyComponent.maxTvern = maxTvern;
        phenologyComponent.tTWindowForPTQ = tTWindowForPTQ;
        phenologyComponent.vBEE = vBEE;
        phenologyComponent.isVernalizable = isVernalizable;
        phenologyComponent.minTvern = minTvern;
        phenologyComponent.intTvern = intTvern;
        phenologyComponent.vAI = vAI;
        phenologyComponent.maxDL = maxDL;
        phenologyComponent.choosePhyllUse = choosePhyllUse;
        phenologyComponent.minDL = minDL;
        phenologyComponent.pFLLAnth = pFLLAnth;
        phenologyComponent.dcd = dcd;
        phenologyComponent.dgf = dgf;
        phenologyComponent.degfm = degfm;
        phenologyComponent.ignoreGrainMaturation = ignoreGrainMaturation;
        phenologyComponent.pHEADANTH = pHEADANTH;
        phenologyComponent.sLDL = sLDL;
        phenologyComponent.sowingDay = sowingDay;
        phenologyComponent.sowingDate = sowingDate;
        phenologyComponent.sDws = sDws;
        phenologyComponent.sDsa_nh = sDsa_nh;
        phenologyComponent.der = der;
        phenologyComponent.targetFertileShoot = targetFertileShoot;
        phenologyComponent.dse = dse;
        phenologyComponent.slopeTSFLN = slopeTSFLN;
        phenologyComponent.intTSFLN = intTSFLN;
    }

    public void EstimatePhenology(DateTime currentdate, double cumulTT, double dayLength, double deltaTT, double pAR, double grainCumulTT, double gAI)
    {
        a.currentdate = currentdate;
        a.cumulTT = cumulTT;
        a.dayLength = dayLength;
        a.deltaTT = deltaTT;
        a.pAR = pAR;
        a.grainCumulTT = grainCumulTT;
        a.gAI = gAI;
        phenologyComponent.CalculateModel(s,s1, r, a, ex);
    }

}
#ifndef _CANOPYTEMPERATURE_
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
#include <array>
#include <map>
#include <tuple>
#include "Canopytemperature.h"
using namespace std;

Canopytemperature::Canopytemperature() { }
double Canopytemperature::getlambdaV() {return this-> lambdaV; }
double Canopytemperature::getrhoDensityAir() {return this-> rhoDensityAir; }
double Canopytemperature::getspecificHeatCapacityAir() {return this-> specificHeatCapacityAir; }
void Canopytemperature::setlambdaV(double _lambdaV) { this->lambdaV = _lambdaV; }
void Canopytemperature::setrhoDensityAir(double _rhoDensityAir) { this->rhoDensityAir = _rhoDensityAir; }
void Canopytemperature::setspecificHeatCapacityAir(double _specificHeatCapacityAir) { this->specificHeatCapacityAir = _specificHeatCapacityAir; }
void Canopytemperature::Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a, EnergybalanceExogenous& ex)
{
    //- Name: CanopyTemperature -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: CanopyTemperature Model
    //            * Author: Pierre Martre
    //            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            * Institution: INRA/LEPSE Montpellier
    //            * Abstract: It is calculated from the crop heat flux and the boundary layer conductance 
    //- inputs:
    //            * name: minTair
    //                          ** description : minimum air temperature
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : auxiliary
    //                          ** min : -30
    //                          ** max : 45
    //                          ** default : 0.7
    //                          ** unit : degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: maxTair
    //                          ** description : maximum air Temperature
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : auxiliary
    //                          ** min : -30
    //                          ** max : 45
    //                          ** default : 7.2
    //                          ** unit : degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: cropHeatFlux
    //                          ** description : Crop heat flux
    //                          ** variablecategory : rate
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 447.912
    //                          ** unit : g/m**2/d
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: conductance
    //                          ** description : the boundary layer conductance
    //                          ** variablecategory : state
    //                          ** inputtype : variable
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** default : 598.685
    //                          ** unit : m/d
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: lambdaV
    //                          ** description : latent heat of vaporization of water
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 2.454
    //                          ** min : 0
    //                          ** max : 10
    //                          ** unit : MJ/kg
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: rhoDensityAir
    //                          ** description : Density of air
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 1.225
    //                          ** unit : kg/m**3
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //            * name: specificHeatCapacityAir
    //                          ** description : Specific heat capacity of dry air
    //                          ** parametercategory : constant
    //                          ** datatype : DOUBLE
    //                          ** default : 0.00101
    //                          ** unit : MJ/kg/degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //- outputs:
    //            * name: minCanopyTemperature
    //                          ** description : minimal Canopy Temperature  
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : state
    //                          ** min : -30
    //                          ** max : 45
    //                          ** unit : degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //            * name: maxCanopyTemperature
    //                          ** description : maximal Canopy Temperature 
    //                          ** datatype : DOUBLE
    //                          ** variablecategory : state
    //                          ** min : -30
    //                          ** max : 45
    //                          ** unit : degC
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    double minTair = a.getminTair();
    double maxTair = a.getmaxTair();
    double cropHeatFlux = r.getcropHeatFlux();
    double conductance = s.getconductance();
    double minCanopyTemperature;
    double maxCanopyTemperature;
    minCanopyTemperature = minTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0));
    maxCanopyTemperature = maxTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0));
    s.setminCanopyTemperature(minCanopyTemperature);
    s.setmaxCanopyTemperature(maxCanopyTemperature);
}
#endif
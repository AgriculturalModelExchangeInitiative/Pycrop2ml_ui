#ifndef _DIFFUSIONLIMITEDEVAPORATION_
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
#include "Diffusionlimitedevaporation.h"
using namespace std;

Diffusionlimitedevaporation::Diffusionlimitedevaporation() { }
double Diffusionlimitedevaporation::getsoilDiffusionConstant() {return this-> soilDiffusionConstant; }
void Diffusionlimitedevaporation::setsoilDiffusionConstant(double _soilDiffusionConstant) { this->soilDiffusionConstant = _soilDiffusionConstant; }
void Diffusionlimitedevaporation::Calculate_Model(EnergybalanceState& s, EnergybalanceState& s1, EnergybalanceRate& r, EnergybalanceAuxiliary& a, EnergybalanceExogenous& ex)
{
    //- Name: DiffusionLimitedEvaporation -Version: 1.0, -Time step: 1
    //- Description:
    //            * Title: DiffusionLimitedEvaporation Model
    //            * Author: Pierre Martre
    //            * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
    //            Evapotranspiration and canopy and soil temperature calculations
    //            * Institution: INRA Montpellier
    //            * Abstract: the evaporation from the diffusion limited soil 
    //- inputs:
    //            * name: deficitOnTopLayers
    //                          ** description : deficit On TopLayers
    //                          ** variablecategory : auxiliary
    //                          ** datatype : DOUBLE
    //                          ** default : 5341
    //                          ** min : 0
    //                          ** max : 10000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : variable
    //            * name: soilDiffusionConstant
    //                          ** description : soil Diffusion Constant
    //                          ** parametercategory : soil
    //                          ** datatype : DOUBLE
    //                          ** default : 4.2
    //                          ** min : 0
    //                          ** max : 10
    //                          ** unit : 
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    //                          ** inputtype : parameter
    //- outputs:
    //            * name: diffusionLimitedEvaporation
    //                          ** description : the evaporation from the diffusion limited soil 
    //                          ** variablecategory : state
    //                          ** datatype : DOUBLE
    //                          ** min : 0
    //                          ** max : 5000
    //                          ** unit : g m-2 d-1
    //                          ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    double deficitOnTopLayers = a.getdeficitOnTopLayers();
    double diffusionLimitedEvaporation;
    if (deficitOnTopLayers / 1000.0 <= 0.0)
    {
        diffusionLimitedEvaporation = 8.3 * 1000.0;
    }
    else
    {
        if (deficitOnTopLayers / 1000.0 < 25.0)
        {
            diffusionLimitedEvaporation = 2.0 * soilDiffusionConstant * soilDiffusionConstant / (deficitOnTopLayers / 1000.0) * 1000.0;
        }
        else
        {
            diffusionLimitedEvaporation = 0.0;
        }
    }
    s.setdiffusionLimitedEvaporation(diffusionLimitedEvaporation);
}
#endif
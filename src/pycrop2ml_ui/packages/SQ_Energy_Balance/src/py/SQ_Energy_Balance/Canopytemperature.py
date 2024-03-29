# coding: utf8
from copy import copy
from array import array
from math import *

import numpy
from math import *

def model_canopytemperature(minTair = 0.7,
         maxTair = 7.2,
         cropHeatFlux = 447.912,
         conductance = 598.685,
         lambdaV = 2.454,
         rhoDensityAir = 1.225,
         specificHeatCapacityAir = 0.00101):
    """
     - Name: CanopyTemperature -Version: 1.0, -Time step: 1
     - Description:
                 * Title: CanopyTemperature Model
                 * Author: Pierre Martre
                 * Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
                 Evapotranspiration and canopy and soil temperature calculations
                 * Institution: INRA/LEPSE Montpellier
                 * Abstract: It is calculated from the crop heat flux and the boundary layer conductance 
     - inputs:
                 * name: minTair
                               ** description : minimum air temperature
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** min : -30
                               ** max : 45
                               ** default : 0.7
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: maxTair
                               ** description : maximum air Temperature
                               ** datatype : DOUBLE
                               ** variablecategory : auxiliary
                               ** min : -30
                               ** max : 45
                               ** default : 7.2
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : variable
                 * name: cropHeatFlux
                               ** description : Crop heat flux
                               ** variablecategory : rate
                               ** inputtype : variable
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 447.912
                               ** unit : g/m**2/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: conductance
                               ** description : the boundary layer conductance
                               ** variablecategory : state
                               ** inputtype : variable
                               ** datatype : DOUBLE
                               ** min : 0
                               ** max : 10000
                               ** default : 598.685
                               ** unit : m/d
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: lambdaV
                               ** description : latent heat of vaporization of water
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 2.454
                               ** min : 0
                               ** max : 10
                               ** unit : MJ/kg
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: rhoDensityAir
                               ** description : Density of air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 1.225
                               ** unit : kg/m**3
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
                 * name: specificHeatCapacityAir
                               ** description : Specific heat capacity of dry air
                               ** parametercategory : constant
                               ** datatype : DOUBLE
                               ** default : 0.00101
                               ** unit : MJ/kg/degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                               ** inputtype : parameter
     - outputs:
                 * name: minCanopyTemperature
                               ** description : minimal Canopy Temperature  
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** min : -30
                               ** max : 45
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
                 * name: maxCanopyTemperature
                               ** description : maximal Canopy Temperature 
                               ** datatype : DOUBLE
                               ** variablecategory : state
                               ** min : -30
                               ** max : 45
                               ** unit : degC
                               ** uri : http://www1.clermont.inra.fr/siriusquality/?page_id=547
    """

    minCanopyTemperature = None
    maxCanopyTemperature = None
    minCanopyTemperature = minTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0))
    maxCanopyTemperature = maxTair + (cropHeatFlux / (rhoDensityAir * specificHeatCapacityAir * conductance / lambdaV * 1000.0))
    return (minCanopyTemperature, maxCanopyTemperature)
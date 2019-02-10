# MovingWindowDefinition
Verify a definition through time

## Goal
Using time series, require to verify definition through time, which have duty cycle, minimum length and max gap characteristics. This library allows from a time series of booleans to verify such a defintion.

## Dependencies
Executed with python2 and 3 with pandas 

## Project

### Analysis
Contains the code to compute the moving window. 
This code deals with boolean time series, first it reorder given the time column. It can deal with datapoints with unregular temporal differences. However it assumes that the label is constant between two datapoints. 

### Examples
A small example is used on a generated dataset: first we apply a simple verification on the features to obtain a boolean time series and then we apply the function `computeMovingWindow`.
"""
    Contains the function to verify the definition
"""
import numpy as np

def verifyDef(booleanTS, duty_cycle = 1, min_length = 0, max_gap = 0, only_first = False):
    """
        Computes the longest period of contiguous (repecting the different criteria)
        of True in the boolean TS

        Arguments:
            booleanTS {Time Series} -- Time Series of boolean (only one dimension)
                                       And time is index (datetimelike !)
        
        Keyword Arguments:
            duty_cycle {int} -- Minimum percentage of positive (default: {1} -- All have to be positive)
            min_length {int} -- Minimum length of event (default: {0} -- Even one datapoint is enough)
            max_gap {int} -- Maximum interruption (default: {0} -- Does not allow to have one missing point)
        
            NB: Max_gap and min_length are dependent on the unit of the data

            only_first {bool} -- Stop after the first event (default: {False})

        Returns:
            List of (begin_time, end_time, duty_cycle)
    """
    # Sort index
    booleanTS.sort_index()

    # Computation
    events = []
    ## Iterate over all the index
    ### Whenevrer gap is more than max gap stop the current event
    start, end, density = None, None, None
    i = 0
    while i < len(booleanTS):
        booltime = booleanTS.iloc[i]
        if start is not None:
            time_weight = booleanTS.iloc[start + 1:i + 1].index \
                        - booleanTS.iloc[start:i].index
            dens_time = np.average(booleanTS.iloc[start:i].values, weights = time_weight)
        if booltime:
            # Point is positive
            if start is None:
                # Possible start
                start = i
                end = i
                density = 1
            elif dens_time >= duty_cycle:
                # Possible end => check next points
                end = i
                density = dens_time
        else:
            # Point is negative
            if end is None:
                pass
            elif (booleanTS.index[i] - booleanTS.index[end]) >= max_gap:
                # Restart at the last end
                i = end

                if (booleanTS.index[end] - booleanTS.index[start]) >= min_length:
                    # Gap is more important than max gap => Save previous event
                    events.append({"begin": booleanTS.index[start], "end": booleanTS.index[end], "density": density})
                    if only_first:
                        end = None
                        break
                start, end, density = None, None, None
        i += 1

    # Save the last point
    if (end is not None) and ((booleanTS.index[end] - booleanTS.index[start]) >= min_length) :
        events.append({"begin": booleanTS.index[start], "end": booleanTS.index[end], "density": density})

    return events
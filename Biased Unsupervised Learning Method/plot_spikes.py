#!/usr/bin/python
import numpy

def plot_mean_spike(spikemonitor_obj, time_window, timeunit):
    """
    Generates two numpy arrays to be used in a plot function with the number of spikes according to the time window.

    spikemonitor_obj->Brian SpikeMonitor object
    timewindow->float (preferable...)
    timeunit->msecond object from Brian (just because I didn't want to import Brian units here...)
    Ex:
    x, y = plot_mean_spike(LSM,50,msecond); plot(x,y); show(block=False)
    """

    if spikemonitor_obj.nspikes==0:
        return [],[]

    spike_matrix = spikemonitor_obj.spikes # it is a list of tuples

    values = []
    times = []
    number_of_spikes = 0
    time = 0*timeunit
    finished_nicely = False

    for i in range(len(spike_matrix)):
        if spike_matrix[i][1]<=(time+time_window*timeunit):
            number_of_spikes+=1 # counts the spikes until inside the time window
            finished_nicely = False
        else:
            values.append(number_of_spikes)
            times.append(time*1000)
            time=spike_matrix[i][1] # update the current time
            number_of_spikes=1 # resets to 1 and not zero because every loop is a spike
            finished_nicely = True

    # updates the last values in case the time window didn't finished in last position
    if not finished_nicely:
        values.append(number_of_spikes)
        times.append(time*1000)            

    return numpy.array(times), numpy.array(values)

def plot_cumulative_spike(spikemonitor_obj):
    """
    Plot the total number of spikes cumulatively according to the time passed.
    spikemonitor_obj->Brian SpikeMonitor object
    timeunit->msecond object from Brian (just because I didn't want to import Brian here too...)    

    x, y = plot_cumulative_spike(LSM,msecond); plot(x,y); show(block=False)
    """

    if spikemonitor_obj.nspikes==0:
        return [],[]

    spike_matrix = spikemonitor_obj.spikes

    # biggest_time = spike_matrix[len(spike_matrix)-1][1]

    values = []
    times = []
    number_of_spikes = 0

    for i in range(len(spike_matrix)):
        number_of_spikes+=1
        values.append(number_of_spikes)
        times.append(spike_matrix[i][1])

    return numpy.array(times)*1000, numpy.array(values)

def plot_cumulative_norm_spike(spikemonitor_obj, number_of_neurons):
    """
    The same as the plot_cumulative_spike, but with the Y values normalized by the total number
    of neurons in the NeuronGroup and the time in milliseconds.

    number_of_neurons->total number of neurons in the NeuronGroup.

    Ex:
    x, y = plot_cumulative_norm_spike(LSM,Number_of_neurons_lsm,msecond); plot(x,y); raster_plot(LSM); show(block=False)
    """

    if spikemonitor_obj.nspikes==0:
        return [],[] # no spikes, no points to plot!

    spike_matrix = spikemonitor_obj.spikes

    # biggest_time = spike_matrix[len(spike_matrix)-1][1]

    values = []
    times = []
    number_of_spikes = 0

    for i in range(len(spike_matrix)):
        number_of_spikes+=1
        values.append(number_of_spikes)
        times.append(spike_matrix[i][1])

    return numpy.array(times)*1000, float(number_of_neurons)*numpy.array(values)/float(spikemonitor_obj.nspikes)


def plot_cumulative_norm_spike_individual(spikemonitor_obj, neuron_n, number_of_neurons):
    """
    The same as the plot_cumulative_norm_spike, but shows only the information about the neurons in the neuron_n list.

    neuron_n->list with the number of the neurons to be analised

    """

    if spikemonitor_obj.nspikes==0:
        return [],[] # no spikes, no points to plot!

    spike_matrix = spikemonitor_obj.spikes

    # biggest_time = spike_matrix[len(spike_matrix)-1][1]

    values = []
    times = []
    number_of_spikes = 0

    for i in range(len(spike_matrix)):
        if spike_matrix[i][0] in neuron_n:
            number_of_spikes+=1
            values.append(number_of_spikes)
            times.append(spike_matrix[i][1])

    return numpy.array(times)*1000, float(number_of_neurons)*numpy.array(values)/float(max(values))

def plot_cumulative_norm_spike_individual_rt(spikemonitor_obj, neuron_n, number_of_neurons, reset_time):
    """
    The same as the plot_cumulative_norm_spike_individual, but resets the number according to reset_time

    reset_time->delta t the sum should be reseted (in seconds!!!!)

    """

    if spikemonitor_obj.nspikes==0:
        return [],[] # no spikes, no points to plot!

    spike_matrix = spikemonitor_obj.spikes

    # biggest_time = spike_matrix[len(spike_matrix)-1][1]

    values = []
    times = []
    number_of_spikes = 0
    time_i = 1

    for i in range(len(spike_matrix)):
        if spike_matrix[i][0] in neuron_n:
            if (spike_matrix[i][1] > (reset_time*time_i)):
                time_i = numpy.floor(spike_matrix[i][1]/float(reset_time)) # adjust the time_i if more than one reset_time occurs at once!
                time_i += 1
                number_of_spikes = 0

            number_of_spikes+=1
            values.append(number_of_spikes)
            times.append(spike_matrix[i][1])
    
    if values==[]:
                return [],[] # no spikes, no points to plot!


    return numpy.array(times)*1000, float(number_of_neurons)*numpy.array(values)/float(max(values))

def plot_cumulative_spike_individual_rt(spikemonitor_obj, neuron_n, number_of_neurons, reset_time):
    """
    The same as the plot_cumulative_norm_spike_individual_rt, but with a non normalized output.

    """

    if spikemonitor_obj.nspikes==0:
        return [],[] # no spikes, no points to plot!

    spike_matrix = spikemonitor_obj.spikes

    # biggest_time = spike_matrix[len(spike_matrix)-1][1]

    values = []
    times = []
    number_of_spikes = 0
    time_i = 1

    for i in range(len(spike_matrix)):
        if spike_matrix[i][0] in neuron_n:
            if (spike_matrix[i][1] > (reset_time*time_i)):
                time_i = numpy.floor(spike_matrix[i][1]/float(reset_time)) # adjust the time_i if more than one reset_time occurs at once!
                time_i += 1
                number_of_spikes = 0

            number_of_spikes+=1
            values.append(number_of_spikes)
            times.append(spike_matrix[i][1])
    
    if values==[]:
                return [],[] # no spikes, no points to plot!


    return numpy.array(times)*1000, numpy.array(values)
#! /usr/bin/python

from mpi4py import MPI

comm = MPI.COMM_WORLD.Split(1)
#print(comm)

#import os
#os.environ['DELAY_PYNEST_INIT'] = "1"
import nest

nest.set_communicator(comm)

pg = nest.Create('poisson_generator', params={'rate': 10.0})
parrots = nest.Create('parrot_neuron', 100)
nest.Connect(pg, parrots)
sd = nest.Create('spike_detector',
                 params={"record_to": ["screen", "arbor"]})
nest.Connect(parrots, sd)

#print(nest.GetKernelStatus())
#nest.SetKernelStatus({'recording_backend': 'arbor'})
#nest.SetKernelStatus({'recording_backends': {'screen': {}}})
status = nest.GetKernelStatus()
print('min_delay: ', status['min_delay'], ", max_delay: ", status['max_delay'])
nest.SetKernelStatus({'min_delay': status['min_delay']/2,
                      'max_delay': status['max_delay']})
status = nest.GetKernelStatus()
print('min_delay: ', status['min_delay'], ", max_delay: ", status['max_delay'])
nest.Simulate(1000.0)

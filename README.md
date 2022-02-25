The tool implemented here is intended for use in the monitoring of currents in RPC chambers of the muon system of CERN's CMS experiment. 
It uses Machine Learning algorithms to model the behavior and time evolution of the currents as a function of LHC paramaters, working point
and environmental parameters. The data used for the training of the models, other relevant data as well as the output of the predictions performed 
by the models, are all stored in a database created for this purpose. This repository also contains the necessary tools for communication with the database.
The principle of work of the monitoring tool is as follows: the incoming data about the currents are compared with the values predicted by previously trained 
models, and if the differences exceed some predermined values, this is interpreted as an indication of chamber misbehavior.

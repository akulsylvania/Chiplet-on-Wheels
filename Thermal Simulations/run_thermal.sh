#!/bin/bash

#run simulated annealing floor planning
python3 sim_annealing.py -c configs/infotainment_unit.cfg -d ./Outputs &


pid=$!


echo "Please wait..."


output=$(wait $pid && echo "Command executed successfully!")


echo "$output"

# visualize the floor plan
python3 config.py -c configs/infotainment_unit.cfg -d ./Outputs

# completion message
echo "Simulation completed executed successfully."


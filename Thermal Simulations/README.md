README

1. Follow the procedure to install TAP-2.5D on your local system: https://github.com/bu-icsg/TAP-2.5D
2. Extract the 'run.sh' script inside the TAP-2.5D folder.
3. Extract the 'infotainment_unit.cfg' file to the TAP-2.5D/configs folder.
4. While inside the TAP-2.5D folder, provide execution privleges to the 'run.sh' script using: chmod u+x run.sh
5. Run the script using: sh run.sh


The script would run and perform floor plan optimizaion on the given infotainment unit config file and save results to a new folder inside the TAP-2.5D folder called 'Outputs'. The resulting output provides powertraces/floorplans/transient temperatures for every iteration of the algorithm as well as a graphic SVG image of the final floorplan.

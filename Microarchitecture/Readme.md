README

The complete docker snapshot containing the micro-architecture simulator framework gem5 integrated with garnet is provided with this README file.

1. Download the `Dockerfile.txt` and place it inside the $PWD directory with the name `Dockerfile`.
2. Run the command `cat gem5_dockerfile.tar | docker import - gem5`
3. Now inside the $PWD directory run the command `docker build -t gem5 .`
4. Next run the following commands to get a shell inside the docker container:
    ```
    docker run -v $PWD:/pwd -d --name gem5 -i gem5
    docker ps # to verify if the container is running
    docker exec -it gem5 /bin/bash
    ```
5. Git clone the repository `https://github.com/GT-CHIPS/gem5_chips.git` inside $PWD.
6. Download and place the jlr.sh inside the `$PWD/gem5_chips/my_scripts` directory.
7. Now inside the container, you can run the following commands to simulate a chiplet architecture of desired configuration.
    ```
    cd /pwd/gem5_chips
    scons build/RISCV_MESI_Two_Level/gem5.opt
    chmod +x ./my_scripts/jlr.sh
    ./my_scripts/jlr.sh
    ```

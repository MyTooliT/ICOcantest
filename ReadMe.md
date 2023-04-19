# ICOtronic CAN Test Container

## Description

Script and [`Dockerfile`](Dockerfile) to test basic CAN communication with the ICOtronic system.

## Docker

### Build

Please run the following command in the root of the repository:

```sh
docker build -t icocantester .
```

### Run

Below we will describe two different options to “connect” the CAN adapter to the running container:

1. Using [host networking](https://docs.docker.com/network/host/)
2. Using network namespaces

#### Host Networking

1. Run Docker container:

   ```sh
   docker run --network host -it --name icocantester icocantester
   ```

2. Run script inside Docker container:

   ```sh
   python cantest/test.py
   ```

### Network Namespaces

1. Run Docker container:

   ```sh
   docker run -itd --name icocantester icocantester
   ```

2. Map CAN adapter into Docker container

   ```sh
   export DOCKERPID="$(docker inspect -f '{{ .State.Pid }}' icocantester)"
   sudo ip link set can0 netns "$DOCKERPID"
   sudo nsenter -t "$DOCKERPID" -n ip link set can0 type can bitrate 1000000
   sudo nsenter -t "$DOCKERPID" -n ip link set can0 up
   ```

3. Execute script:

   ```
   docker exec icocantester python cantest/test.py
   ```

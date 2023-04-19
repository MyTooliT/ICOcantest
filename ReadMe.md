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

1. Run Docker container

   ```sh
   docker run -it icocantester
   ```

2. Run script inside Docker container

   ```sh
   python cantest/test.py
   ```

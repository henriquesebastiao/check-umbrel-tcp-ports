# CUTP - Check Umbrel TCP Ports

A simple CLI tool to check if the TCP port you want to use in your container does not conflict with the port used by any of your [Umbrel](https://github.com/getumbrel/umbrel) apps.

### Check the desired port

Let's assume you want to use port `1287`, then run:

```bash
cutp check 1287
# Port 1287 is free.
```

A sad case:

```bash
cutp check 1234
# Port 1234 is already used by an Umbrel application.
```

### Generating a random port

If you are lacking creativity today, cutp can suggest a port:

```bash
cutp gen
# 4120
```

## Installation

Since `cutp` is a Python CLI you can install it with any package manager, here we will use `pipx`:

```bash
pipx install cutp
```

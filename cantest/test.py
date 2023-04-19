"""Connect to and reset Sensory Tool Holder"""

# -- Imports ------------------------------------------------------------------

from asyncio import run
from sys import stderr

from mytoolit.can import Network, NetworkError

# -- Functions ----------------------------------------------------------------


async def test():
    print("Try to connect to CAN device")
    try:
        async with Network() as network:
            print("Connected to CAN bus")

            node = "STU 1"
            print(f"Reset “{node}”")
            await network.reset_node(node)
            print(f"Success 🥳")
    except NetworkError as error:
        print(f"\nCAN communication failed: {error}", file=stderr)


# -- Main ---------------------------------------------------------------------

if __name__ == "__main__":
    run(test())

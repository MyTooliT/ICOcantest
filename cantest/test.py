"""Connect to and reset Sensory Tool Holder"""

# -- Imports ------------------------------------------------------------------

from asyncio import run

from mytoolit.can import Network

# -- Functions ----------------------------------------------------------------


async def test():
    print("Try to connect to CAN device")
    async with Network() as network:
        print("Connected to CAN bus")

        node = "STU 1"
        print(f"Reset “{node}”")
        await network.reset_node(node)
        print(f"Success 🥳")


# -- Main ---------------------------------------------------------------------

if __name__ == "__main__":
    run(test())

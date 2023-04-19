"""Connect to and reset Sensory Tool Holder"""

# -- Imports ------------------------------------------------------------------

from asyncio import run
from logging import basicConfig, getLogger, INFO
from sys import stderr

from mytoolit.can import Network, NetworkError

# -- Functions ----------------------------------------------------------------


async def test() -> int:
    """Connect computer to STU

    Returns
    -------

    `0` if everything worked as expected, `1` otherwise

    """

    basicConfig(
        level=INFO, style="{", format="{asctime} {levelname:7} {message}"
    )

    logger = getLogger(__name__)

    logger.info("Try to connect to CAN device")
    try:
        async with Network() as network:
            logger.info("Connected to CAN bus")

            node = "STU 1"
            logger.info(f"Reset “{node}”")
            await network.reset_node(node)
            logger.info(f"Success 🥳")
    except NetworkError as error:
        print(f"\nCAN communication failed: {error}", file=stderr)
        return 1

    return 0


# -- Main ---------------------------------------------------------------------

if __name__ == "__main__":
    exit(run(test()))

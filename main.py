import asyncio
import logging
import os

from dotenv import load_dotenv
from telentfy import Notifier

# load variables from .env
load_dotenv()

# debug flag
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# setup logging
logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

# setup notifier
notifier = Notifier()


async def main() -> None:
    logger.info("executing")


if __name__ == "__main__":
    asyncio.run(main())

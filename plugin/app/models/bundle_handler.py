from abc import ABC, abstractmethod
from app.models import BundleCredentials
import logging

logger = logging.getLogger(__name__)


class BundleHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    async def verify(self, credentials: BundleCredentials):
        raise NotImplementedError

import datetime
from typing import List, Optional

from data.package import Package
from data.release import Release


def release_count() -> int:
    return 2_234_847


def package_count() -> int:
    return 274_000


def latest_releases(limit: int=5) -> List:
    return [
        {"id": "fastapi", "summary": "A great web framework"},
        {"id": "uvicorn", "summary": "Your favorite ASGI server"},
        {"id": "httpx", "summary": "Requests for an async world"},
    ][:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name,
        "A great web framework",
        "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.",
        "https://fastapi.tiangolo.com/",
        "MIT",
        "Sebastián Ramírez",
    )
    return package


def get_package_for_package(package_name: str) -> Optional[Package]:
    return Release("1.2.0", datetime.datetime.now())
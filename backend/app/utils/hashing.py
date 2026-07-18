"""Privacy-preserving identifiers for contextual grouping."""

import hashlib


def generate_route_hash(origin: str, destination: str) -> str:
    """Return a stable opaque identifier for an origin-destination pair."""
    route = f"{origin.strip().casefold()}:{destination.strip().casefold()}"
    return hashlib.sha256(route.encode("utf-8")).hexdigest()[:16]

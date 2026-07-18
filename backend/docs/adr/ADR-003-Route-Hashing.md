# ADR-003: Server-side Route Hashing

## Status

Accepted

## Context

Journey grouping requires users travelling along similar routes to be identified efficiently.

Clients should not understand internal routing logic.

## Decision

Clients provide:

- origin
- destination
- host application

JourneyService generates a deterministic route hash internally.

The generated hash is stored in the database and indexed for efficient matching.

## Consequences

- Cleaner SDK API.
- Internal implementation can evolve without affecting clients.
- Prevents exposing routing implementation.
- Enables future geospatial optimisation.
# ADR-002: Journey-Centric Domain

## Status

Accepted

## Context

ContextLink SDK enables contextual social interactions.

Instead of matching users globally, matching occurs within a shared context.

## Decision

The Journey is the core domain object.

Users join Journeys through JourneyParticipant records.

Matching, AI conversation generation, anonymous chat, and trust evaluation all operate within a Journey.

## Consequences

- Better scalability.
- Better privacy.
- Context-aware recommendations.
- Multiple contexts supported.

Examples include:

- Traffic
- Bus
- Airport
- Campus
- Conference
- Events
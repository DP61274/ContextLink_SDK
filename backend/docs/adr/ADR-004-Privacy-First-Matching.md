# ADR-004: Privacy-First Matching

## Status

Accepted

## Context

ContextLink SDK is designed around user trust and consent.

Users should never become match candidates automatically.

## Decision

Journey participants are excluded from matching unless they explicitly opt in.

Matching considers:

- Journey
- Visibility
- Consent
- Intent
- Trust score (future)
- AI compatibility score (future)

## Consequences

- Consent-first architecture.
- Easier compliance with privacy expectations.
- Better user trust.
- Safer matchmaking.
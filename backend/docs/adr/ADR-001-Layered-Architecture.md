# ADR-001: Layered Architecture

## Status

Accepted

## Context

ContextLink SDK is designed as a reusable backend SDK rather than a standalone application.

As the project grows to include journey management, AI matching, anonymous communication, trust scoring, and Africa's Talking integrations, business logic must remain maintainable and independent from API endpoints.

## Decision

The project follows a layered architecture:

Client

↓

API (FastAPI Routers)

↓

Services (Business Logic)

↓

Repositories (Database Access)

↓

Database (SQLModel)

## Consequences

- Business logic is reusable.
- Database implementation is isolated.
- APIs remain thin.
- Easier testing.
- Easier future migration to PostgreSQL or other databases.
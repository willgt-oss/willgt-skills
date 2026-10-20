# TRD — <capability>

Technical contract. implementer owns writes. This file owns interfaces, data, and failure behavior. It does not restate the PRD.

`TYPES.md` decides when a feature needs this file. A feature with no interface does not get one. Existing screens are not backfilled.

## Interfaces

<the calls this capability exposes, and what each accepts and returns>

## Data

<the records this capability stores or reads, and which fields are required>

## Failure

<what the caller observes when the interface cannot complete, and what is not written>

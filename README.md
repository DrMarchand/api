# Discord Status Adapter

> A small Discord guild-command adapter with an HTTP health endpoint.

`DrMarchand/api` is the repository identifier. The checked-in package identifies the service as `echo-discord-bot`; neither identifier is presented here as a cleared public brand.

## Quick start

```bash
npm ci
cp .env.example .env
npm start
```

`npm start` runs [`index.js`](index.js), as defined by [`package.json`](package.json). Keep the real Discord token in the local `.env`; [`.gitignore`](.gitignore) excludes that file.

If the required Discord variables are absent, the HTTP health server still starts and the Discord client does not log in.

## Library map

| File | Purpose |
|---|---|
| [`index.js`](index.js) | HTTP health route, Discord command registration, and status response |
| [`package.json`](package.json) | Package metadata, commands, and dependency declarations |
| [`.env.example`](.env.example) | Non-secret configuration names |

## API

| Surface | Current behavior | Source |
|---|---|---|
| `GET /health` | Returns health, service identifier, application identifier, mode, and current timestamp | [`index.js`](index.js) |
| `/nfe_status` | Returns a read-only status response in Discord | [`index.js`](index.js) |
| Discord registration | Registers the guild command when token, client ID, and guild ID are present | [`index.js`](index.js) |

`nfe_status` is a compatibility command identifier. It is not a public product or brand name, and changing it requires a separate compatibility review.

## Commands

| Command | Effect | Defined by |
|---|---|---|
| `npm ci` | Installs the locked dependency tree | [`package-lock.json`](package-lock.json) |
| `npm start` | Starts the health server and, when configured, the Discord client | [`package.json`](package.json) |
| `npm test` | Exits with “no test specified” | [`package.json`](package.json) |

## Configuration

| Variable | Required for | Boundary |
|---|---|---|
| `DISCORD_TOKEN` | Discord registration and login | Secret; never commit |
| `DISCORD_CLIENT_ID` | Guild command registration | Runtime configuration |
| `DISCORD_GUILD_ID` | Guild command registration | Runtime configuration |
| `DISCORD_ALERT_CHANNEL_ID` | Reserved in [`.env.example`](.env.example) | Not consumed by current `index.js` |
| `PORT` | HTTP health server | Defaults to `8787` |

## Architecture

The current code implements one status command and one health endpoint. It does not implement a general execution engine, identity system, append-only ledger, cryptographic vault, or authorization framework.

Discord is an external connection boundary. This adapter does not hold organizational authority and does not make a third-party platform part of a private execution system.

## Public naming boundary

Public mark claims are paused as of August 26, 2026. Display copy is functional and unmarked. Repository names, package names, command identifiers, routes, and environment variables remain exact machine identifiers.

## Validation

`npm test` currently exits with “no test specified.” No automated test suite is claimed.

Useful checks after checkout:

```bash
node --check index.js
npm start
curl http://localhost:8787/health
```

The health response proves only that the observed process answered that request. It does not prove Discord connectivity when the required credentials are absent.

## Authority and license

**Legal and operating company:** Design Orchard LLC

[`package.json`](package.json) declares `ISC`, while [`LICENSE`](LICENSE) contains different terms. License scope remains unresolved pending authorized owner or legal review; this README does not alter either artifact.

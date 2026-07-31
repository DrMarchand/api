# Echo — Discord Audit Bot

> A minimal Discord guild-command adapter with an HTTP health endpoint, implemented in `DrMarchand/api`.

`api` is the existing repository identifier. The checked-in package identifies the service as `echo-discord-bot`; this repository is not the full DrMarchand’s ⚙︎ Nɛuro-Forge Engine™ API described by the previous README.

## Quick start

```bash
npm ci
cp .env.example .env
npm start
```

`npm start` runs [`index.js`](index.js), as defined by [`package.json`](package.json). Keep the real Discord token in the local `.env`; [`.gitignore`](.gitignore) excludes that file.

If the required Discord variables are absent, the HTTP health server still starts and the Discord client does not log in.

## Commands

| Command | Effect | Defined by |
|---|---|---|
| `npm ci` | Installs the locked dependency tree | [`package-lock.json`](package-lock.json) |
| `npm start` | Starts the health server and, when configured, the Discord client | [`package.json`](package.json) |
| `npm test` | Exits with “no test specified” | [`package.json`](package.json) |

## Implemented surfaces

| Surface | Current behavior | Source |
|---|---|---|
| `GET /health` | Returns service name, application name, integration mode, and current timestamp | [`index.js`](index.js) |
| `/nfe_status` | Guild slash command returning Echo/Atlas integration status | [`index.js`](index.js) |
| Discord registration | Registers the guild command when token, client ID, and guild ID are present | [`index.js`](index.js) |

`nfe_status` is a compatibility command identifier. Published prose should introduce the full Engine identity as DrMarchand’s ⚙︎ Nɛuro-Forge Engine™.

## Configuration

| Variable | Required for | Boundary |
|---|---|---|
| `DISCORD_TOKEN` | Discord registration and login | Secret; never commit |
| `DISCORD_CLIENT_ID` | Guild command registration | Runtime configuration |
| `DISCORD_GUILD_ID` | Guild command registration | Runtime configuration |
| `DISCORD_ALERT_CHANNEL_ID` | Reserved in [`.env.example`](.env.example) | Not consumed by current `index.js` |
| `PORT` | HTTP health server | Defaults to `8787` |

## Runtime boundary

Echo is a communications and status adapter. It does not implement 🗺️ DrMarchand’s ⚛︎ Atlas, DrMarchand’s ⚙︎ Nɛuro-Forge Engine™, or organizational authority.

The current code implements one read-only status command and one health endpoint. The `audit-only` label describes the present mode; it is not proof of a generalized authorization or blocking framework.

External Discord communication is a Bridge boundary. It does not make Discord, Echo, or this repository an internal Engine component.

## Architecture

`Discord user → external Discord Bridge → Echo service → read-only status response`

The HTTP health route is a separate local service surface. The current code does not call the Engine or Atlas.

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

Legal authority: `Design Orchard LLC`  
Copyright attribution: `© Design Orchard LLC`

[`package.json`](package.json) declares `ISC`, while [`LICENSE`](LICENSE) contains different MMS-oriented terms. License scope remains unresolved pending authorized owner/legal review; this README does not alter either artifact.

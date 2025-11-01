
# ELK Stack on Docker

[![validate-stack.yml](https://github.com/kalvinparker/ELK-Stack/actions/workflows/validate-stack.yml/badge.svg?branch=main)](https://github.com/kalvinparker/ELK-Stack/actions/workflows/validate-stack.yml)

[![codecov](https://codecov.io/gh/kalvinparker/ELK-Stack/branch/main/graph/badge.svg)](https://codecov.io/gh/kalvinparker/ELK-Stack)
[![coverage](https://github.com/kalvinparker/ELK-Stack/actions/workflows/coverage.yml/badge.svg?branch=main)](https://github.com/kalvinparker/ELK-Stack/actions/workflows/coverage.yml)

## Security Assessment: CLOSED

The security assessment for this fork has been completed and formally closed. See the closure report for details and evidence:

[SECURITY_ASSESSMENT_CLOSURE.md](SECURITY_ASSESSMENT_CLOSURE.md)

This repository is a fork of the original "Getting started with the Elastic Stack and Docker Compose: Part 2" example. The upstream content (blog and demo) is maintained by Elastic and available at:

- Upstream blog: https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose-part-2
- Upstream repo: https://github.com/elkninja/elastic-stack-docker-part-two

This fork contains personal modifications and improvements to make the stack easier to run locally, improve reproducibility, and add basic CI validation for the compose stack. If you're interested in the original upstream project, please refer to the links above.

NOTE: This README documents both the original upstream guidance and the changes made in this fork. Use the Getting Started section below to run this repository locally.

---

## My work / Changelog (what I changed in this fork)

- Centralized image pins into environment variables in `.env` (ES_IMAGE, KIBANA_IMAGE, METRICBEAT_IMAGE, FILEBEAT_IMAGE, LOGSTASH_IMAGE, ELASTIC_AGENT_IMAGE). This makes rotating digests easier and limits changes to one file.
- Added `.env.example` with placeholder values for local development and to prevent accidental secrets being committed.
- Upgraded the `app` Dockerfile to Python 3.11 and fixed dependency resolution in `app/requirements.txt` (so the `webapp` builds reliably).
- Fixed YAML/formatting issues in `docker-compose.yml` and removed the deprecated top-level `version` key.
- Added a GitHub Actions workflow `.github/workflows/validate-stack.yml` that validates `docker-compose config` and builds the `webapp` as part of CI.
- Added a small README "Getting Started" section and documented recommended `.env` values for local dev.

If you'd like a full diff or a PR link for these changes, I can include that here (or link to the branch/PR I used).

Branch/PR used for these changes: [chore/move-digests-to-env](https://github.com/kalvinparker/ELK-Stack/compare/main...chore/move-digests-to-env) — create/view a PR: https://github.com/kalvinparker/ELK-Stack/pull/new/chore/move-digests-to-env

---

## SDLC / Development Process used for this fork

This fork follows a small, pragmatic SDLC suitable for demo or POC projects:

1. Work is done on feature branches (e.g. `chore/move-digests-to-env`).
2. Changes are validated locally (`docker-compose -f docker-compose.yml config` and `docker-compose build webapp`).
3. A branch is pushed and a pull request is opened for review.
4. CI runs (`validate-stack.yml`) which currently:
	- Validates `docker-compose config` to detect YAML/syntax errors.
	- Builds the `webapp` image to ensure Dockerfile and Python dependencies are valid.
	- Optionally runs a secrets scan to prevent accidental commits of sensitive values.
5. After CI passes and review, the branch is merged into `main` and the changes are deployed or tagged as needed.

Good practices applied here:
- Pin images by digest for reproducible runs.
- Keep secrets out of the repository (`.env` is in `.gitignore`; `.env.example` contains placeholders).
- Use short-lived, fine‑grained tokens for any automation that needs GitHub API access.

---


## Resources
### Fleet/Agent

Overview: https://www.elastic.co/guide/en/fleet/current/fleet-overview.html

Policy Creation, No UI: https://www.elastic.co/guide/en/fleet/current/create-a-policy-no-ui.html

Adding Fleet On-Prem: https://www.elastic.co/guide/en/fleet/current/add-fleet-server-on-prem.html

Agent in a Container: https://www.elastic.co/guide/en/fleet/current/elastic-agent-container.html

Air Gapped: https://www.elastic.co/guide/en/fleet/current/air-gapped.html

Secure Fleet: https://www.elastic.co/guide/en/fleet/current/secure-connections.html

### APM

APM: https://www.elastic.co/guide/en/apm/guide/current/upgrade-to-apm-integration.html

On Prem: https://www.elastic.co/guide/en/apm/guide/current/apm-integration-upgrade-steps.html

Fleet-Managed: https://www.elastic.co/guide/en/fleet/8.8/install-fleet-managed-elastic-agent.html

Queue Full Error: https://www.elastic.co/guide/en/apm/server/current/common-problems.html#queue-full

---

## How to run (local development)

1. Copy or review the existing `.env` at the repo root and update secrets/passwords before starting.

2. Build the local `webapp` service (validates Dockerfile and Python dependencies):

```powershell
docker-compose -f "docker-compose.yml" build webapp
```

3. Start the stack (this will pull images and start services):

```powershell
docker-compose -f "docker-compose.yml" up
```

4. Access Kibana at: https://localhost:5601 (adjust port if you changed `KIBANA_PORT` in `.env`).

5. To stop and remove containers (local dev):

```powershell
docker-compose -f "docker-compose.yml" down -v
```

## Recommended `.env` values (edit for your environment)

Below are the local/dev recommended values already present in `.env`. Change passwords and keys for any real usage.

```properties
# Project namespace
COMPOSE_PROJECT_NAME=es

# Passwords (change!)
ELASTIC_PASSWORD=changeme
KIBANA_PASSWORD=changeme

# Elastic Stack version (tag used only for Kibana; other images are pinned by digest in docker-compose.yml)
STACK_VERSION=8.10.0

# Cluster and service ports
ES_PORT=9200
KIBANA_PORT=5601
FLEET_PORT=8220
APMSERVER_PORT=8200

# Memory limits for local/dev
ES_MEM_LIMIT=1g
KB_MEM_LIMIT=512m
LS_MEM_LIMIT=512m

# APM Secret Token (change)
ELASTIC_APM_SECRET_TOKEN=changeme_apm_token

# Encryption key (POC only)
ENCRYPTION_KEY=changeme_encryption_key
```

If you'd like me to add a sample `.env.example` file to the repo, I can create it and reference it from this README.

## Getting Started

1.  **Clone the Repository:**
	```bash
	git clone https://github.com/kalvinparker/ELK-Stack.git
	cd ELK-Stack
	```

2.  **Create Your Environment File:**
	Copy the provided template. **This file uses Unix-style (LF) line endings. Ensure your editor preserves this format.**
	```bash
	cp .env.example .env
	```

3.  **Generate Secrets:**
	Open the `.env` file and replace all `CHANGEME_*` placeholder values.
    
	*   **CRITICAL:** The `ENCRYPTION_KEY` must be a cryptographically secure random string of **at least 32 characters**. To generate a secure 64-character key, run the following command and paste the output into your `.env` file:
		```bash
		openssl rand -hex 32
		```

4.  **Build and Run the Stack:**
	```bash
	# Build all services defined in the compose file
	docker-compose build

	# Start the stack in detached mode
	docker-compose up -d
	```

5.  **Access Kibana:**
	After a few minutes for services to initialize, you can access Kibana at `https://localhost:5601`. The default user is `elastic` and the password is the `ELASTIC_PASSWORD` you set in your `.env` file.

---

## Troubleshooting

Here are solutions to common issues encountered during setup.

#### **Problem: `FATAL Error ... encryptionKey ... must have a minimum length of [32]`**

-   **Symptom:** The `kibana` container is in a restart loop or is marked as "unhealthy".
-   **Cause:** The `ENCRYPTION_KEY` in your `.env` file is too short.
-   **Solution:** Follow **Step 3** of the "Getting Started" guide to generate a new, cryptographically strong key of at least 32 characters. Then, run `docker-compose down -v` and `docker-compose up -d` to restart the stack with the new secret.

#### **Problem: `The "\\r" variable is not set` Warning**

-   **Symptom:** You see this warning when running any `docker-compose` command. Services may fail to start correctly.
-   **Cause:** Your `.env` file has been saved with Windows-style line endings (`CRLF`) instead of Unix-style (`LF`). The `\\r` (carriage return) character is corrupting the variables.
-   **Solution:** Open your `.env` and `.env.example` files in a modern text editor like VS Code. In the bottom-right status bar, click on `CRLF` and change it to `LF`. Save the files and restart your stack.

#### **Problem: Service Fails with `ENOTFOUND` or "Connection Refused"**

-   **Symptom:** One service log (e.g., Kibana or the webapp) shows it cannot connect to another service (e.g., `fleet-server` or `es01`).
-   **Cause:** The stack is still starting up. Docker Compose starts services in parallel, but some services depend on others being fully ready.
-   **Solution:** Be patient. The `healthcheck` configurations in `docker-compose.yml` will eventually ensure services start in the correct order. It can take several minutes for the entire stack, especially Elasticsearch, to become fully healthy. You can monitor the status with `docker-compose ps`.

---

	Security Principle: Secure Knowledge Transfer. By documenting the specific errors we encountered and their solutions, we are hardening the human process around the system. This reduces future downtime and prevents other developers from making the same security-critical mistakes (like using a weak encryption key).

	GRC Principle: Continuous Improvement. This update formally incorporates the lessons learned from our incident response (CR-20251101-01 and -02) back into the primary asset documentation, closing the loop on the Plan-Do-Check-Act cycle.

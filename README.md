# Getting started with the Elastic Stack and Docker Compose: Part 2
## Elastic Agent, Fleet, and Elastic APM

This repo is in reference to the blog [Getting Started with the Elastic Stack and Docker Compose: Part 2](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose-part-2)

You can read the first blog: [Getting Started with the Elastic Stack and Docker Compose](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose) or visit it's [GitHub repo](https://github.com/elkninja/elastic-stack-docker-part-one)

Please feel free to ask any questions via issues [here](https://github.com/elkninja/elastic-stack-docker-part-two/issues), our [Community Slack](https://ela.st/slack), or over in our [Discuss Forums](https://discuss.elastic.co/).

Pull Requests welcome :)

 
# Getting started with the Elastic Stack and Docker Compose: Part 2
## Elastic Agent, Fleet, and Elastic APM

This repo is in reference to the blog [Getting Started with the Elastic Stack and Docker Compose: Part 2](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose-part-2)

You can read the first blog: [Getting Started with the Elastic Stack and Docker Compose](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose) or visit its [GitHub repo](https://github.com/elkninja/elastic-stack-docker-part-one)

Please feel free to ask any questions via issues [here](https://github.com/elkninja/elastic-stack-docker-part-two/issues), our [Community Slack](https://ela.st/slack), or over in our [Discuss Forums](https://discuss.elastic.co/).

Pull requests welcome :)


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

1. Copy the example environment file:

```powershell
cp .env.example .env
```

2. Edit the `.env` file and replace all `CHANGEME_*` values with your actual secrets and configuration.

3. Build the webapp image:

```powershell
docker-compose build webapp
```

4. Start the stack:

```powershell
docker-compose up -d
```

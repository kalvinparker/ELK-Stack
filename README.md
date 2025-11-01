
# ELK Stack on Docker

[![validate-stack.yml](https://github.com/kalvinparker/ELK-Stack/actions/workflows/validate-stack.yml/badge.svg?branch=main)](https://github.com/kalvinparker/ELK-Stack/actions/workflows/validate-stack.yml)

This repository provides a comprehensive, security-hardened configuration for running the Elastic Stack (Elasticsearch, Logstash, Kibana) along with Beats and a sample web application using Docker Compose.

The configuration has been modernized and secured to follow current best practices, including immutable image pinning, automated CI/CD validation, and robust secrets management.

---

## Security Features & Hardening

This isn't just a standard ELK setup; it has been explicitly hardened:

- ✅ **Immutable Infrastructure:** All Elastic Stack services are pinned to their specific `sha256` digests in the `.env` file. This prevents unexpected or malicious image updates and ensures reproducible builds.
- ✅ **Secure by Default:** Kibana is configured with a mandatory, cryptographically strong encryption key. The service will refuse to start with a weak key.
- ✅ **Automated Validation:** A GitHub Actions workflow (`validate-stack.yml`) automatically validates the Docker Compose configuration and a successful `webapp` build on every commit and pull request.
- ✅ **Secrets Management:** A `.env.example` template is provided, and the `.gitignore` file is configured to prevent accidental commitment of the production `.env` file containing real secrets.

---

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

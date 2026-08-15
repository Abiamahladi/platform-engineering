# Platform Engineering Roadmap

## Project Objective

Build a cloud-native platform progressively, starting from local development and containerization and evolving toward a production-oriented Kubernetes platform.

The project is intentionally developed in stages so that each stage introduces a new operational capability and builds on the previous one.

---

## Stage 1 — Development Foundation

- [x] Linux development environment
- [x] Git configuration
- [x] GitHub repository
- [x] Project repository structure

---

## Stage 2 — Containerization

- [x] Docker installation
- [x] Docker images
- [x] Containerized Employee API
- [x] PostgreSQL container
- [x] Docker networking

---

## Stage 3 — Docker Compose

Docker Compose was used to run the Employee API and PostgreSQL together as a local multi-container application stack.

- [x] Docker Compose configuration
- [x] API container
- [x] PostgreSQL container
- [x] Environment-based configuration
- [x] API-to-database communication
- [x] Local application testing

### Architectural Milestone

**Docker Compose → Kubernetes**

The project moved from local multi-container orchestration to Kubernetes when the focus expanded from simply running containers to managing workloads as a platform.

---

## Stage 4 — Kubernetes Foundation

- [x] Kubernetes cluster using kind
- [x] Kubernetes namespaces
- [x] Employee API Deployment
- [x] PostgreSQL workload
- [x] Persistent storage
- [x] Kubernetes Services
- [x] API replicas
- [x] Internal service discovery

---

## Stage 5 — Database Platform

- [x] PostgreSQL deployed in Kubernetes
- [x] PostgreSQL database initialization
- [x] PersistentVolumeClaim
- [x] Database Service
- [x] API-to-PostgreSQL connectivity
- [x] Database authentication verification

---

## Stage 6 — Secrets Management

- [x] HashiCorp Vault
- [x] Vault authentication
- [x] Vault Secrets Operator
- [x] Kubernetes Secret integration
- [x] API consumption of database credentials

---

## Stage 7 — Container Registry

- [x] GitHub Container Registry
- [x] Versioned Employee API image
- [x] employee-api:v2
- [x] Image push to GHCR
- [x] Kubernetes deployment using registry image

---

## Stage 8 — Kubernetes Networking

- [x] ClusterIP Service
- [x] Kubernetes DNS service discovery
- [x] Internal API testing
- [x] NodePort Service
- [x] External access through Kubernetes node
- [x] End-to-end API testing

### Current State

The Employee API is accessible through a Kubernetes NodePort and successfully communicates with PostgreSQL.

---

## Stage 9 — Ingress

- [ ] Ingress Controller
- [ ] HTTP routing
- [ ] Host-based routing
- [ ] Browser access without NodePort
- [ ] TLS/HTTPS

---

## Stage 10 — Observability

- [x] Kubernetes Metrics Server
- [x] Node resource metrics
- [x] Pod resource metrics
- [ ] Prometheus
- [ ] Grafana
- [ ] Loki
- [ ] Alertmanager
- [ ] Application metrics
- [ ] Infrastructure dashboards
- [ ] Alerting

### Current State

Kubernetes Metrics Server is deployed and healthy.

The platform can currently expose CPU and memory usage for nodes and Pods through:

```bash
kubectl top nodes
kubectl top pods -A
```
---

## Stage 11 — Infrastructure as Code

- [ ] Terraform modules
- [ ] Kubernetes infrastructure automation
- [ ] Reusable infrastructure
- [ ] Environment configuration

---

## Stage 12 — CI/CD

- [ ] GitHub Actions
- [ ] Automated image builds
- [ ] Image publishing
- [ ] Deployment automation
- [ ] Git-based deployment workflow

---

## Stage 13 — Production Engineering

- [ ] High availability
- [ ] Resource requests and limits
- [ ] Horizontal scaling
- [ ] Database backup and recovery
- [ ] Security hardening
- [ ] Disaster recovery
- [ ] Production deployment strategy

---

## Engineering Progression

```text
Local Development
       ↓
Docker
       ↓
Docker Compose
       ↓
Kubernetes
       ↓
Persistent Storage
       ↓
Secrets Management
       ↓
Container Registry
       ↓
Kubernetes Networking
       ↓
Ingress
       ↓
Observability
       ↓
Infrastructure as Code
       ↓
CI/CD
       ↓
Production Engineering

# Platform Architecture

## 1. Architecture Evolution

The platform is being built progressively rather than introduced as a complete system from the beginning.

The architecture has evolved through several stages:

```text
Local Development
       │
       ▼
     Docker
       │
       ▼
 Docker Compose
       │
       │  Architectural transition
       ▼
   Kubernetes
       │
       ├── Employee API
       ├── PostgreSQL
       ├── Persistent Storage
       ├── Kubernetes Services
       ├── Vault
       └── GHCR
       │
       ▼
    Ingress
       │
       ▼
 Observability
       │
       ▼
 CI/CD

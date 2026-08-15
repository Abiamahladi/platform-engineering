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
    Argo CD (GitOps)
       │
       ▼
    Ingress
       │
       ▼
 Observability
       │
       ├── Prometheus
       └── Grafana
       │
       ▼
     CI/CD
```

## 2. GitOps Reconciliation Loop

Since Stage 9, the cluster no longer relies solely on manual `kubectl apply`. Argo CD continuously reconciles cluster state against the `kubernetes/` path in this repository.

```text
Git Repository (source of truth)
       │
       ▼
   Argo CD
       │
       ├── Sync — applies Git state to cluster
       └── selfHeal — reverts manual cluster drift back to Git
```

## 3. Observability Data Flow

```text
Kubernetes Cluster
  (Nodes, Pods, Kubernetes components)
       │
       ▼
  Prometheus
  (scrape, store, query via PromQL)
       │
       ▼
   Grafana
  (dashboards)
```

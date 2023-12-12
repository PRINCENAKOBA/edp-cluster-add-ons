# EPAM Delivery Platform (EDP) Cluster Add-ons Repository

This repository contains a collection of pre-configured solutions (add-ons) for Kubernetes cluster. It follows the GitOps methodology and utilizes the ArgoCD App of Apps pattern for streamlined configuration and deployment.

The repository offers a variety of Kubernetes add-ons that can be easily integrated into Kubernetes cluster, whether running on Openshift or any other Managed Kubernetes distribution. These add-ons enhance cluster capabilities and provide additional functionalities for the EPAM Delivery Platform (EDP).

Using ArgoCD, one can leverage the repository to expedite the setup process of the EPAM Delivery Platform (EDP) and cluster components. The repository provides ready-to-use configurations for add-ons, simplifying deployment and reducing complexity.

Explore this repository to access a comprehensive collection of Kubernetes add-ons for your Kubernetes. Simplify deployment, enhance cluster capabilities, and stay up-to-date with the evolving landscape of Kubernetes.

## Repository structure

* `add-ons` - contains the source code of the Add Ons in the form of the Helm charts
* `chart` - contains the Helm chart that uses Apps of Apps pattern and contains ArgoCD Application CRs

```bash
.
├── add-ons
│   ├── argocd
│   ├── aws-efs-csi-driver
│   ├── cert-manager
...
│   ├── tekton
│   └── vault
└── chart
    ├── Chart.yaml
    ├── README.md
    ├── templates
    │   ├── argocd.yaml
    │   ├── aws-efs-csi-driver.yaml
    │   ├── cert-manager.yaml
...
    │   ├── tekton.yaml
    │   └── vault.yaml
    └── values.yaml
    └── values.yaml
```

## Available add-ons

Check out the list of available add-ons in the [chart](./chart/README.md) directory.

```bash
make update-readme
```

<!-- AUTOGENERATED CONTENT BELOW -->
| Component              | version   | appVersion   | createNamespace   | enable   |
|:-----------------------|:----------|:-------------|:------------------|:---------|
| argo-cd                | N/A       | N/A          | False             | False    |
| aws-efs-csi-driver     | 1.5.7     | 1.5.7        | N/A               | False    |
| capsule                | 0.5.3     | 0.4.2        | False             | False    |
| capsule-tenant         | N/A       | N/A          | N/A               | False    |
| certmanager            | N/A       | N/A          | False             | False    |
| defectdojo             | 1.6.96    | 2.28.2       | False             | False    |
| dependency-track       | 1.5.5     | v1.12.1      | False             | False    |
| edp                    | 3.6.0     | 3.6.0        | False             | False    |
| extensions-oidc        | 1.18.1    | 1.18.1       | False             | False    |
| external-secrets       | 0.9.9     | 1.0          | False             | False    |
| fluent-bit             | 0.1.0     | 2.1.4        | False             | False    |
| harbor                 | 0.1.0     | 1.12.2       | False             | False    |
| harbor-ha              | 1.13.0    | 2.9.0        | False             | False    |
| harbor-ha-okd          | 1.13.0    | 2.9.0        | False             | False    |
| ingress-nginx          | 4.7.3     | 1.8.4        | False             | False    |
| jaeger-operator        | 1.45.0    | 1.45.0       | False             | False    |
| keycloak               | 0.1.1     | 1.0          | False             | False    |
| keycloak-postgresql    | 0.1.1     | 1.0          | False             | False    |
| minio-operator         | 0.1.0     | 5.0.5        | False             | False    |
| nexus                  | 61.0.2    | 3.61.0       | False             | False    |
| nexus-operator         | 2.17.0    | 2.17.0       | False             | False    |
| opensearch             | 2.16.1    | 2.11.0       | False             | False    |
| opentelemetry-operator | 0.1.0     | 0.30.1       | False             | False    |
| postgres-operator      | 0.1.0     | 5.4.3        | False             | False    |
| prometheus-operator    | 0.1.0     | 46.4.1       | False             | False    |
| redis-operator         | 0.1.0     | 3.2.8        | False             | False    |
| sonar                  | 8.0.2     | 9.9.2        | False             | False    |
| sonar-operator         | 3.1.0     | 3.1.0        | False             | False    |
| storage-class          | N/A       | N/A          | N/A               | False    |
| tekton-cache           | 0.1.0     | 0.1.0        | True              | True     |
| tekton                 | N/A       | N/A          | False             | False    |
| vault                  | 0.24.1    | 1.13.1       | False             | False    |
| vault-kms              | 0.25.0    | 1.14.0       | False             | False    |
| vault-okd              | 0.25.0    | 1.14.0       | False             | False    |

# Automation

154 open-source tools that automate the software lifecycle. All on GitHub.

| Category | Tools |
|:--|--:|
| [Workflows](#workflows) | 13 |
| [CI/CD](#cicd) | 11 |
| [Releases](#releases) | 9 |
| [Infrastructure as code](#infrastructure-as-code) | 12 |
| [Cloud and policy](#cloud-and-policy) | 9 |
| [Kubernetes](#kubernetes) | 16 |
| [Data and ML](#data-and-ml) | 10 |
| [Task queues and runners](#task-queues-and-runners) | 14 |
| [Desktop and RPA](#desktop-and-rpa) | 7 |
| [Testing](#testing) | 18 |
| [Developer workflow](#developer-workflow) | 9 |
| [Security and networks](#security-and-networks) | 10 |
| [Alerting and ChatOps](#alerting-and-chatops) | 8 |
| [Backup, marketing, home](#backup-marketing-home) | 8 |

## Workflows

| Tool | What it does |
|:--|:--|
| [n8n](https://github.com/n8n-io/n8n) | Connect apps and automate tasks visually |
| [Node-RED](https://github.com/node-red/node-red) | Flow-based programming for event-driven apps and IoT |
| [Huginn](https://github.com/huginn/huginn) | Agents that watch the web and act for you |
| [Windmill](https://github.com/windmill-labs/windmill) | Workflows, scripts and integrations |
| [Temporal](https://github.com/temporalio/temporal) | Reliable microservice orchestration |
| [Apache Airflow](https://github.com/apache/airflow) | Author, schedule and monitor workflows in code |
| [Prefect](https://github.com/PrefectHQ/prefect) | Orchestrate data workflows |
| [Dagster](https://github.com/dagster-io/dagster) | Data orchestrator for ML, analytics, ETL |
| [Luigi](https://github.com/spotify/luigi) | Batch job pipelines in Python. Built at Spotify. |
| [Argo Workflows](https://github.com/argoproj/argo-workflows) | Parallel container jobs on Kubernetes |
| [Apache NiFi](https://github.com/apache/nifi) | Move data between systems |
| [Azkaban](https://github.com/azkaban/azkaban) | Batch job scheduler for Hadoop |
| [Apache Camel](https://github.com/apache/camel) | Enterprise integration patterns |

## CI/CD

| Tool | What it does |
|:--|:--|
| [Jenkins](https://github.com/jenkinsci/jenkins) | The classic automation server |
| [GitHub Actions Runner](https://github.com/actions/runner) | Self-hosted runner for GitHub Actions |
| [GitLab Runner](https://github.com/gitlab-org/gitlab-runner) | Runs GitLab CI/CD pipelines |
| [Tekton Pipelines](https://github.com/tektoncd/pipeline) | Kubernetes-native pipelines |
| [Drone](https://github.com/harness/drone) | Container-native CI/CD |
| [Woodpecker CI](https://github.com/woodpecker-ci/woodpecker) | Simple community fork of Drone |
| [Concourse](https://github.com/concourse/concourse) | Simple, scalable CI/CD |
| [GoCD](https://github.com/gocd/gocd) | Build and deployment pipelines |
| [Dagger](https://github.com/dagger/dagger) | CI/CD pipelines as code |
| [Jenkins X](https://github.com/jenkins-x/jx) | Kubernetes-native CI/CD |
| [Spinnaker](https://github.com/spinnaker/spinnaker) | Multi-cloud continuous delivery |

## Releases

Pair semantic-release with conventional commits for fully automatic releases.

| Tool | What it does |
|:--|:--|
| [semantic-release](https://github.com/semantic-release/semantic-release) | Versions and changelogs from commits |
| [release-please](https://github.com/googleapis/release-please) | Releases from conventional commits |
| [release-it](https://github.com/release-it/release-it) | Versioning and package publishing |
| [changesets](https://github.com/changesets/changesets) | Versions and changelogs for JS monorepos |
| [commitlint](https://github.com/conventional-changelog/commitlint) | Enforce conventional commit messages |
| [GoReleaser](https://github.com/goreleaser/goreleaser) | Ship Go binaries fast |
| [fastlane](https://github.com/fastlane/fastlane) | Build and release iOS and Android apps |
| [danger](https://github.com/danger/danger) | Automate code review chores |
| [Shopify Shipit](https://github.com/Shopify/shipit-engine) | Coordinate deployments |

## Infrastructure as code

| Tool | What it does |
|:--|:--|
| [Terraform](https://github.com/hashicorp/terraform) | Build and manage infrastructure in code |
| [OpenTofu](https://github.com/opentofu/opentofu) | Open-source fork of Terraform |
| [Terragrunt](https://github.com/gruntwork-io/terragrunt) | Keep Terraform configs DRY |
| [Atlantis](https://github.com/runatlantis/atlantis) | Terraform through pull requests |
| [Infracost](https://github.com/infracost/infracost) | Cloud cost estimates in pull requests |
| [Pulumi](https://github.com/pulumi/pulumi) | Infrastructure in real programming languages |
| [Ansible](https://github.com/ansible/ansible) | IT automation |
| [Salt](https://github.com/saltstack/salt) | Remote execution and configuration |
| [Chef Infra](https://github.com/chef/chef) | Infrastructure automation |
| [Puppet](https://github.com/puppetlabs/puppet) | Configuration management |
| [Packer](https://github.com/hashicorp/packer) | Build machine images |
| [Vagrant](https://github.com/hashicorp/vagrant) | Dev environments in VMs and containers |

## Cloud and policy

| Tool | What it does |
|:--|:--|
| [Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian) | Rules engine for cloud accounts |
| [CloudQuery](https://github.com/cloudquery/cloudquery) | Load cloud assets into databases |
| [AWS CDK](https://github.com/aws/aws-cdk) | Cloud infrastructure in familiar languages |
| [CDK for Terraform](https://github.com/hashicorp/terraform-cdk) | Terraform in TypeScript or Python |
| [Open Policy Agent](https://github.com/open-policy-agent/opa) | Enforce policies across the stack |
| [Conftest](https://github.com/open-policy-agent/conftest) | Test config files with OPA |
| [Checkov](https://github.com/bridgecrewio/checkov) | Security scans for infrastructure code |
| [tfsec](https://github.com/aquasecurity/tfsec) | Security scans for Terraform |
| [Terrascan](https://github.com/tenable/terrascan) | Compliance checks for infrastructure code |

## Kubernetes

| Tool | What it does |
|:--|:--|
| [Argo CD](https://github.com/argoproj/argo-cd) | GitOps continuous delivery |
| [Flux](https://github.com/fluxcd/flux2) | GitOps toolkit |
| [Argo Rollouts](https://github.com/argoproj/argo-rollouts) | Progressive delivery |
| [Argo Events](https://github.com/argoproj/argo-events) | Event-driven triggers |
| [Helm](https://github.com/helm/helm) | Package manager |
| [Kustomize](https://github.com/kubernetes-sigs/kustomize) | Patch and overlay manifests |
| [KEDA](https://github.com/kedacore/keda) | Event-driven autoscaling |
| [Keptn](https://github.com/keptn/keptn) | App lifecycle orchestration |
| [Crossplane](https://github.com/crossplane/crossplane) | Control plane for cloud infrastructure |
| [Kruise](https://github.com/openkruise/kruise) | Workload management |
| [Kured](https://github.com/kubereboot/kured) | Automatic node reboots |
| [Rancher Fleet](https://github.com/rancher/fleet) | Manage thousands of clusters |
| [kOps](https://github.com/kubernetes/kops) | Production-grade cluster installs |
| [Cluster API](https://github.com/kubernetes-sigs/cluster-api) | Declarative cluster management |
| [Operator SDK](https://github.com/operator-framework/operator-sdk) | Build operators |
| [Kubeflow Pipelines](https://github.com/kubeflow/pipelines) | ML workflows on Kubernetes |

## Data and ML

Use DVC for data versions and MLflow for experiment tracking.

| Tool | What it does |
|:--|:--|
| [Airbyte](https://github.com/airbytehq/airbyte) | ELT data integration |
| [Meltano](https://github.com/meltano/meltano) | Data integration and transformation |
| [Pachyderm](https://github.com/pachyderm/pachyderm) | Data versioning and reproducible pipelines |
| [DVC](https://github.com/iterative/dvc) | Version control for ML projects |
| [MLflow](https://github.com/mlflow/mlflow) | ML lifecycle: experiments to deployment |
| [Kedro](https://github.com/kedro-org/kedro) | Reproducible data science code |
| [Metaflow](https://github.com/Netflix/metaflow) | Data science workflows in Python. Built at Netflix. |
| [BentoML](https://github.com/bentoml/BentoML) | Serve and deploy ML models |
| [Ray](https://github.com/ray-project/ray) | Distributed applications |
| [Flyte](https://github.com/flyteorg/flyte) | Cloud-native ML and data workflows |

## Task queues and runners

| Tool | What it does |
|:--|:--|
| [Celery](https://github.com/celery/celery) | Distributed task queue for Python. Fast, medium learning curve. |
| [RQ](https://github.com/rq/rq) | Simple background jobs for Python. Easiest to learn. |
| [Dramatiq](https://github.com/Bogdanp/dramatiq) | Fast, reliable task processing for Python |
| [APScheduler](https://github.com/agronholm/apscheduler) | Job scheduling for Python |
| [BullMQ](https://github.com/taskforcesh/bullmq) | Fast job queue for Node.js |
| [Agenda](https://github.com/agenda/agenda) | Light job scheduling for Node.js |
| [Sidekiq](https://github.com/mperham/sidekiq) | Background jobs for Ruby |
| [Taskfile](https://github.com/go-task/task) | Task runner and build tool |
| [Just](https://github.com/casey/just) | Command runner like make |
| [Invoke](https://github.com/pyinvoke/invoke) | Python task execution |
| [Fabric](https://github.com/fabric/fabric) | Run shell commands remotely from Python |
| [Mage](https://github.com/magefile/mage) | Make-like build tool in Go |
| [doit](https://github.com/pydoit/doit) | Task automation |
| [tox](https://github.com/tox-dev/tox) | Test across Python environments |

## Desktop and RPA

Best for repetitive business tasks across many apps.

| Tool | What it does |
|:--|:--|
| [OpenRPA](https://github.com/open-rpa/openrpa) | Automate desktop and web tasks |
| [RPA Framework](https://github.com/robocorp/rpaframework) | Python RPA libraries from Robocorp |
| [TagUI](https://github.com/kelaberetiv/TagUI) | Automate web and desktop tasks |
| [AutoHotkey](https://github.com/AutoHotkey/AutoHotkey) | Windows desktop scripting |
| [SikuliX](https://github.com/RaiMan/SikuliX1) | Automate with image recognition |
| [robotgo](https://github.com/go-vgo/robotgo) | Desktop automation in Go |
| [PyAutoGUI](https://github.com/asweigart/pyautogui) | GUI automation in Python |

## Testing

| Tool | What it does |
|:--|:--|
| [Playwright](https://github.com/microsoft/playwright) | End-to-end tests across browsers |
| [Selenium](https://github.com/SeleniumHQ/selenium) | Browser automation for tests |
| [Cypress](https://github.com/cypress-io/cypress) | End-to-end testing in JavaScript |
| [Puppeteer](https://github.com/puppeteer/puppeteer) | Headless Chrome API for Node.js |
| [TestCafe](https://github.com/DevExpress/testcafe) | Web app testing |
| [Nightwatch](https://github.com/nightwatchjs/nightwatch) | End-to-end web testing |
| [Appium](https://github.com/appium/appium) | Mobile and desktop app automation |
| [Taiko](https://github.com/getgauge/taiko) | Reliable browser automation |
| [Robot Framework](https://github.com/robotframework/robotframework) | Generic test automation |
| [Karate](https://github.com/karatelabs/karate) | API test automation |
| [Gauge](https://github.com/getgauge/gauge) | Lightweight cross-platform testing |
| [Newman](https://github.com/postmanlabs/newman) | Run Postman collections from the command line |
| [k6](https://github.com/grafana/k6) | Load testing for developers |
| [Locust](https://github.com/locustio/locust) | Scalable load testing in Python |
| [JMeter](https://github.com/apache/jmeter) | Load and performance testing |
| [Vegeta](https://github.com/tsenart/vegeta) | HTTP load testing |
| [Artillery](https://github.com/artilleryio/artillery) | Performance testing |
| [Pact](https://github.com/pact-foundation/pact) | Contract tests for microservices and APIs |

## Developer workflow

Run Renovate and Dependabot together for full dependency coverage.

| Tool | What it does |
|:--|:--|
| [Renovate](https://github.com/renovatebot/renovate) | Automatic dependency updates |
| [Dependabot Core](https://github.com/dependabot/dependabot-core) | Dependency updates for GitHub |
| [pre-commit](https://github.com/pre-commit/pre-commit) | Multi-language pre-commit hooks |
| [Husky](https://github.com/typicode/husky) | Easy native Git hooks |
| [lint-staged](https://github.com/okonet/lint-staged) | Lint only staged files |
| [Commitizen](https://github.com/commitizen/cz-cli) | Write conventional commits |
| [auto](https://github.com/intuit/auto) | Releases from pull request labels |
| [Bashly](https://github.com/DannyBen/bashly) | Generate Bash CLIs from YAML |
| [Taskwarrior](https://github.com/GothenburgBitFactory/taskwarrior) | Command-line task manager |

## Security and networks

| Tool | What it does |
|:--|:--|
| [osquery](https://github.com/osquery/osquery) | Query your OS with SQL |
| [Wazuh](https://github.com/wazuh/wazuh) | Security monitoring, detection, response |
| [OWASP ZAP](https://github.com/zaproxy/zaproxy) | Web app security scanner |
| [StreamAlert](https://github.com/airbnb/streamalert) | Real-time security alerting. Built at Airbnb. |
| [TheHive](https://github.com/TheHive-Project/TheHive) | Incident response platform |
| [Cortex](https://github.com/TheHive-Project/Cortex) | Observable analysis and active response |
| [Nornir](https://github.com/nornir-automation/nornir) | Network automation framework |
| [Netmiko](https://github.com/ktbyers/netmiko) | Simple SSH to network devices |
| [NAPALM](https://github.com/napalm-automation/napalm) | Multi-vendor network automation |
| [Batfish](https://github.com/batfish/batfish) | Network configuration analysis |

## Alerting and ChatOps

| Tool | What it does |
|:--|:--|
| [Alertmanager](https://github.com/prometheus/alertmanager) | Route alerts from Prometheus |
| [Kapacitor](https://github.com/influxdata/kapacitor) | Process and alert on time series |
| [Alerta](https://github.com/alerta/alerta) | Alert management |
| [ElastAlert2](https://github.com/jertel/elastalert2) | Alerting for Elasticsearch |
| [Hubot](https://github.com/hubotio/hubot) | ChatOps for DevOps teams |
| [Errbot](https://github.com/errbotio/errbot) | Chatbot for ChatOps |
| [Lita](https://github.com/litaio/lita) | ChatOps framework |
| [Opsdroid](https://github.com/opsdroid/opsdroid) | Build chatbots |

## Backup, marketing, home

| Tool | What it does |
|:--|:--|
| [rclone](https://github.com/rclone/rclone) | Sync files with cloud storage |
| [restic](https://github.com/restic/restic) | Fast, secure backups |
| [Autorestic](https://github.com/cupcakearmy/autorestic) | Simpler restic configuration |
| [BorgBackup](https://github.com/borgbackup/borg) | Deduplicated, encrypted archives |
| [Syncthing](https://github.com/syncthing/syncthing) | Continuous file sync between devices |
| [Mautic](https://github.com/mautic/mautic) | Marketing automation |
| [Home Assistant](https://github.com/home-assistant/core) | Smart home automation |
| [openHAB](https://github.com/openhab/openhab-core) | Vendor-neutral home automation |

## Pick by need

| Need | Tools | Difficulty | Setup |
|:--|:--|:--|:--|
| Basic CI/CD | GitHub Actions and semantic-release | Easy | 30 min |
| Infrastructure | Terraform and Atlantis | Medium | 2 hours |
| Data pipelines | Airflow and DVC | Hard | 4 hours |
| Kubernetes | Argo CD and Helm | Expert | 1 day |
| ML workflows | MLflow and Kubeflow | Expert | 2 days |

- **Small teams:** GitHub Actions or Drone · Terraform or Pulumi · Prometheus and Grafana · Cypress and k6
- **Enterprise:** Airflow or Temporal · OWASP ZAP and Wazuh · Open Policy Agent · Kubernetes and Argo CD

**Stacks that work together**
- GitOps: Argo CD, Kustomize, Helm
- ML pipeline: DVC, MLflow, Kubeflow
- Security first: Open Policy Agent, Falco, OWASP ZAP
- Observability: Prometheus, Grafana, Alertmanager

**Worth watching:** Backstage · Kratix · Flagger · Linkerd

## Learn

- **Courses:** [Test Automation University](https://testautomationu.applitools.com/) · [DevOps roadmap](https://roadmap.sh/devops) · [Kubernetes training](https://kubernetes.io/training/) · [Terraform tutorials](https://learn.hashicorp.com/terraform)
- **Communities:** [DevOps.com](https://devops.com/community/) · [r/devops](https://reddit.com/r/devops) · [CNCF Slack](https://slack.cncf.io/) · [Kubernetes Slack](https://kubernetes.slack.com/)
- **YouTube:** [TechWorld with Nana](https://www.youtube.com/c/TechWorldwithNana) · [Docker](https://www.youtube.com/user/dockerrun) · [Kubernetes](https://www.youtube.com/c/KubernetesCommunity) · [HashiCorp](https://www.youtube.com/c/HashiCorp)

Updated September 2025.

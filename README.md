# NexusML

<!-- toc -->

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Multi-Tenancy and Subscriptions](#multi-tenancy-and-subscriptions)
- [Pending Refactor Note](#pending-refactor-note)
- [Additional Documentation](#additional-documentation)
- [Maintainers](#maintainers)
- [Acknowledgments](#acknowledgments)

## Introduction

NexusML is a multimodal AutoML platform for classification and regression tasks.

Please refer to [docs/what-is-nexusml.md](docs/what-is-nexusml.md) and [docs/concepts.md](docs/concepts.md) for an 
overview of NexusML and its key features.

## Requirements

- Python 3.10
- [Auth0](https://auth0.com/) configuration for user authentication
- [AWS S3](https://aws.amazon.com/s3/) configuration if you want to use S3 as the file storage backend

## Multi-Tenancy and Subscriptions

NexusML is designed with multi-tenancy in mind, enabling multiple organizations (tenants) to use the platform 
independently within isolated workspaces. Each tenant has its own environment, where organization members can 
collaborate on tasks, manage data, and deploy AI models without affecting other tenants.

> ℹ️ Multi-tenancy requires [Auth0](https://auth0.com/) for user authentication. Please refer to 
> [docs/auth0.md](docs/auth0.md) for instructions on setting up Auth0 for NexusML.

NexusML allows you to create and customize subscription plans, adjusting quota limits (such as storage and compute 
resources) to meet the specific needs of different organizations.

> ℹ️ Billing and payment processing are not implemented. To use NexusML in a production environment, you will need to 
> integrate a billing and payment system such as [Stripe](https://stripe.com/). To do this, you will need to override 
> the `nexusml.api.jobs.periodic_jobs.bill()` function.

## Pending Refactor Note

The engine was originally designed as a standalone RESTful API, operating on a separate infrastructure from the main 
API. As a result, interactions between the engine and the main API rely heavily on JSON objects (Python dictionaries).

We are planning a comprehensive refactor to allow the engine to interact directly with database models. This change 
will streamline and simplify the integration between the engine and the main API.

## Additional Documentation

The [docs](docs) directory contains additional documentation:

- [architecture.md](docs/architecture.md): Describes the architecture of NexusML.
- [auth0.md](docs/auth0.md): Describes the Auth0 configuration for NexusML.
- [concepts.md](docs/concepts.md): Describes the concepts used in NexusML.
- [quickstart.md](docs/quickstart.md): Provides a quick start guide for NexusML.
- [states-and-statuses.md](docs/states-and-statuses.md): Describes NexusML's states and statuses.
- [what-is-nexusml.md](docs/what-is-nexusml.md): Provides an overview of NexusML.

## Maintainers

NexusML is maintained by the following individuals (in alphabetical order):

- Mikel Elkano Ilintxeta ([@melkilin](https://github.com/melkilin))
- Mikel Uriz Martin ([@MikelUriz](https://github.com/MikelUriz))

## Acknowledgments

We would like to recognize the valuable contributions of the following individuals (in alphabetical order):

- Enrique Hernández Calabrés ([@ehcalabres](https://github.com/ehcalabres))
- Leyre Ayllón Lafuente ([@layllon](https://github.com/layllon))
- Marco D'Alessandro ([@IoSonoMarco](https://github.com/IoSonoMarco))
- Miguel Ángel Álvarez Fernández ([@MigangalWork](https://github.com/MigangalWork))
- Miguel Pérez Martínez ([@MiguelPerezMartinez](https://github.com/MiguelPerezMartinez))

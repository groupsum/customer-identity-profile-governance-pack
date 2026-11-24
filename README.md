# customer-identity-profile-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>customer-identity-profile-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for customer identity, profile claims, SCIM, OpenID Connect, verified credentials, and CDP profile concepts.</p>
<p align="center">
<a href="https://pypi.org/project/customer-identity-profile-governance-pack/"><img alt="pypi: customer-identity-profile-governance-pack" src="https://img.shields.io/pypi/v/customer-identity-profile-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.2.0.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.2.0.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/customer-identity-profile-governance-pack/"><img alt="Monthly PyPI downloads: customer-identity-profile-governance-pack" src="https://img.shields.io/pypi/dm/customer-identity-profile-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/README.md"><img alt="README hits: customer-identity-profile-governance-pack" src="https://hits.sh/github.com/groupsum/customer-identity-profile-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/customer-identity-profile-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for customer identity, profile claims, SCIM, OpenID Connect, verified credentials, and CDP profile concepts.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern customer identity and profile data, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Customer Identity And Profile Data.

### Features

**Included ADRs**

- [`adr:customer-profile-source-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1001-customer-profile-source-policy.yaml) — Customer Profile Source Policy
- [`adr:scim-provisioning-profile-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1002-scim-provisioning-profile-policy.yaml) — SCIM Provisioning Profile Policy
- [`adr:shared-identity-signal-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1006-shared-identity-signal-policy.yaml) — Shared Identity Signal Policy
- [`adr:cdp-profile-persistence-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1007-cdp-profile-persistence-policy.yaml) — CDP Profile Persistence Policy
- [`adr:schema-org-person-profile-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1008-schema-org-person-profile-policy.yaml) — Schema.org Person Profile Policy
- [`adr:profile-identifier-and-attribute-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1009-profile-identifier-and-attribute-policy.yaml) — Profile Identifier And Attribute Policy
- [`adr:verified-profile-evidence-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1010-verified-profile-evidence-policy.yaml) — Verified Profile Evidence Policy
- [`adr:customer-profiles-consume-external-identity-protocol-authorities`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1011-customer-profiles-consume-external-identity-protocol-authorities.yaml) — Customer Profiles Consume External Identity Protocol Authorities

**Included SPECs**

- [`spc:scim-core-user-schema-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2001-scim-core-user-schema-requirements.yaml) — SCIM Core User Schema Requirements
- [`spc:scim-group-schema-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2002-scim-group-schema-requirements.yaml) — SCIM Group Schema Requirements
- [`spc:scim-protocol-operation-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2003-scim-protocol-operation-requirements.yaml) — SCIM Protocol Operation Requirements
- [`spc:scim-schema-uri-registry-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2004-scim-schema-uri-registry-requirements.yaml) — SCIM Schema URI Registry Requirements
- [`spc:openid-shared-signals-subject-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2008-openid-shared-signals-subject-requirements.yaml) — OpenID Shared Signals Subject Requirements
- [`spc:openid-shared-signals-event-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2009-openid-shared-signals-event-requirements.yaml) — OpenID Shared Signals Event Requirements
- [`spc:cdp-persistent-profile-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2012-cdp-persistent-profile-requirements.yaml) — CDP Persistent Profile Requirements
- [`spc:cdp-profile-accessibility-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2013-cdp-profile-accessibility-requirements.yaml) — CDP Profile Accessibility Requirements
- [`spc:schema-org-person-profile-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2014-schema-org-person-profile-requirements.yaml) — Schema.org Person Profile Requirements
- [`spc:profile-attribute-classification-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2015-profile-attribute-classification-requirements.yaml) — Profile Attribute Classification Requirements
- [`spc:verified-profile-evidence-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2016-verified-profile-evidence-requirements.yaml) — Verified Profile Evidence Requirements
- [`spc:customer-profile-attribute-integration-contract`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2017-customer-profile-attribute-integration-contract.yaml) — Customer Profile Attribute Integration Contract

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

If the desired PyPI release is a prerelease, use its exact version in the installer command.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add customer-identity-profile-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install customer-identity-profile-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add customer-identity-profile-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_customer_identity_profile import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:customer-identity-profile"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:customer-identity-profile` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/examples/usage.py).

```python
"""Resolve and read a packaged specification without synchronizing it."""

from ssot_pack_customer_identity_profile import load_document_manifest, read_packaged_document_text

spec = next(row for row in load_document_manifest("spec") if row["id"] == "spc:scim-core-user-schema-requirements")
document = read_packaged_document_text("spec", spec["filename"])
assert spec["id"] in document
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `customer-identity-profile-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_customer_identity_profile
uv run ssot pack preflight . ssot_pack_customer_identity_profile --all
uv run ssot pack sync . ssot_pack_customer_identity_profile --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_customer_identity_profile` in SSOT Registry. Review reservation owner `extension-pack:customer-identity-profile-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

Removed duplicate OIDC, identity-assurance, and VC ownership; added a customer-profile integration boundary.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_customer_identity_profile` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/customer-identity-profile-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/customer-identity-profile-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/customer-identity-profile-governance-pack)
- [Issues](https://github.com/groupsum/customer-identity-profile-governance-pack/issues)
- [Repository](https://github.com/groupsum/customer-identity-profile-governance-pack)
- [pypi: customer-identity-profile-governance-pack](https://pypi.org/project/customer-identity-profile-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/customer-identity-profile-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:customer-identity-profile`. The pack's reservation owner is `extension-pack:customer-identity-profile-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [CDP Institute CDP definition](https://www.cdpinstitute.org/learning-center/what-is-a-cdp/)
- [SCIM Core Schema](https://www.rfc-editor.org/rfc/rfc7643.html) and [SCIM Protocol](https://www.rfc-editor.org/rfc/rfc7644.html)
- [IANA SCIM Schema URI Registry](https://www.iana.org/assignments/scim/scim.xhtml)
- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0-18.html)
- [OpenID Connect for Identity Assurance](https://openid.net/specs/openid-connect-4-identity-assurance-1_0.html)
- [OpenID Shared Signals Framework](https://openid.github.io/sharedsignals/openid-sharedsignals-framework-1_0.html)
- [W3C Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/)
- [Schema.org Person](https://schema.org/Person)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->

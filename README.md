# customer-identity-profile-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/customer-identity-profile-governance-pack.svg)](https://pypi.org/project/customer-identity-profile-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/customer-identity-profile-governance-pack.svg)](https://pypi.org/project/customer-identity-profile-governance-pack/)
[![License](https://img.shields.io/pypi/l/customer-identity-profile-governance-pack.svg)](https://pypi.org/project/customer-identity-profile-governance-pack/)
[![Publish](https://github.com/groupsum/customer-identity-profile-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/customer-identity-profile-governance-pack/actions/workflows/publish.yml)
[![GitHub package](https://img.shields.io/badge/GitHub-package-24292f)](https://github.com/groupsum/customer-identity-profile-governance-pack)

Installable SSOT governance pack for customer identity, profile claims, SCIM, OpenID Connect, verified credentials, and CDP profile concepts.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `customer-identity-profile-governance-pack` is an installable SSOT governance pack for Customer Identity And Profile Data. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern customer identity and profile data, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`customer-identity-profile-governance-pack`](https://pypi.org/project/customer-identity-profile-governance-pack/)
- GitHub package repository: [`groupsum/customer-identity-profile-governance-pack`](https://github.com/groupsum/customer-identity-profile-governance-pack)
- Import package: `ssot_pack_customer_identity_profile`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:customer-identity-profile`
- PyPI package: `customer-identity-profile-governance-pack`
- Import package: `ssot_pack_customer_identity_profile`
- GitHub repository: `groupsum/customer-identity-profile-governance-pack`
- Reservation owner: `extension-pack:customer-identity-profile-governance-pack`

## Domain Focus

Customer Identity And Profile Data

## Authority Sources

- [CDP Institute CDP definition](https://www.cdpinstitute.org/learning-center/what-is-a-cdp/)
- [SCIM Core Schema](https://www.rfc-editor.org/rfc/rfc7643.html) and [SCIM Protocol](https://www.rfc-editor.org/rfc/rfc7644.html)
- [IANA SCIM Schema URI Registry](https://www.iana.org/assignments/scim/scim.xhtml)
- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0-18.html)
- [OpenID Connect for Identity Assurance](https://openid.net/specs/openid-connect-4-identity-assurance-1_0.html)
- [OpenID Shared Signals Framework](https://openid.github.io/sharedsignals/openid-sharedsignals-framework-1_0.html)
- [W3C Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/)
- [Schema.org Person](https://schema.org/Person)

## Included ADRs

- [`adr:customer-profile-source-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1001-customer-profile-source-policy.yaml) - Customer Profile Source Policy
- [`adr:scim-provisioning-profile-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1002-scim-provisioning-profile-policy.yaml) - SCIM Provisioning Profile Policy
- [`adr:openid-connect-profile-claims-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1003-openid-connect-profile-claims-policy.yaml) - OpenID Connect Profile Claims Policy
- [`adr:openid-identity-assurance-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1004-openid-identity-assurance-policy.yaml) - OpenID Identity Assurance Policy
- [`adr:verifiable-credential-profile-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1005-verifiable-credential-profile-policy.yaml) - Verifiable Credential Profile Policy
- [`adr:shared-identity-signal-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1006-shared-identity-signal-policy.yaml) - Shared Identity Signal Policy
- [`adr:cdp-profile-persistence-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1007-cdp-profile-persistence-policy.yaml) - CDP Profile Persistence Policy
- [`adr:schema-org-person-profile-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1008-schema-org-person-profile-policy.yaml) - Schema.org Person Profile Policy
- [`adr:profile-identifier-and-attribute-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1009-profile-identifier-and-attribute-policy.yaml) - Profile Identifier And Attribute Policy
- [`adr:verified-profile-evidence-policy`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/adr/ADR-1010-verified-profile-evidence-policy.yaml) - Verified Profile Evidence Policy

## Included SPECs

- [`spc:scim-core-user-schema-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2001-scim-core-user-schema-requirements.yaml) - SCIM Core User Schema Requirements
- [`spc:scim-group-schema-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2002-scim-group-schema-requirements.yaml) - SCIM Group Schema Requirements
- [`spc:scim-protocol-operation-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2003-scim-protocol-operation-requirements.yaml) - SCIM Protocol Operation Requirements
- [`spc:scim-schema-uri-registry-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2004-scim-schema-uri-registry-requirements.yaml) - SCIM Schema URI Registry Requirements
- [`spc:openid-connect-standard-claims-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2005-openid-connect-standard-claims-requirements.yaml) - OpenID Connect Standard Claims Requirements
- [`spc:openid-connect-userinfo-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2006-openid-connect-userinfo-requirements.yaml) - OpenID Connect UserInfo Requirements
- [`spc:openid-identity-assurance-verified-claims-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2007-openid-identity-assurance-verified-claims-requirements.yaml) - OpenID Identity Assurance Verified Claims Requirements
- [`spc:openid-shared-signals-subject-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2008-openid-shared-signals-subject-requirements.yaml) - OpenID Shared Signals Subject Requirements
- [`spc:openid-shared-signals-event-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2009-openid-shared-signals-event-requirements.yaml) - OpenID Shared Signals Event Requirements
- [`spc:verifiable-credentials-core-profile-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2010-verifiable-credentials-core-profile-requirements.yaml) - Verifiable Credentials Core Profile Requirements
- [`spc:verifiable-credentials-status-schema-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2011-verifiable-credentials-status-schema-requirements.yaml) - Verifiable Credentials Status And Schema Requirements
- [`spc:cdp-persistent-profile-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2012-cdp-persistent-profile-requirements.yaml) - CDP Persistent Profile Requirements
- [`spc:cdp-profile-accessibility-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2013-cdp-profile-accessibility-requirements.yaml) - CDP Profile Accessibility Requirements
- [`spc:schema-org-person-profile-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2014-schema-org-person-profile-requirements.yaml) - Schema.org Person Profile Requirements
- [`spc:profile-attribute-classification-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2015-profile-attribute-classification-requirements.yaml) - Profile Attribute Classification Requirements
- [`spc:verified-profile-evidence-requirements`](https://github.com/groupsum/customer-identity-profile-governance-pack/blob/master/src/ssot_pack_customer_identity_profile/templates/specs/SPEC-2016-verified-profile-evidence-requirements.yaml) - Verified Profile Evidence Requirements

## Install With uv

```bash
uv add customer-identity-profile-governance-pack
uv add ssot-registry customer-identity-profile-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install customer-identity-profile-governance-pack
uvx --from ssot-registry ssot pack sync . customer-identity-profile-governance-pack
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_customer_identity_profile import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub package repository: [groupsum/customer-identity-profile-governance-pack](https://github.com/groupsum/customer-identity-profile-governance-pack)
- PyPI package: [customer-identity-profile-governance-pack](https://pypi.org/project/customer-identity-profile-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

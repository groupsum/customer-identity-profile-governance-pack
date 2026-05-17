# ssot-pack-customer-identity-profile

Installable SSOT governance pack for customer identity, profile claims, SCIM, OpenID Connect, verified credentials, and CDP profile concepts.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:customer-identity-profile`
- Priority: `P2.1`
- PyPI package: `ssot-pack-customer-identity-profile`
- Import package: `ssot_pack_customer_identity_profile`
- GitHub repository: `groupsum/customer-identity-profile-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-customer-identity-profile`

## Domain Focus

Customer Identity And Profile Data

## Authority Sources

- CDP Institute CDP definition
- SCIM Core Schema and Protocol
- IANA SCIM Schema URI Registry
- OpenID Connect Core
- OpenID Connect for Identity Assurance
- OpenID Shared Signals Framework
- W3C Verifiable Credentials Data Model
- Schema.org Person

## Included ADRs

- `adr:customer-profile-source-policy` - Customer Profile Source Policy
- `adr:scim-provisioning-profile-policy` - SCIM Provisioning Profile Policy
- `adr:openid-connect-profile-claims-policy` - OpenID Connect Profile Claims Policy
- `adr:openid-identity-assurance-policy` - OpenID Identity Assurance Policy
- `adr:verifiable-credential-profile-policy` - Verifiable Credential Profile Policy
- `adr:shared-identity-signal-policy` - Shared Identity Signal Policy
- `adr:cdp-profile-persistence-policy` - CDP Profile Persistence Policy
- `adr:schema-org-person-profile-policy` - Schema.org Person Profile Policy
- `adr:profile-identifier-and-attribute-policy` - Profile Identifier And Attribute Policy
- `adr:verified-profile-evidence-policy` - Verified Profile Evidence Policy

## Included SPECs

- `spc:scim-user-profile-contract` - SCIM User Profile Contract
- `spc:openid-connect-claims-contract` - OpenID Connect Claims Contract
- `spc:verifiable-credentials-profile-contract` - Verifiable Credentials Profile Contract
- `spc:cdp-profile-contract` - CDP Profile Contract

## Install With uv

```bash
uv add ssot-pack-customer-identity-profile
uv add ssot-registry ssot-pack-customer-identity-profile
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-customer-identity-profile
uvx --from ssot-registry ssot pack sync . ssot-pack-customer-identity-profile
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

- GitHub repository: https://github.com/groupsum/customer-identity-profile-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-customer-identity-profile/
- SSOT Registry: https://pypi.org/project/ssot-registry/

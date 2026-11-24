"""Inspect the installed pack identity."""

from ssot_pack_customer_identity_profile import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:customer-identity-profile"
print(metadata["origin"]["id"])

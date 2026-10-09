# API wiring

The gateway is an adapter boundary, not business authority.

Owns:
- GET /v1/gateway/capabilities
- POST /v1/gateway/commands

It normalizes supported MDM/OEM operations, dispatches only authorized commands, and reports provider/device readback to Control Server.
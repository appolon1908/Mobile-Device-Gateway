from fastapi import FastAPI,Header,HTTPException
from pydantic import BaseModel
from typing import Any
app=FastAPI(title="Codestra Mobile Device Gateway",version="0.1.0")
SUPPORTED={"apply_policy","install_managed_app","remove_managed_app","lock_device","sync_contacts","sync_media","collect_inventory"}
class Dispatch(BaseModel):
    command_id:str;device_id:str;type:str;payload:dict[str,Any]={}
@app.get("/v1/health")
def health():return {"status":"ok"}
@app.get("/v1/gateway/capabilities")
def capabilities():return {"platform":"android","commands":sorted(SUPPORTED),"mode":"authorized-mdm"}
@app.post("/v1/gateway/commands",status_code=202)
def dispatch(body:Dispatch,x_service_identity:str|None=Header(None)):
    if not x_service_identity:raise HTTPException(401,"service identity required")
    if body.type not in SUPPORTED:raise HTTPException(422,"unsupported command")
    return {"command_id":body.command_id,"device_id":body.device_id,"status":"acknowledged","provider":"android-enterprise-adapter"}
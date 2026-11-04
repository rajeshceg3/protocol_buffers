#!/usr/bin/env python3
from pathlib import Path
import json,tempfile,subprocess,sys,shutil,hashlib
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'artifacts/verification';OUT.mkdir(parents=True,exist_ok=True)
scratch=Path(tempfile.mkdtemp(prefix='verify-protobuf-'));proof={'scope':'Compile actual schemas and serialize/deserialize actual generated Python messages. Not wire compatibility with other languages or prior deployed schema versions.','passed':False}
try:
 files=['enum.proto','helloworld.proto','nested.proto'];proof['sourceSha256']={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in files}
 cmd=[sys.executable,'-m','grpc_tools.protoc','-I'+str(ROOT),'--python_out='+str(scratch)]+[str(ROOT/x) for x in files]
 p=subprocess.run(cmd,capture_output=True,text=True,timeout=30);proof['compile']={'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr};assert p.returncode==0,'protoc failed'
 sys.path.insert(0,str(scratch));import helloworld_pb2 as h;import nested_pb2 as n;import enum_pb2 as e
 a=h.SampleMessage(id=7,is_sample=True,name='sample',slist=[1,3,5]);b=h.SampleMessage.FromString(a.SerializeToString());assert a==b and b.id==7 and list(b.slist)==[1,3,5]
 empty=h.SampleMessage();assert h.SampleMessage.FromString(empty.SerializeToString())==empty and empty.id==0 and not empty.is_sample
 x=n.ComplexMessage(one_msg=n.SimpleMessage(id=4,name='single'),multiple_msg=[n.SimpleMessage(id=5,name='list')]);y=n.ComplexMessage.FromString(x.SerializeToString());assert x==y and y.one_msg.name=='single' and len(y.multiple_msg)==1
 v=e.EnumMessage(id=3,team=e.ARSENAL);w=e.EnumMessage.FromString(v.SerializeToString());assert v==w and w.team==2 and e.Teams.Name(w.team)=='ARSENAL'
 proof['contracts']=['scalar/repeated roundtrip','proto3defaults','nested/repeated message roundtrip','enum name/numeric roundtrip'];proof['passed']=True
except Exception as error:proof['failure']=str(error)
finally:
 (OUT/'protobuf.json').write_text(json.dumps(proof,indent=2)+'\n');shutil.rmtree(scratch);assert (OUT/'protobuf.json').exists();print(json.dumps(proof,indent=2))
if not proof['passed']:raise SystemExit(1)

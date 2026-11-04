"""Docs cases that need more than one `apply` call (an op cannot see what an earlier op of the same batch created).
Run in the work directory after setup (base.docx must exist). Each case prints the status of each stage, then a read-back check."""
import json, subprocess, shutil, os, zipfile
W = os.getcwd(); os.makedirs("out", exist_ok=True)
def run(name, *batches, check):
    out = f"{W}/out/{name}.docx"; shutil.copy(f"{W}/base.docx", out)
    for i, ops in enumerate(batches):
        p = f"{W}/out/{name}{i}.json"; json.dump(ops, open(p, "w"))
        r = subprocess.run(["genoffice", "docs", "apply", out, "--ops", p, "--json"], capture_output=True, text=True)
        d = json.loads(r.stdout)
        print(name, i, d["status"], str(d.get("summary") or d.get("message"))[:100])
    xml = zipfile.ZipFile(out).read("word/document.xml").decode()
    print(name, "check", "ok" if check(xml) else "FAILED")
run("tablestyle",
    [{"op": "define_style", "styleId": "Banded", "name": "Banded", "type": "table", "run": {"bold": True}}],
    [{"op": "setTableStyle", "target": {"blockIndexes": [6]}, "styleId": "Banded", "look": {"bandedRows": True}}],
    check=lambda x: '<w:tblStyle w:val="Banded"' in x)
run("wrap_unwrap",
    [{"op": "wrap_content_control", "startBlockIndex": 3, "tag": "sec"}],
    [{"op": "unwrap_content_control", "tag": "sec"}],
    check=lambda x: "<w:sdt>" not in x)

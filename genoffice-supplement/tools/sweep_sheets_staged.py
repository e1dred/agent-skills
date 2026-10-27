"""Sheets cases that need more than one `apply` call (an op cannot see what an earlier op of the same batch created).
Run in the work directory after setup (base.xlsx must exist). Each case prints the status of each stage."""
import json, subprocess, shutil, os
W = os.getcwd(); os.makedirs("out", exist_ok=True)
def run(name, *batches, base="base.xlsx"):
    out = f"{W}/out/{name}.xlsx"; shutil.copy(base, out)
    for i, ops in enumerate(batches):
        p = f"{W}/out/{name}{i}.json"; json.dump(ops, open(p, "w"))
        r = subprocess.run(["genoffice", "sheet", "apply", out, "--ops", p, "--json"], capture_output=True, text=True)
        d = json.loads(r.stdout)
        print(name, i, d["status"], str(d.get("summary"))[:100], str(d.get("detail", {}).get("failures") or d.get("detail", {}).get("warnings") or "")[:200])
run("ctv", [{"op": "set_formula", "address": "F2", "formula": "=C2*D2"}], [{"op": "convert_to_values", "range": "F2:F2"}])
run("filtcrit", [{"op": "set_filter", "range": "A1:E7"}], [{"op": "set_filter_criteria", "column": "A", "values": ["North"]}])
run("table", [{"op": "clear_filter"}], [{"op": "add_table", "range": "A1:E7", "name": "Sales", "style": "TableStyleMedium2", "bandedRows": True}])
run("pivot", [{"op": "add_sheet", "name": "Piv"}], [{"op": "add_pivot", "sheet": "base", "sourceRange": "A1:E7", "targetCell": "A1", "targetSheet": "Piv", "rowFields": "Region", "columnField": "Product", "values": [{"field": "Qty", "agg": "sum"}]}])
run("pivot2", [{"op": "add_pivot", "sourceRange": "A1:E7", "targetCell": "H1", "rowFields": ["Region"], "values": [{"field": "Qty", "agg": "sum", "showDataAs": "percentOfTotal", "name": "Share"}, {"field": "Price", "agg": "average"}], "filters": [{"kind": "label", "field": "Region", "op": "beginsWith", "value": "No"}]}])
run("pivot3", [{"op": "add_pivot", "sourceRange": "A1:E7", "targetCell": "H1", "rowFields": ["Date"], "values": [{"field": "Qty", "agg": "sum"}], "groupings": [{"kind": "date", "field": "Date", "dateUnit": "month"}]}])
run("dupmove", [{"op": "duplicate_sheet", "sheet": "base", "name": "Copy"}], [{"op": "move_sheet", "sheet": "Copy", "position": 1}])
run("editchart", [{"op": "add_chart", "chartType": "line", "dataRange": "B1:C7", "title": "T"}], [{"op": "edit_chart", "chartPath": "xl/charts/chart1.xml", "title": "New", "chartType": "column", "legend": "bottom", "dataLabels": "value", "grouping": "stacked", "axisTitles": {"category": "Item", "value": "Qty"}, "seriesColors": {"0": "#C00000"}}])
run("pivot_editor_only", [{"op": "refresh_pivot"}])
run("protect", [{"op": "protect_sheet", "protected": True, "password": "pw", "allow": {"sort": True, "autoFilter": True}}])   # check the XML: no password, no allow attributes

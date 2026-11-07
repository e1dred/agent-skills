# GridCraft command catalogue (0.17.0)

Built 2026-11-06 from the skill's own text (SKILL.md, reference/ and tools/); no command was run and nothing was re-tested. Ids come from `gridcraft-cli` 0.17.0 (385 ids); the skill's version label: last tested on gridcraft-cli 0.17.0; evidence sections cite 0.14-0.17.0.
Status: **V** verified - the hit is under a heading naming verification or records an observed result (arrow, before/after, read-back, checked file, confirmed); **d** documented - named with parameters or usage, no recorded evidence; **n** named only - a bare list or command index; **s** skipped on purpose - the skill says skipped/not run/not tested/not exercised; **x** known no-op, broken or refused - the line says so; **V+** verified, but another line records a limit (refused or skipped in some state or version); the note quotes both. When a command has verified evidence anywhere, it counts as verified: a refusal or skip recorded elsewhere usually names a precondition or an older round.
Counts: V 368, V+ 5, d 2, n 0, s 8, x 2.

## app (1)

| id | status | note |
|---|---|---|
| `app.commands` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …s base64), `app.commands {"search":"sparkli… |

## arrange (6)

| id | status | note |
|---|---|---|
| `arrange.align` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …returned): `arrange.align {"kind":"shape","… |
| `arrange.bringForward` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …BOX id), `arrange.bringForward\|sendBackwa… |
| `arrange.group` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …wrong id), `arrange.group`, `arrange.rotate… |
| `arrange.rotate` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …ge.group`, `arrange.rotate {"degrees"}`, `o… |
| `arrange.selectionPane` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …k":true}`, `arrange.selectionPane {}` → `[{… |
| `arrange.sendBackward` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …:"left"}`, `arrange.sendBackward {"kind","i… |

## automate (7)

| id | status | note |
|---|---|---|
| `automate.allScripts` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …rams"}]}`, `automate.allScripts` → `[{name,… |
| `automate.deleteScript` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …workbook is refused until trusted), `automa… |
| `automate.newScript` | V | reference/auditing-and-helpers.md#Formula auditing, select…: `automate.newScript {"name","commands":[{"c… |
| `automate.recordActions` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …scripts: `automate.recordActions {}` … do… |
| `automate.runScript` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …ed:true}`, `automate.runScript {"name"}` → … |
| `automate.stopAction` | V | reference/newer-commands.md#New in 0.12.x (verified headle…: `automate.stopAction {}` → `{stopped:false}… |
| `automate.trustScripts` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …rusted}]`, `automate.trustScripts {}` → `{t… |

## cell (3)

| id | status | note |
|---|---|---|
| `cell.get` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: … back with `cell.get`, `sheet.read`, `docum… |
| `cell.set` | V | SKILL.md#Command formats (verified): …one cell \| `cell.set {"cell":"A1","input":"=B2*C2"}` (input is a st… |
| `cell.toggleCheckbox` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …E5:E6"}` + `cell.toggleCheckbox {"cell"}` (… |

## chart (12)

| id | status | note |
|---|---|---|
| `chart.addElement` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …*Charts: `chart.addElement {"element":"tr… |
| `chart.changeColors` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: `chart.changeColors {"palette":"monochrome\|… |
| `chart.changeType` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …yout":3}`, `chart.changeType {"type":"line"… |
| `chart.delete` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …solute"}`, `chart.delete {"chart":id}`, `ch… |
| `chart.formatSelection` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …:[hex…]`), `chart.formatSelection {"series"… |
| `chart.move` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …ed 3 → 2), `chart.move {"sheet":"Dash","at"… |
| `chart.quickLayout` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …C00000"}`, `chart.quickLayout {"layout":3}`… |
| `chart.selectData` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: `chart.selectData {"range":"Sheet1!A1:C6","… |
| `chart.set` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …d":true}`, `chart.set {"legend":"bottom","x… |
| `chart.shapeFill` | s | reference/analysis-pivots-charts.md#Pivot tables and chart…: Not run … - Not run: pivot slicers/timelines, `pivot.… |
| `chart.shapeOutline` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …art":id}`, `chart.shapeOutline`. |
| `chart.switchRowColumn` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …arkers"}`, `chart.switchRowColumn`, |

## control (5)

| id | status | note |
|---|---|---|
| `control.assign` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: `control.assign {"id":1,"command":"range.se… |
| `control.format` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: `control.format {"id":1,"text":"Speed","min… |
| `control.list` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: …ommands: `control.list {}` → `[{id,kind,n… |
| `control.press` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: `control.press {"id":1,"approve":true}` ran… |
| `control.setValue` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: `control.setValue {"id":1,"value":55}` move… |

## data (41)

| id | status | note |
|---|---|---|
| `data.advancedFilter` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: … filter: `data.advancedFilter {"range":"A… |
| `data.analysisToolPak` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …ToolPak: `data.analysisToolPak {"tool":"d… |
| `data.circleInvalid` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: `data.circleInvalid {}` → `{invalid:["F2"]}… |
| `data.clearFilter` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …{sorted}`, `data.clearFilter`, `data.reappl… |
| `data.consolidate` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …y labels): `data.consolidate {"sources":["Q… |
| `data.dataTable` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …(what-if): `data.dataTable {"range":"G1:H6"… |
| `data.filter` | V | reference/recipes.md#More recipes (verified headless): …*Filter: `data.filter {"range"}` turns AutoFilt… |
| `data.filterBy` | V | reference/recipes.md#More recipes (verified headless): …r on, then `data.filterBy {"column":"A","values":… |
| `data.flashFill` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …lashFill`, `data.flashFill`) answered "didn… |
| `data.forecastSheet` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …t sheet: `data.forecastSheet {"timeline":… |
| `data.fromTableRange` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …Table1"}`, `data.fromTableRange {}` → copie… |
| `data.fromTextCsv` | V | reference/recipes.md#More recipes (verified headless): ….xlsx` and `data.fromTextCsv` both turn `007` int… |
| `data.getData` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: … import: `data.getData {"text":"[{\"id\":… |
| `data.goalSeek` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …al seek: `data.goalSeek {"set":"D5","to":… |
| `data.group` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: `data.group {"rows":"2:5"}`/`ungroup`, `dat… |
| `data.hideDetail` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …":"2:4"}`, `data.hideDetail\|showDetail {"ro… |
| `data.outlineSettings` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …`ungroup`, `data.outlineSettings {"summaryB… |
| `data.queriesConnections` | s | reference/formatting-and-sheets.md#Cell styles, table desi…: Not run … - Not run: `.xls/.xlsb/.ods` import (no sam… |
| `data.reapply` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …arFilter`, `data.reapply` |
| `data.refreshAll` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …],range}`, `data.refreshAll` → `{refreshed:… |
| `data.removeDuplicates` | V | reference/formatting-and-sheets.md#Everyday formatting and…: … / split \| `data.removeDuplicates {"range",… |
| `data.scenarioAdd` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …enarios: `data.scenarioAdd {"name":"Boom"… |
| `data.scenarioDelete` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …a. (2): `data.scenarioDelete` `{"name": … |
| `data.scenarioManager` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …e values), `data.scenarioManager {}`, `data… |
| `data.scenarioShow` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …,80,50]}`, `data.scenarioShow {"name"}` (wr… |
| `data.scenarioSummary` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …nager {}`, `data.scenarioSummary {}` (adds … |
| `data.showDetail` | V | reference/command-sweep.md#Verified in detail, GridCraft s…: …a. (1): `data.showDetail` headless: rows… |
| `data.showLevels` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: `data.showLevels {"rows":1}` collapses to t… |
| `data.solver` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …*Solver: `data.solver {"objective":"E1","… |
| `data.solverLoadModel` | V | reference/newer-commands.md#0.16 changes (verified headles…: `data.solverLoadModel {"from":"J1:J6"}` gav… |
| `data.solverReport` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: `data.solverReport` makes the report sheets… |
| `data.solverReset` | V | reference/newer-commands.md#0.16 changes (verified headles…: `data.solverReset {}` → `{removed:25,masked… |
| `data.solverSaveModel` | V | reference/newer-commands.md#0.16 changes (verified headles…: `data.solverSaveModel {"to":"J1"}` wrote J1… |
| `data.sort` | V | SKILL.md#Command formats (verified): \| sort \| `data.sort {"range","header":true,"keys":[{"column":"B","o… |
| `data.sortAscending` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …filters: `data.sortAscending\|sortDescendi… |
| `data.sortDescending` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `data.sortDescending` `{"range": "A80:B83",… |
| `data.subtotal` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …outline: `data.subtotal {"range":"A1:C5",… |
| `data.textToColumns` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …r":true}`, `data.textToColumns {"range","de… |
| `data.ungroup` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …"level"}`, `data.ungroup {"rows"}`. |
| `data.validate` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: … window: `data.validate {"cell":"F2","inp… |
| `data.validation` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: …idation: `data.validation {"range","type"… |

## document (1)

| id | status | note |
|---|---|---|
| `document.inspect` | V | SKILL.md#Surfaces: ….inspect`, `document.inspect`, |

## draw (5)

| id | status | note |
|---|---|---|
| `draw.eraser` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …"color"}`, `draw.eraser {"on":true}`, `draw… |
| `draw.inkToShape` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …shape:1}`, `draw.inkToShape {}` → `{kind:"L… |
| `draw.lasso` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …n":true}`, `draw.lasso`. |
| `draw.pen` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …e a line), `draw.pen {"on":true,"color"}`, … |
| `draw.stroke` | V | reference/auditing-and-helpers.md#Formula auditing, select…: - Ink: `draw.stroke {"points":[[10,10],… |

## edit (26)

| id | status | note |
|---|---|---|
| `edit.autoFill` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …s text), `edit.autoFill {"range","target"… |
| `edit.beginEdit` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …t. (6): `edit.beginEdit` (live) before: … |
| `edit.clearAll` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …` pastes), `edit.clearAll\|clearContents\|cle… |
| `edit.clearClipboard` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `edit.clearClipboard` (live) before: copy A… |
| `edit.clearComments` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `edit.clearComments` `{"range": "A6"}` (liv… |
| `edit.clearContents` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `edit.clearContents` `{"range": "A50"}` (li… |
| `edit.clearFormats` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: Editing: `edit.clearFormats\|clearContents\|c… |
| `edit.clearHyperlinks` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `edit.clearHyperlinks` `{"range": "A52"}` (… |
| `edit.copy` | V | reference/formatting-and-sheets.md#Everyday formatting and…: … / paste \| `edit.copy {"range"}`, `edit.pas… |
| `edit.cut` | V | reference/auditing-and-helpers.md#Formula auditing, select…: `edit.cut {"range"}` → `{range,text}`, `edi… |
| `edit.fillDown` | V | reference/recipes.md#More recipes (verified headless): …set`, then `edit.fillDown {"range":"E2:E7"}`. |
| `edit.fillLeft` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `edit.fillLeft` `{"range": "A54:B55"}` (liv… |
| `edit.fillRight` | V | reference/formatting-and-sheets.md#Everyday formatting and…: `edit.fillRight {"range"}` \| |
| `edit.fillSeries` | V | reference/formatting-and-sheets.md#Everyday formatting and…: \| series \| `edit.fillSeries {"range","type"… |
| `edit.fillUp` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …"range"}`, `edit.fillUp\|fillLeft {"range"}`… |
| `edit.find` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …`target`), `edit.find {"what"}` (error "We … |
| `edit.flashFill` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …sh Fill (`edit.flashFill`, `data.flashFil… |
| `edit.formatPainter` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …dit.redo`, `edit.formatPainter` (first call… |
| `edit.goTo` | V | reference/auditing-and-helpers.md#Formula auditing, select…: … `A1:D6`), `edit.goTo {"reference":"C3"\|"Sh… |
| `edit.goToSpecial` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …n absent), `edit.goToSpecial {"what":"formu… |
| `edit.paste` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …"range"}`, `edit.paste {"at":"C3"}`, `edit.… |
| `edit.pasteSpecial` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …t":"C3"}`, `edit.pasteSpecial {"what":"valu… |
| `edit.redo` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …you made), `edit.redo`, `edit.formatPainter… |
| `edit.replace` | V | reference/formatting-and-sheets.md#Everyday formatting and…: … replace \| `edit.replace {"what":"Jan","wit… |
| `edit.selectAll` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …d from A), `edit.selectAll` (current region… |
| `edit.undo` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …ge,text}`, `edit.undo {"steps":2}` → `{undo… |

## equation (1)

| id | status | note |
|---|---|---|
| `equation.edit` | V | reference/newer-commands.md#0.16 changes (verified headles…: `equation.edit {"id":1,"latex":"a^2+b^2=c^2… |

## file (13)

| id | status | note |
|---|---|---|
| `file.close` | d | SKILL.md#Limits to remember: …pp.quit` / `file.close {force:true}` discard unsaved work. |
| `file.exportCsv` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …{"path"}`, `file.exportCsv {"path"}` wrote … |
| `file.exportHtml` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …ll block), `file.exportHtml {"path"}`, `fil… |
| `file.exportPdf` | V | SKILL.md#Command formats (verified): \| PDF \| `file.exportPdf {"path":…,"sheets":"active\|all","range"?,"f… |
| `file.new` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …e. (2): `file.new` (live) before: ui.ins… |
| `file.open` | V | reference/recipes.md#More recipes (verified headless): `file.open {"path":"in.csv","csvAsText":true}` (v… |
| `file.options` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `file.options` (live) returned the active w… |
| `file.print` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …es,name}`, `file.printPreview {"page":1}` →… |
| `file.printPreview` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …es,name}`, `file.printPreview {"page":1}` →… |
| `file.properties` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: Files: `file.properties {"title","author"}`… |
| `file.save` | d | SKILL.md#Traps: …file.open`/`file.save` without `path` fail ("never opens dialogs"). |
| `file.saveAs` | V | SKILL.md#Command formats (verified): \| save \| `file.saveAs {"path":…}` (.xlsx default; `.csv .tsv .json … |
| `file.saveBytes` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …*Output: `file.saveBytes {"format":"csv\|x… |

## formulas (32)

| id | status | note |
|---|---|---|
| `formulas.autoSum` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: `formulas.autoSum {"range"}`, `formulas.tra… |
| `formulas.calculateNow` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …rations}`, `formulas.calculateNow` → `{cell… |
| `formulas.calculateSheet` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …,value}]`, `formulas.calculateSheet` → `{ce… |
| `formulas.calculationOptions` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …s {"on"}`, `formulas.calculationOptions {"m… |
| `formulas.convertToNumber` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …}` → `[]`, `formulas.convertToNumber`, `for… |
| `formulas.createFromSelection` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …`{cells}`, `formulas.createFromSelection {"… |
| `formulas.dateTime` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …s. (6): `formulas.dateTime` (live) retur… |
| `formulas.defineName` | V | reference/recipes.md#More recipes (verified headless): …lls down), `formulas.defineName {"name":"TaxRate"… |
| `formulas.deleteName` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …n the UI), `formulas.deleteName {"name"}`, … |
| `formulas.errorChecking` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …`{cells}`, `formulas.errorChecking` (earlie… |
| `formulas.evaluate` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …helpers: `formulas.evaluate {"formula":"=… |
| `formulas.evaluateFormula` | V | reference/auditing-and-helpers.md#Formula auditing, select…: `formulas.evaluateFormula {"cell":"D2"}` → … |
| `formulas.financial` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …ive cell), `formulas.financial\|logical\|text… |
| `formulas.functions` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …ToNumber`, `formulas.functions {}` (the who… |
| `formulas.insertFunction` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …tegory}]`, `formulas.insertFunction {"name"… |
| `formulas.logical` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `formulas.logical` (live) returned the Logi… |
| `formulas.lookupReference` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `formulas.lookupReference` (live) returned … |
| `formulas.mathTrig` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `formulas.mathTrig` (live) returned the Mat… |
| `formulas.moreFunctions` | V | reference/auditing-and-helpers.md#Formula auditing, select…: `formulas.moreFunctions {"category":"Statis… |
| `formulas.nameManager` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …eader row; `formulas.nameManager` lists the… |
| `formulas.pasteName` | V | reference/newer-commands.md#New in 0.12.x (verified headle…: - `formulas.pasteName {"list":true,"at":"J1… |
| `formulas.recentlyUsed` | V | reference/auditing-and-helpers.md#Formula auditing, select…: … section), `formulas.recentlyUsed` → `[]` i… |
| `formulas.removeArrows` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …pendents`, `formulas.removeArrows`, |
| `formulas.selectDependents` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `formulas.selectDependents` works only on t… |
| `formulas.selectPrecedents` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …l:"D2"}]`, `formulas.selectPrecedents {"cel… |
| `formulas.showFormulas` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …rors:[]}`, `formulas.showFormulas {"on"}`, … |
| `formulas.text` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `formulas.text` (live) returned the Text fu… |
| `formulas.traceDependents` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …,sheet}]`, `formulas.traceDependents {"cell… |
| `formulas.traceError` | V | reference/newer-commands.md#0.16 changes (verified headles…: - `formulas.traceError {"cell"}` → `{er… |
| `formulas.tracePrecedents` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …uditing: `formulas.tracePrecedents {"cell… |
| `formulas.useInFormula` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …{"name"}`, `formulas.useInFormula {"name"}`… |
| `formulas.watchWindow` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …la steps), `formulas.watchWindow {"add":"Sh… |

## history (1)

| id | status | note |
|---|---|---|
| `history.list` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: … Sheet1`), `history.list {"limit"}` → `{und… |

## home (64)

| id | status | note |
|---|---|---|
| `home.accounting` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: `home.accounting`/`percent`/`comma`/`increa… |
| `home.addIns` | V | reference/command-sweep.md#Verified in detail, GridCraft s…: …e. (1): `home.addIns` informational only… |
| `home.alignBottom` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …. (14): `home.alignBottom` (live) before… |
| `home.alignCenter` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …e","on"}`, `home.alignCenter\|alignRight\|jus… |
| `home.alignLeft` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …`{size}`), `home.alignLeft\|alignCenter\|alig… |
| `home.alignMiddle` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.alignMiddle` (live) before: cell.get … |
| `home.alignRight` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.alignRight` (live) before: cell.get A… |
| `home.alignTop` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.alignTop` (live) before: cell.get A70… |
| `home.autofitColumnWidth` | V | SKILL.md#Command formats (verified): …ol width \| `home.autofitColumnWidth {"cols":"A:D"}`, `home.columnWi… |
| `home.autofitRowHeight` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …ght":30}`, `home.autofitRowHeight`, `home.h… |
| `home.bold` | V | SKILL.md#Command formats (verified): \| bold \| `home.bold {"range":"A1:D1","on":true}` — a toggle if `o… |
| `home.borders` | V | reference/formatting-and-sheets.md#Everyday formatting and…: … borders \| `home.borders {"range":"A1:D5","… |
| `home.cellStyle` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: … checked): `home.cellStyle {"range","name":… |
| `home.clearRules` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …an index), `home.clearRules {"range"\|"sheet… |
| `home.columnWidth` | V | SKILL.md#Command formats (verified): …":"A:D"}`, `home.columnWidth {"cols":"B:D","width":64}` \| |
| `home.comma` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …seIndent`, `home.comma`, `home.increaseDeci… |
| `home.conditionalFormat` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: …formats (`home.conditionalFormat {"range"… |
| `home.decreaseDecimal` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.decreaseDecimal` (live) before: cell.… |
| `home.decreaseFontSize` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.decreaseFontSize` (live) before: cell… |
| `home.decreaseIndent` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …gnBottom`, `home.decreaseIndent`, `home.com… |
| `home.defaultWidth` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …"color"}`, `home.defaultWidth {"width":80}`… |
| `home.deleteCells` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …dth":80}`, `home.deleteCells {"range","shif… |
| `home.deleteColumns` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …column"}`, `home.deleteColumns {"cols"}`, `… |
| `home.deleteRows` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …":"3:5"}`, `home.deleteRows {"rows":"3:5"}`… |
| `home.deleteSheet` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …previous`, `home.deleteSheet` |
| `home.doubleUnderline` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.doubleUnderline` (live) before: cell.… |
| `home.drawBorder` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …eDecimal`, `home.drawBorder {"range","edge"… |
| `home.fillColor` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …t colour \| `home.fillColor {"range","color"… |
| `home.fontColor` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …DDEBF7"}`, `home.fontColor {"range","color"… |
| `home.fontName` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …e","on"}`, `home.fontName {"range","name":"… |
| `home.fontSize` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …n":true}`, `home.fontSize {"range","size":1… |
| `home.formatAsTable` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …t":true}`, `home.formatAsTable {"range","st… |
| `home.formatCells` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: …re, unlike `home.formatCells`). |
| `home.hideColumns` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …{"rows"}`, `home.hideColumns\|unhideColumns … |
| `home.hideRows` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …owHeight`, `home.hideRows\|unhideRows {"rows… |
| `home.increaseDecimal` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …me.comma`, `home.increaseDecimal\|decreaseDe… |
| `home.increaseFontSize` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …eorgia"}`, `home.increaseFontSize\|decreaseF… |
| `home.increaseIndent` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …gle":45}`, `home.increaseIndent`, |
| `home.insertCells` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …{"cols"}`, `home.insertCells {"range","shif… |
| `home.insertColumns` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …e","on"}`, `home.insertColumns/deleteColumn… |
| `home.insertCopiedCells` | V+ | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.insertCopiedCells` `{"at": "A45", "sh… · limit: command-sweep.md: …"}` before `home.insertCopiedCells {"at":"J3","shift":"down"… |
| `home.insertRows` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …ars":14}`, `home.insertRows {"rows":"3:5"}`… |
| `home.insertSheet` | V | reference/recipes.md#More recipes (verified headless): `home.insertSheet {"name":"Notes"}` |
| `home.italic` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …= toggle): `home.italic\|underline\|doubleUnd… |
| `home.justify` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.justify` (live) before: cell.get A70 … |
| `home.lockCell` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …{"cols"}`, `home.lockCell {"range","on"}`, … |
| `home.manageRules` | V | reference/auditing-and-helpers.md#Formula auditing, select…: … tables: `home.manageRules {}` → `{rules:… |
| `home.mergeAcross` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …"A7:D7"}` (`home.mergeAcross`) |
| `home.mergeCells` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …ltiplies), `home.mergeCells/unmergeCells`, … |
| `home.mergeCenter` | V | reference/formatting-and-sheets.md#Everyday formatting and…: \| merge \| `home.mergeCenter {"range":"A7:D7… |
| `home.newCellStyle` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …d orange), `home.newCellStyle {"name":"MySt… |
| `home.numberFormat` | V | SKILL.md#Command formats (verified): …r format \| `home.numberFormat {"range":"C2:D5","format":"Currency"}… |
| `home.orientation` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …gnBottom`, `home.orientation {"range","angl… |
| `home.percent` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …of 5 under `home.percent` showed 500%: the … |
| `home.rowHeight` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …rgeCells`, `home.rowHeight {"rows":"1:1","h… |
| `home.shrinkToFit` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.shrinkToFit` `{"on": true}` (live) be… |
| `home.strikethrough` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.strikethrough` `{"on": true}` (live) … |
| `home.subscript` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.subscript` `{"on": true}` (live) befo… |
| `home.superscript` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …double"}`, `home.superscript\|subscript\|stri… |
| `home.underline` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …helpers: `home.underline {"range","style"… |
| `home.unhideColumns` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.unhideColumns` `{"cols": "B:C"}` (hea… |
| `home.unhideRows` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …s:"C:C"}`, `home.unhideRows\|unhideColumns`. |
| `home.unmergeCells` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `home.unmergeCells` `{"range": "A72:B72"}` … |
| `home.wrapText` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …ize":12}`, `home.wrapText {"range","on":tru… |

## insert (20)

| id | status | note |
|---|---|---|
| `insert.button` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: …ew ids): `insert.button {"at":"E4","text"… |
| `insert.chart` | V | SKILL.md#Command formats (verified): \| chart \| `insert.chart {"range":"A1:A5,D1:D5","type":"column","tit… |
| `insert.chartRecommendations` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: `insert.chartRecommendations {"range"}` → r… |
| `insert.checkbox` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: `insert.checkbox {"range":"E5:E6"}` + `cell… |
| `insert.equation` | V | reference/newer-commands.md#0.16 changes (verified headles…: …uations: `insert.equation {"latex":"x^2+y… |
| `insert.icons` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …image:1}`, `insert.icons {}` → `{shape}` |
| `insert.link` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …yperlink \| `insert.link {"cell":"A9","targe… |
| `insert.picture` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …hape:id}`, `insert.picture {"path","at","wi… |
| `insert.pivotChart` | x | reference/analysis-pivots-charts.md#Pivot tables and chart…: … cell, but `insert.pivotChart {"pivot":"P1"… |
| `insert.pivotTable` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …t build: `insert.pivotTable {"source":"Sa… |
| `insert.recommendedCharts` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …t. (1): `insert.recommendedCharts` `{"ra… |
| `insert.recommendedPivotTables` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …ords:24}`, `insert.recommendedPivotTables {… |
| `insert.shape` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …Objects: `insert.shape {"kind":"roundedRe… |
| `insert.slicer` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …Slicers: `insert.slicer {"table"\|"pivot",… |
| `insert.slider` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: …",20]]}}`, `insert.slider {"at":"C2","link"… |
| `insert.sparkline` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …parkline \| `insert.sparkline {"range":"B2:B… |
| `insert.spinButton` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: …lue":40}`, `insert.spinButton {"at":"C6","l… |
| `insert.symbol` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …, no box), `insert.symbol {"char":"©"}` a… |
| `insert.table` | V | SKILL.md#Command formats (verified): \| table \| `insert.table {"range":"A1:D5","header":true,"style"?,"na… |
| `insert.textBox` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …red text), `insert.textBox {"at","text","wi… |

## link (1)

| id | status | note |
|---|---|---|
| `link.open` | V | reference/auditing-and-helpers.md#Formula auditing, select…: `link.open {"cell"}` → `{opened:"https://ex… |

## macro (9)

| id | status | note |
|---|---|---|
| `macro.check` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: …acro.run`, `macro.check` and `macro.debug` … |
| `macro.debug` | V | reference/newer-commands.md#0.17.0 changes (verified headl…: …check` and `macro.debug` accept `output` (a… |
| `macro.delete` | V | reference/recipes.md#Macros and CSV values (0.14, verified…: …e","to"}`, `macro.delete {"name"}`. |
| `macro.get` | V | reference/recipes.md#Macros and CSV values (0.14, verified…: …cro.list`, `macro.get {"name"}` (the macro … |
| `macro.list` | V | reference/command-sweep.md#Verified in detail, GridCraft s…: … listed by `macro.list`, not here. |
| `macro.record` | V | reference/command-sweep.md#Verified in detail, GridCraft s…: … made with `macro.record` are listed by `ma… |
| `macro.rename` | V | reference/recipes.md#Macros and CSV values (0.14, verified…: …issions`), `macro.rename {"name","to"}`, `m… |
| `macro.run` | V+ | reference/newer-commands.md#0.17.0 changes (verified headl…: `macro.run`, `macro.check` and `macro.debug… · limit: recipes.md: …le paused, `macro.run` is refused ("Finish or stop the macro… |
| `macro.save` | V | reference/recipes.md#Macros and CSV values (0.14, verified…: …orkbook: `macro.save` in one `run` and `m… |

## object (3)

| id | status | note |
|---|---|---|
| `object.delete` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …egrees"}`, `object.delete {"id"}`. |
| `object.move` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …d {"id"}`, `object.move {"id","at"}` ("no s… |
| `object.setAnchorMode` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …orMode}]`, `object.setAnchorMode {"kind","i… |

## pageLayout (16)

| id | status | note |
|---|---|---|
| `pageLayout.background` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …n":true}`, `pageLayout.background {"color"}… |
| `pageLayout.breaks` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …ridlines`, `pageLayout.breaks {"insert":tru… |
| `pageLayout.headerFooter` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …":"1:1"}`, `pageLayout.headerFooter {"heade… |
| `pageLayout.margins` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …e":"A4"}`, `pageLayout.margins {"preset":"n… |
| `pageLayout.orientation` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …ight":0}`, `pageLayout.orientation {"orient… |
| `pageLayout.pageSetup` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …ge setup \| `pageLayout.pageSetup {"orientat… |
| `pageLayout.printArea` | V | reference/formatting-and-sheets.md#Everyday formatting and…: …rgins"?}`, `pageLayout.printArea {"range":"… |
| `pageLayout.printGridlines` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …dscape"}`, `pageLayout.printGridlines`, `pa… |
| `pageLayout.printHeadings` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …narrow"}`, `pageLayout.printHeadings {"on":… |
| `pageLayout.printTitles` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: …Print: `pageLayout.printTitles {"rows":… |
| `pageLayout.scaleToFit` | V | reference/analysis-pivots-charts.md#Analysis and layout to…: … of &N"}`, `pageLayout.scaleToFit {"width":… |
| `pageLayout.size` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: `pageLayout.size {"name":"A4"}`, `pageLayou… |
| `pageLayout.theme` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …e: after `pageLayout.theme {"name":"Ocean… |
| `pageLayout.themeColors` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …Ocean"}` + `pageLayout.themeColors {"name":… |
| `pageLayout.themeEffects` | x | reference/command-sweep.md#Checked, no effect in this vers…: …t. (1): `pageLayout.themeEffects` checke… |
| `pageLayout.themeFonts` | s | reference/auditing-and-helpers.md#Formula auditing, select…: Not run … - Not run: `.xls/.xlsb/.ods` import, `windo… |

## pivot (22)

| id | status | note |
|---|---|---|
| `pivot.addField` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …s/areas`), `pivot.addField {"field":"Units"… |
| `pivot.calculatedField` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: `pivot.calculatedField {"name":"Tax","formu… |
| `pivot.changeSource` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …edium9"}`, `pivot.changeSource {"source":"S… |
| `pivot.collapse` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: `pivot.collapse {"field":"Date","collapse":… |
| `pivot.delete` | V+ | reference/formatting-and-sheets.md#Cell styles, table desi…: …eshed:1}`, `pivot.delete {}`. · limit: analysis-pivots-charts.md: Not run … - Not run: pivot slicers/timelines, `pivot.moveField/removeF… |
| `pivot.fieldList` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …t. (1): `pivot.fieldList` (live) returne… |
| `pivot.fields` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: … --sheet`: `pivot.fields {"pivot"}` (source… |
| `pivot.filter` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …:"desc"}`, `pivot.filter {"field":"Region",… |
| `pivot.grandTotals` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …ion rows), `pivot.grandTotals {"mode":"off"… |
| `pivot.group` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: `pivot.group {"field":"Date","by":"months"}… |
| `pivot.layout` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …computed), `pivot.layout {"layout":"tabular… |
| `pivot.list` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …edium9"}`, `pivot.list {}` (name, anchor, f… |
| `pivot.moveField` | V+ | reference/formatting-and-sheets.md#Cell styles, table desi…: …mainder: `pivot.moveField {"pivot","field… · limit: analysis-pivots-charts.md: Not run … - Not run: pivot slicers/timelines, `pivot.moveField/removeF… |
| `pivot.options` | V | reference/newer-commands.md#New in 0.12.x (verified headle…: - `pivot.options {"enableShowDetails":true}… |
| `pivot.refresh` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …":"off"}`, `pivot.refresh {}` → `{records:2… |
| `pivot.removeField` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …:"rows"}`, `pivot.removeField {"field","are… |
| `pivot.reportLayout` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …bottom"}`, `pivot.reportLayout {"layout":"o… |
| `pivot.showDetails` | V | reference/newer-commands.md#New in 0.12.x (verified headle…: …rue}` then `pivot.showDetails {"cell":"B5"}… |
| `pivot.sort` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: `pivot.sort {"field":"Region","order":"desc… |
| `pivot.style` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …utline"}`, `pivot.style {"style":"PivotStyl… |
| `pivot.subtotals` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …,"area"}`, `pivot.subtotals {"mode":"none\|t… |
| `pivot.valueSettings` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …per cell), `pivot.valueSettings {"field":"S… |

## python (2)

| id | status | note |
|---|---|---|
| `python.output` | V | reference/newer-commands.md#0.16 changes (verified headles…: `python.output {"cell"}` toggles `value` ↔ … |
| `python.set` | V | reference/newer-commands.md#0.16 changes (verified headles…: …n cells: `python.set {"cell":"G1","code":… |

## range (3)

| id | status | note |
|---|---|---|
| `range.fill` | V | reference/log.md#Log: … headless; `range.fill` relative-formula trap found. |
| `range.move` | V | reference/newer-commands.md#0.16.1 changes (verified headl…: - `range.move {"to":"F2","overwrite":true… |
| `range.setValues` | V | SKILL.md#Command formats (verified): …ny cells \| `range.setValues {"range":"A2","values":[["a",3,4.5,"=B2… |

## review (21)

| id | status | note |
|---|---|---|
| `review.addToDictionary` | s | reference/auditing-and-helpers.md#Formula auditing, select…: …d","to"}`, `review.addToDictionary {"word"}… |
| `review.allowEditRanges` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: `review.allowEditRanges {"action":"add","ti… |
| `review.changeSpelling` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …synonyms), `review.changeSpelling {"cell","… |
| `review.checkAccessibility` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: `review.checkAccessibility {}` → `[{issue:"… |
| `review.convertToComments` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: …acy note), `review.convertToComments {}` → … |
| `review.deleteComment` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …n":true}`, `review.deleteComment {"cell"}`,… |
| `review.newComment` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: …d notes: `review.newComment {"cell","text… |
| `review.newNote` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: …{"cell"}`, `review.newNote {…}` (legacy not… |
| `review.nextComment` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …AllNotes`, `review.nextComment\|previousComm… |
| `review.previousComment` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …w. (1): `review.previousComment` (live) … |
| `review.protectSheet` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: …tection: `review.protectSheet {"password"… |
| `review.protectWorkbook` | V | reference/formatting-and-sheets.md#Everyday formatting and…: `review.protectWorkbook` \| |
| `review.replyComment` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: …author"}`, `review.replyComment {"cell","te… |
| `review.resolveComment` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: …author"}`, `review.resolveComment {"cell"}`… |
| `review.showAllNotes` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …"cell"}` / `review.showAllNotes`, `review.n… |
| `review.showComments` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …et,cell}`, `review.showComments {"on":true}… |
| `review.showNote` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …newNote` / `review.showNote {"cell"}` / `re… |
| `review.spelling` | s | reference/formatting-and-sheets.md#Cell styles, table desi…: Not run … - Not run: `.xls/.xlsb/.ods` import (no sam… |
| `review.thesaurus` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …{"cell"}`, `review.thesaurus {"word":"big"}… |
| `review.unprotectSheet` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: `review.unprotectSheet {"password":"bad"}` … |
| `review.workbookStatistics` | V | reference/analysis-pivots-charts.md#Conditional formats, v…: `review.workbookStatistics {}` → per-sheet … |

## selection (8)

| id | status | note |
|---|---|---|
| `selection.column` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …` → `5:5`, `selection.column` → `A1:XFD1048… |
| `selection.currentRegion` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …e found"), `selection.currentRegion` → `{se… |
| `selection.move` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …lection}`, `selection.move {"dr":1,"dc":0,"… |
| `selection.next` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …rl+arrow), `selection.next`, `selection.row… |
| `selection.nextCorner` | V | reference/newer-commands.md#0.16.1 changes (verified headl…: - `selection.nextCorner` moves the acti… |
| `selection.row` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …ion.next`, `selection.row` → `5:5`, `select… |
| `selection.set` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …igation: `selection.set {"range":"A1:B2,D… |
| `selection.stats` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …fillLeft`, `selection.stats`. |

## shape (1)

| id | status | note |
|---|---|---|
| `shape.setText` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: `shape.setText {"id","text"}` (`id` must … |

## sheet (10)

| id | status | note |
|---|---|---|
| `sheet.activate` | V | reference/analysis-pivots-charts.md#Pivot tables and chart…: …ctivated* (`sheet.activate {"sheet":1}`; pa… |
| `sheet.hide` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …,"to":0}`, `sheet.hide/unhide`, `sheet.next… |
| `sheet.move` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …"color"}`, `sheet.move {"sheet":1,"to":0}`,… |
| `sheet.moveColumns` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …{"cols"}`, `sheet.moveColumns {"cols":"B:B"… |
| `sheet.next` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …e/unhide`, `sheet.next/previous`, `home.del… |
| `sheet.previous` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …t. (2): `sheet.previous` (live) before: … |
| `sheet.read` | V | SKILL.md#Command formats (verified): \| read \| `sheet.read {"range":"A1:D5","formulas"?:true,"formatted"?… |
| `sheet.rename` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …w, page: `sheet.rename {"sheet":0,"name":… |
| `sheet.tabColor` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …:"Data"}`, `sheet.tabColor {"sheet","color"… |
| `sheet.unhide` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `sheet.unhide` `{"sheet": "Extra"}` (live) … |

## slicer (4)

| id | status | note |
|---|---|---|
| `slicer.clear` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: … several), `slicer.clear`/`selectAll` (both… |
| `slicer.delete` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: … Filter"), `slicer.delete`. |
| `slicer.selectAll` | s | reference/auditing-and-helpers.md#Formula auditing, select…: Not run … - Not run: `.xls/.xlsb/.ods` import, `windo… |
| `slicer.toggle` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …e SAME run `slicer.toggle {"value":"N"}` (n… |

## table (14)

| id | status | note |
|---|---|---|
| `table.bandedColumns` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `table.bandedColumns\|firstColumn\|lastColumn… |
| `table.bandedRows` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …r\|none"}`, `table.bandedRows\|bandedColumns\|… |
| `table.convertToRange` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …"A1:C5"}`, `table.convertToRange`, `table.r… |
| `table.firstColumn` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `table.firstColumn` `{"table": "T", "on": t… |
| `table.headerRow` | V | reference/auditing-and-helpers.md#Formula auditing, select…: …,sheet}`), `table.headerRow\|bandedColumns\|f… |
| `table.insertSlicer` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …:2}` (also `table.insertSlicer {"column","a… |
| `table.lastColumn` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `table.lastColumn` `{"table": "T", "on": tr… |
| `table.removeDuplicates` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …tToRange`, `table.removeDuplicates {"column… |
| `table.rename` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …edium9"}`, `table.rename {"name"}`, `table.… |
| `table.resize` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …{"name"}`, `table.resize {"range":"A1:C5"}`… |
| `table.style` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …w {"on"}`, `table.style {"style":"TableStyl… |
| `table.summarizePivot` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …irst try), `table.summarizePivot`. |
| `table.totalFunction` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …n":true}`, `table.totalFunction {"column":"… |
| `table.totalRow` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …l"` fine): `table.totalRow {"on":true}`, `t… |

## view (30)

| id | status | note |
|---|---|---|
| `view.arrangeAll` | V+ | reference/command-sweep.md#Verified in detail, GridCraft s…: … view) and `view.arrangeAll` leave no trace… · limit: command-sweep.md: …w. (1): `view.arrangeAll` checked, no effect on a Wayland… |
| `view.customViews` | s | reference/formatting-and-sheets.md#Cell styles, table desi…: Not run … - Not run: `.xls/.xlsb/.ods` import (no sam… |
| `view.formulaBar` | V | reference/command-sweep.md#Verified in detail, GridCraft s…: `view.formulaBar`, `view.ruler` (also in Pa… |
| `view.freezeFirstColumn` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: …. (12): `view.freezeFirstColumn` (live) … |
| `view.freezePanes` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: `view.freezePanes {"cell":"B2"}` → `{freeze… |
| `view.freezeTopRow` | V | reference/recipes.md#More recipes (verified headless): `freeze`: `view.freezeTopRow {}`. |
| `view.gridlines` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.gridlines\|headings\|rightToLeft\|pageLa… |
| `view.headings` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.headings` `{"on": false}` (headless) … |
| `view.hideWindow` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.hideWindow` (live) before: window 4 h… |
| `view.macros` | V | reference/command-sweep.md#Verified in detail, GridCraft s…: …w. (1): `view.macros` headless: `[]` at … |
| `view.newWindow` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.newWindow` (live) before: ui.inspect … |
| `view.normal` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …akPreview`/`view.normal` → `{view}`, `view.… |
| `view.pageBreakPreview` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …r {"on"}`, `view.pageBreakPreview`/`view.no… |
| `view.pageLayout` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.pageLayout` (headless) before: sheet1… |
| `view.rightToLeft` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.rightToLeft` `{"on": true}` (headless… |
| `view.ruler` | V | reference/command-sweep.md#Verified in detail, GridCraft s…: …rmulaBar`, `view.ruler` (also in Page Layou… |
| `view.showHorizontalScrollBar` | V | reference/newer-commands.md#0.16.1 changes (verified headl…: - `view.showHorizontalScrollBar`, `view.s… |
| `view.showObjects` | V | reference/command-sweep.md#Verified in detail, GridCraft s…: …w. (1): `view.showObjects` `{"on":false}… |
| `view.showOutlineSymbols` | V | reference/newer-commands.md#New in 0.12.x (verified headle…: …t":true}`, `view.showOutlineSymbols {"on":t… |
| `view.showSheetTabs` | V | reference/newer-commands.md#0.16.1 changes (verified headl…: …crollBar`, `view.showSheetTabs` take `on`… |
| `view.showVerticalScrollBar` | V | reference/newer-commands.md#0.16.1 changes (verified headl…: …crollBar`, `view.showVerticalScrollBar`, `v… |
| `view.showZeros` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …value`), `view.showZeros\|gridlines\|headin… |
| `view.split` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: … `{view}`, `view.split` |
| `view.statusBar` | V | reference/newer-commands.md#New in 0.12.x (verified headle…: …n":true}`, `view.statusBar {"sum":true,"ave… |
| `view.switchWindows` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.switchWindows` `{"window": 1}` (live)… |
| `view.unfreezePanes` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.unfreezePanes` (live) before: documen… |
| `view.unhideWindow` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.unhideWindow` (live) before: window 4… |
| `view.zoom` | V | reference/formatting-and-sheets.md#Cell styles, table desi…: …e:[1,1]}`, `view.zoom {"percent":120}` (`… |
| `view.zoom100` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.zoom100` (live) before: document.insp… |
| `view.zoomToSelection` | V | reference/command-sweep.md#Verified in detail, GridCraft p…: `view.zoomToSelection` `{"viewWidth": 300, … |

## window (3)

| id | status | note |
|---|---|---|
| `window.activate` | s | reference/auditing-and-helpers.md#Formula auditing, select…: Not run … - Not run: `.xls/.xlsb/.ods` import, `windo… |
| `window.close` | V | reference/newer-commands.md#Newer commands: …hidden}]`; `window.close {"window"?,"doc"?,"force"?}` → `{cl… |
| `window.list` | V | reference/log.md#Log: ….newWindow, window.list/close); `ui.screenshot` timed out (window minimized). |

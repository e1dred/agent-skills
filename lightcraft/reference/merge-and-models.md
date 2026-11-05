# Merge, models (denoise, faces, segmentation), lens, app

## Merge (HDR, panorama, HDR panorama)

- All merges need **real photo files**; a demo photo is refused (*"… is a demo photo; Photo Merge needs photo
  files"*). Make inputs with `lightcraft-cli synth-merge hdr|panorama -o DIR`
  (verified: 3 bracketed DNGs `bracket-0..2.dng`, 5 overlapping PNGs `view-0..4.png`), import them into a library,
  then run the command.
- `merge.panorama {ids?,projection:auto|spherical|cylindrical|perspective,boundaryWarp?,autoCrop?,fillEdges?,
  autoSettings?,stack?,maxMegapixels?,preview?,previewPath?}` — verified: 5 synthetic views wrote
  `view-4-Pano.dng` (7.8 MB) next to the first file and added it to the library (`photos.length` 8 → 9).
  Non-overlapping photos are refused with *"the photos don't overlap enough to be stitched"*.
- `merge.hdr {ids?,align,deghost:none|low|medium|high,autoSettings,stack,preview,previewPath?}` — verified:
  3 bracketed DNGs wrote `bracket-0-HDR.dng` (3.0 MB) and added it (photos 9 → 10). Photos of different sizes are
  refused (*"HDR merge needs photos of the same size"*).
- `merge.hdrBatch {ids?,…}` merges each bracket set (a stack, or photos <1 s apart at exposures ≥ ½ EV apart);
  with our synthetic brackets it merged one set and listed the other in `failed`. With no bracket sets:
  *"no bracket sets among these photos…"*.
- `merge.hdrPanorama {ids?,bracket?,align,deghost,projection,boundaryWarp,autoCrop,fillEdges,autoSettings,
  stack,preview,previewPath?}` — needs photos forming brackets of N at ≥2 positions (*"select at least 4 photos
  to merge"*, *"8 photos don't form brackets of 3 for at least two positions"* with our inputs).
- Shell form: `lightcraft-cli merge hdr|panorama|hdr-panorama|hdr-batch FILES… [--deghost] [--projection]
  [--auto-crop] [--preview OUT.png]`.

## Denoise (AI)

- Needs a model installed; **no model was installed and none was downloaded here** (network rule). Without one:
  `denoise.queue` refuses (*"no denoise model is chosen: install one first"*); `denoise.models.remove/test`
  refuse ("that model is not installed"); `denoise.models.inspect` wants a `denoise-model.json` beside the `.onnx`;
  `denoise.models.install {path,acknowledged:true}` needs readable files.
- Commands that work with nothing installed (verified): `denoise.settings {auto,cacheGb,threads,runOn:auto|gpu|cpu}`,
  `denoise.status`, `denoise.models.list` (`{auto,cacheGb,dir,…}`), `denoise.models.downloads`
  (`{downloads:[],running:false}`), `denoise.models.downloadCancel {id}` (`{discarded:false}`),
  `denoise.models.select {id:null}`, `denoise.pump {pace:pause|light|normal|full}`, `denoise.cancel {id|all}`,
  `denoise.clear`.
- `denoise.toggle {id,enabled?}` applies to **raw photos** only (*"AI Denoise applies to raw photos developed
  from their sensor data"*).
- `denoise.models.download {id,acknowledged:true}` — a model download; not run here.
- `denoise-serve` runs tiles for other computers over TCP (not exercised).

## Faces

- Face work needs two models: **YuNet** (232 KB, MIT) for detection and a recognition model for indexing. Without
  them: `faces.detect` refuses (*"finding faces needs the YuNet face detector…"*), `faces.enable/evaluate/index/
  suggest` refuse (*"no recognition model is chosen"*). No model was downloaded here.
- Verified without models: `faces.gpu {cpuOnly}` (`cpuOnly` false → true), `faces.pump {pace}`,
  `faces.unnamed {limit?}` (`{faces:[],ready:false,total:0}`), `faces.person {name,more?}`
  (`{confirmed:[],more:[],pendingPhotos:0,ready:…}`), `faces.models.list` (`{catalog:{models:0,…}}`),
  `faces.models.downloads`, `faces.models.downloadCancel`, `faces.models.select {id:null}`.
- Refused for lack of data/models: `faces.nameFaces {faces:[{photo,index}],name}`, `faces.renamePerson {from,to,
  merge?}`, `faces.setName {id?,index,name}`, `faces.models.remove/test/install/inspect`.
- `faces.models.download {id,acknowledged:true}` — a model download; not run here.

## Segmentation (SAM 3)

- `segment.model.status` → `{available:false,analyzing,busy,dir}`; `segment.prepare` refuses: *"The SAM 3 model
  is not installed (about 3.4 GB, SAM License)"*; `segment.model.cancel` works (`{cancelled:false}`).
- The same model unlocks `mask.add kind=object|prompt` and `mask.objectPoint`/`mask.refineDetail`.
- `segment.model.download {acknowledged:true}` — a model download; not run here.

## Lens database and app

- `lens.databaseStatus` → `{dir:null, download:{state:"idle"}, lenses:0}`; `lens.downloadDatabase` (verified:
  created the config folder and set the download path) — a network download of the lens database, treat like a
  model download.
- `app.gpu {enabled?,wait?}` — verified disabling: `{enabled:false, available:false, reason:"disabled by
  env/option", lastFallback}`. `LIGHTCRAFT_GPU=0` forbids it for the process.
- `app.memoryBudget {mb?}` — verified 512 MB → `{budget:536870912, cacheBudget:268435456, …}`.
- `activity.list` → `{tasks:[{id,kind,label,done,total,unit,detail,cancellable,cancelling,ageMs}]}`;
  `activity.cancel {id|all}` → `{cancelled}`.
- `focus.pump {pace}` is the out-of-focus preview queue (`{active,last,lookedAt,running}`).

# Library, import, folders, albums, stacks, versions, view state

## Import and folders

- `library.import {paths:[file|dir], mode?: add|copy|move}` — verified with a folder of 2 new images:
  result `{imported:[5,6], failed:[], scanned:2}`; `library.info.photos` rose 4 → 6. `copy` puts originals under
  `Originals/YYYY/YYYY-MM-DD/`; `move` removes the source after verifying the copy.
- `library.importPreview {paths}` lists candidates with duplicate info and adds nothing (Local photos).
  `photo.addToLibrary {ids?}` adopts browsed Local photos.
- `library.browse {path, subfolders?}` → `{new:0, …}` for a folder already imported (verified).
- `library.folders` returns the tree of imported folders (`name`, `path`, `count`, `own`, `children`).
  Folder commands take that path.
- `folder.label {path,label}`, `folder.rename {path,name}`, `folder.move {path,into}`, `folder.scanChanges
  {path,disk?}`, `folder.synchronize {path,disk?,scanned?,importNew?,relinkMoved?,removeMissing?}`,
  `folder.create {parent,name}` — all verified on the test library. `folder.synchronize` returned
  `{imported:3, relinked:0, removed:0, failed:[]}`.
- **A folder imported only through the CLI's startup `--import` was not recognised by `folder.label`,
  `folder.removeFolder` or `folder.scanChanges`** — error *"no photo in the library was imported from it"*.
  A folder imported later with `library.import` worked for every folder command.
- **`folder.rename`/`folder.move` rename the real directory** (verified: `in2` became `in2-renamed` on disk).
- `library.autoImport {folder,copy}`, `library.autoImportScan {listing?,start?}` — the watched folder's settings
  are read back by `library.autoImport`; a scan with `start:true` reported its import.
- `library.autoImportScan {start:false}` returns the `library.import` params instead of importing.
- Preview cache: `library.buildPreviews {size:standard|full, wait:true}`, `library.clearPreviews` (verified:
  disk cache bytes 36,773 → 0), `library.previewProgress`, `library.cancelPreviews`, `library.recheckPreviewOnly`.
- `library.smartPreviews {ids?,discard?,background?}` failed on the library's JPEG/TIFF test photo
  (`failed:[[1, …]]`) — it is for raw files; `library.smartPreviewsLocation {path,reset?,existing?}` set a
  custom folder (`custom:true`).
- `library.missing`/`library.findMissing {folder}` — `findMissing` cleared a real missing list (4 → 0) after the
  photos were found again.
- `library.forgetLocal {dryRun,days}`, `library.compact`, `library.devices` (`[]` with none), `library.memory`,
  `library.retrySidecars` (`{waiting:0,written:0}`), `library.refreshLensProfiles {ids|all}`,
  `library.refresh`, `library.info`, `library.state`.

## Albums

- `album.create {name,parent?,folder?,addSelected?}` → `{id,skipped}`; in the demo library the next id was 8
  (2…7 exist). `albums.list` returns the tree with per-album `count` and `cover`.
- `album.createSmart {name,rules?}` — rules use a Filter: `{rating:4, ratingOp:"atLeast"}` (`atLeast|exactly|atMost`),
  or `ruleSet:{match:all|any|none, rules:[{field,op,value}|{group:ruleSet}]}`; `album.ruleFields` lists the fields.
  Without rules it saves the current view.
- `album.setRules {id,rules?,replace?,fromView?,name?}` — only on a smart album ("not a smart album" otherwise).
- `album.addPhotos {id,ids?}`, `album.removePhotos {id?,ids?}` (`{removed,album}`), `album.rename`, `album.move
  {id,parent|null}`, `album.reorder {id,parent?,before?}` (`{changed}`), `album.setCover {id,photo?}`,
  `album.sort {parent?}` (`{changed}`), `album.delete {id}` (one undo step; photos stay), `album.clearQuick`,
  `album.setTarget {id|null}`, `album.toggleTarget {ids?}` (`{album,added,toggled,skipped}`).

## Stacks and versions

- `stack.group {ids,top,collapsed}` → `{count,stack}` (verified: selection 2 → 1, undo "Group into Stack",
  visibleCount 23 → 24). `stack.ungroup`, `stack.remove`, `stack.toggle {collapsed}`, `stack.collapseAll`,
  `stack.expandAll`, `stack.moveUp/moveDown`, `stack.setTop`, `stack.auto {gap,ids?}`.
- `stack.split` needs the selected photo to be below the top of a stack ("pick a photo below the top of a stack").
- `version.create {name?}` returns `null` and appends to `photo.inspect.versions` (settings snapshot, `auto` flag,
  `created`). `version.delete/rename/restore/update {index}` — `version.restore` re-applies the snapshot
  (exposure 1.0 → −1.0 → restored 1.0), `version.update` replaces the stored settings.

## History, undo, journal

- `edit.undo` / `edit.redo` verified on a develop edit (exposure 1.0 ↔ 0.0, `edited` timestamp follows).
- `history.list {id?}` → `{cursor, history:[labels], versions:[]}`. With a single step the cursor is 0 and both
  `history.previous` and `history.next` refuse (*"at the first/latest History step"*) — add a second edit first.
- `history.clear`, `history.restore {index}` (verified: contrast 30 → 0 at index 0).
- `journal.list {limit?}` returns the last commands of the session (persistence debugging aid).

## View, filter, selection

- `library.state` is the read for all of this: `source`, `sourceLabel`, `filter`, `sort`, `selection{active,ids}`,
  `visibleCount`, `undo`/`redo` labels, `clipboard`, `activeMask`, `activeSpot`.
- `library.source {kind: all|recentlyAdded|album|recentlyDeleted|picks|missing|libraryFolder, id?, path?}`.
- `library.filter {text,rating,ratingOp:atLeast|exactly|atMost,flag,flags,label,kind,edited,date,keyword,person,
  camera,libraryFolder}` — `{rating:3}` cut visibleCount 24 → 15; `library.clearFilter` restored it;
  `library.toggleFilters` sets a filter aside and brings it back.
- `library.sort {key:captureDate|importDate|editDate|fileName|rating|fileSize|random,ascending,group,seed}`;
  `library.shuffle {seed}` sets key `random` with that seed.
- `library.select {ids,active?,mode:replace|add|toggle|range}`, `library.selectAll`, `library.selectNone`,
  `library.selectBy {flag,rating,ratingOp:gte|eq|lte,label,add?}` (**note the different enum** from album rules),
  `library.up/down {rows?}`, `library.next/previous`, `library.holdView`, `library.groups {by}`.
- `library.findSimilar {id,similarity?,filter?}` filters the view to similar photos (0 found for the synthetic
  gradient test photo).
- `library.preferences` (import presets, per-camera presets, cacheMb…), `library.xmpPreferences {autoWrite,naming}`,
  `library.toggleAutoWriteXmp`.

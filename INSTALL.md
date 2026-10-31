# Installing a skill from this repo (for AI assistants)

A user has asked you to add one or more skills from this repo. Put the skill folders in your harness's own skills directory
(you know where that is); this file covers what is specific to the repo. Install only the skills the user named (all seven if they ask for all).

## What counts as a skill

A top-level folder that contains a `SKILL.md`: `wordcraft/`, `gridcraft/`, `deckcraft/`, `photocraft/`,
`cadcraft/`, `onlyoffice/`, `genoffice-supplement/`. Copy the **whole folder** with all its subfolders, not just `SKILL.md`:
skills keep reference pages, helper scripts, recipes and examples next to it, and `SKILL.md` points to them. `styles/`, `everyday/` and `smoke-tested/` are
not skills; do not install them.

## How to fetch

Clone with `--depth 1` (a full clone is slower and not needed) into a scratch directory, copy the folders, and delete the clone:

```sh
git clone --depth 1 https://gitlab.com/e1dred/agent-skills.git /path/to/scratch/agent-skills
```

Copy the folders (`cp -r`); do not symlink them to the clone, because you delete the clone afterwards. (`install.sh` in
the repo root symlinks into `~/.claude/skills` and is meant for people who keep a clone; do not use it here.)

After copying and before deleting the clone, write the commit you copied from into `<skill>/.installed-from` (`git -C <clone> rev-parse HEAD`; the file holds only that hash), so the skill
can later tell whether the repo has moved on (each `SKILL.md` has an `Updates` note that uses it).

If the skill is already in the user's skills directory, do not overwrite it: treat the request as an update (see "Updating"
below, which also covers a symlink into a clone). Installed skills check for a newer commit themselves and offer the
update; they never update on their own.

If your harness has no skills feature, you can still read a `SKILL.md` as plain instructions (for example by
referencing it from `AGENTS.md`).

## Updating an installed skill

Only when the user has said yes to an update. Work in a scratch directory **outside** the skills directory, and leave the
installed folder untouched until the user has chosen what to do.

- `OLD` is the hash in `<skill>/.installed-from` (trim whitespace).
- `NEW` is the repo's current `HEAD`: `git ls-remote <url> HEAD`, the hash on the line that ends in exactly `HEAD` (ignore other lines).
- **Backup:** every path below except "keep mine" first copies the installed folder to `<skill>.bak`, next to it (a sibling),
  never inside it. If `<skill>.bak` already exists, use `<skill>.bak-YYYYMMDD-HHMM` (current date and time) instead. Tell the
  user where the backup is.

```sh
git clone --depth 1 https://gitlab.com/e1dred/agent-skills.git new
git -C new fetch --depth 1 origin OLD        # the version that was installed (GitLab allows fetching by hash)
```

1. **Compare with `OLD`.** Ignore `.installed-from` throughout.
   - *Edited:* a file in `git -C new ls-tree -r --name-only OLD -- <skill>` whose installed copy differs from
     `git -C new show OLD:<path>` (`cmp`).
   - *Added:* a file in the installed folder that is not in `OLD`'s tree.
   - *Deleted upstream:* a file in `OLD`'s tree that is not in `NEW`'s.
2. **Nothing edited:** no choices to offer. Make the backup, remove the installed folder, copy the new one in (`cp -r`), then
   put any *added* files back and tell the user which ones you kept (or that nothing was lost).
3. **Something edited:** list the edited (and added) files and offer three choices; do not pick one yourself.
   - **Overwrite:** make the backup, remove the installed folder, copy the new one in. Say that the user's edits and added
     files are now only in the backup.
   - **Keep mine:** change nothing, including `.installed-from`.
   - **Merge:** make the backup, then build the result file by file:
     - edited by the user and changed upstream: `git merge-file -p <mine> <base> <theirs>`, where `<base>` is a file you write
       with `git -C new show OLD:<path> > <base>` and `<theirs>` is the file in the new clone;
     - edited by the user only: keep the user's version;
     - not edited by the user: take the new version (this includes files new upstream);
     - added by the user: keep;
     - deleted upstream: remove it if the user did not edit it; if they did, keep it and say so. Remove folders left empty.

     `git merge-file` exits with the number of conflicts. Show each conflict to the user and settle it with them, then write
     the file with no markers left (`grep -c '<<<<<<<'` must be 0). When keeping both sides, put a blank line between them so
     Markdown does not run them together.
4. **Finish:** write `NEW` (hash only) into `.installed-from` once the update is complete; delete the clone.

**No base:** if `OLD` cannot be fetched (history rewritten) or the folder has no `.installed-from` at all (copied by hand or
before this file existed), you cannot tell the user's edits from upstream changes. Offer only overwrite (with the backup)
or keep mine, and say why. After an overwrite, write `.installed-from` so the next update has a base.

**A clone, not a copy:** if the installed skill is a symlink into a git clone of this repo (what `install.sh` makes) or the
folder sits inside such a clone, it is a developer install: do not replace it. Updating it is `git -C <clone> pull`, and
only if the user asks.

## Parts that need the full repo

A single skill folder stands alone for everyday use. A few things point at the repo root and only work in a full clone:
`../check-versions.sh` and `../coverage.sh` (version and coverage checks), and the document-style builders that read
`../styles/` (in `wordcraft`, `onlyoffice` and `genoffice-supplement`). If the user needs those, ask them to keep a clone
and do not delete yours.

## After copying

- Installing a skill does **not** connect its app. Each skill's `SKILL.md` (and its `README.md`, where there is one) says
  how to connect: MCP server, launch flags, CLI version. Tell the user about any manual steps, such as starting the
  app first. Most of the skills expect the app to be installed already.
- The skills are meant to grow: most `SKILL.md` files ask the assistant to add what it learns to the skill's own files (notes,
  `reference/`, a log). So an installed copy collects local edits over time, which is why an update offers to merge
  them (see "Updating" above). Mention this to the user.
- `genoffice-supplement` only adds to GenOffice's own skills, which come with GenOffice and are not in this repo.
  It is not useful without them.
- Tell the user to restart or reload their session if your harness needs that to pick up new skills.

## Trust

A skill is instructions you will follow later. Skim what you install and tell the user if anything in it asks
for something unexpected (credentials, network access unrelated to the app, running unknown downloads).

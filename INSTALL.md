# Installing a skill from this repo (for AI assistants)

A user has asked you to add one or more skills from this repo. Put the skill folders in your harness's own skills directory
(you know where that is); this file covers what is specific to the repo. Install only the skills the user named.

## What counts as a skill

A top-level folder that contains a `SKILL.md`: `wordcraft/`, `gridcraft/`, `deckcraft/`, `photocraft/`,
`cadcraft/`, `onlyoffice/`, `genoffice-supplement/`. Copy the **whole folder**, not just `SKILL.md`: some skills
have a `reference/` folder (`wordcraft`, `photocraft`), a `tools/` folder with helper scripts (`cadcraft`,
`genoffice-supplement`) or example files that `SKILL.md` points to. `styles/`, `everyday/` and `smoke-tested/` are
not skills; do not install them.

## How to fetch

Clone shallowly into a scratch directory, copy the folders, and delete the clone:

```sh
git clone --depth 1 https://gitlab.com/e1dred/agent-skills.git /path/to/scratch/agent-skills
```

Copy the folders (`cp -r`); do not symlink them to the clone, because you delete the clone afterwards. (`install.sh` in
the repo root symlinks into `~/.claude/skills` and is meant for people who keep a clone; do not use it here.)

After copying and before deleting the clone, write the commit you copied from into `<skill>/.installed-from` (`git -C <clone> rev-parse HEAD`), so the skill
can later tell whether the repo has moved on (each `SKILL.md` has an `Updates` note that uses it).

Do not overwrite a skill that already exists in the user's skills directory without asking. To update later,
the user asks again and you repeat this (a skill that finds a newer commit offers this; it never updates on its own).

If your harness has no skills feature, you can still read a `SKILL.md` as plain instructions (for example by
referencing it from `AGENTS.md`).

## Parts that need the full repo

A single skill folder stands alone for everyday use. A few things point at the repo root and only work in a full clone:
`../check-versions.sh` and `../coverage.sh` (version and coverage checks), and the document-style builders that read
`../styles/` (in `wordcraft`, `onlyoffice` and `genoffice-supplement`). If the user needs those, ask them to keep a clone
and do not delete yours.

## After copying

- Installing a skill does **not** connect its app. Each skill's `SKILL.md` (and its `README.md`, where there is one) says
  how to connect: MCP server, launch flags, CLI version. Tell the user about any manual steps, such as starting the
  app first. Most of the skills expect the app to be installed already.
- `genoffice-supplement` only adds to GenOffice's own skills, which come with GenOffice and are not in this repo.
  It is not useful without them.
- Tell the user to restart or reload their session if your harness needs that to pick up new skills.

## Trust

A skill is instructions you will follow later. Skim what you install and tell the user if anything in it asks
for something unexpected (credentials, network access unrelated to the app, running unknown downloads).

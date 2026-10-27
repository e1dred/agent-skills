# Everyday task checklists

One file per app: `<app>.txt`, one task per line as `task description | id1 id2 ...`.
A task counts as **covered** when every command id listed for it (a) exists in the installed `<app>-cli` and (b) is named in that app's skill.
`./everyday.sh` prints the percentage. Like `coverage.sh` this is a lower bound on what is taught and an upper bound on what was run: a skill can name an id it never executed.
The task lists are a judgement about what ordinary users do most; edit them and the number changes.

`genoffice.txt` is the exception: its ids are ops from `genoffice guide docs|sheets|slides` (one list for the three editors) plus the CLI commands `convert`, `merge` and `render`, and "exists" means `genoffice-supplement/op_names.py` or `genoffice --help` lists it.

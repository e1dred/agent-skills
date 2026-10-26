# Everyday task checklists

One file per app: `<app>.txt`, one task per line as `task description | id1 id2 ...`.
A task counts as **covered** when every command id listed for it (a) exists in the installed `<app>-cli` and (b) is named in that app's skill.
`./everyday.sh` prints the percentage. Like `coverage.sh` this is a lower bound on what is taught and an upper bound on what was run: a skill can name an id it never executed.
The task lists are a judgement about what ordinary users do most; edit them and the number changes.

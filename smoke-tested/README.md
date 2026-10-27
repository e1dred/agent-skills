# Smoke-tested command ids

`coverage.sh` counts a command as documented when its id appears in the skill, which says nothing about how well it was checked. These files list the ids that were **only smoke-tested**: run on a scratch document and accepted (or refused with a recorded reason) without looking at the result, apart from a changed/unchanged comparison of the saved file for some. One id per line, `<app>.txt`.

To verify an id properly: run it on a document where the effect is visible, look at a render or read the value back, write what was seen into the skill, and delete the id from the list. `wc -l smoke-tested/*.txt` is the number left to do.

Not listed: ids that were run and looked at in earlier rounds, and ids skipped on purpose (printing, plug-in and preference writes, window management).

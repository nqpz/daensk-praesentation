HTML=dænsk-præsentation/index.html

$(HTML): dænsk-præsentation.md $(shell find media)
	.venv/bin/mdslides $< --include media

.PHONY: run
run: $(HTML)
	surf -bdgmn $< &

HTML=dænsk-præsentation/index.html

$(HTML): dænsk-præsentation.md $(shell find media)
	mdslides $< --include media

.PHONY: run
run: $(HTML)
	surf -bdgmn $< &

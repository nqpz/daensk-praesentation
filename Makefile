HTML=dænsk-præsentation/index.html

$(HTML): dænsk-præsentation.md $(find media)
	mdslides $< --include media

.PHONY: run
run: $(HTML)
	firefox $<

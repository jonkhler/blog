SOURCE_FOLDER=.
BUILD_FOLDER=build
TARGET_FOLDER=${HOME}/html/blog

# Ensure BUILD_FOLDER exists
$(BUILD_FOLDER):
	mkdir -p $(BUILD_FOLDER)

all: $(BUILD_FOLDER)/index.html $(BUILD_FOLDER)/code.css

clean:
	rm -rf $(BUILD_FOLDER)

install:
	cp $(BUILD_FOLDER)/index.html $(TARGET_FOLDER)/index.html
	cp $(SOURCE_FOLDER)/reset.css $(TARGET_FOLDER)/reset.css
	cp $(SOURCE_FOLDER)/index.css $(TARGET_FOLDER)/index.css
	cp $(BUILD_FOLDER)/code.css $(TARGET_FOLDER)/code.css

$(BUILD_FOLDER)/code.css: pandoc-style.sh $(BUILD_FOLDER)
	./pandoc-style.sh > $@

$(BUILD_FOLDER)/processed.md: index.md mdcat.py $(BUILD_FOLDER)
	./mdcat.py $< > $@

$(BUILD_FOLDER)/index.html: $(BUILD_FOLDER)/processed.md $(BUILD_FOLDER)/code.css template.html Makefile $(BUILD_FOLDER)
	pandoc --toc -s --css reset.css --css index.css --css code.css -i $< -o $@ --template=template.html

.PHONY: all clean
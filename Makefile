DIRECTORY := integration
DRIVER    := hetznercloud

default: test

clean:
	@rm -rf $(DIRECTORY)

init: clean
	@molecule init role -d $(DRIVER) $(DIRECTORY)

test:
	@cd $(DIRECTORY) && molecule test

.PHONY: clean init test

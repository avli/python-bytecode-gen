test:   install
    pytest

install:
    pip install .

.PHONY: test install
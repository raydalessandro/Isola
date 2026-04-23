.PHONY: world validate world-check

world:
	python3 tools/build_world.py

validate:
	python3 tools/validate.py

world-check: world
	@git diff --exit-code world/ || (echo "WORLD NOT DETERMINISTIC"; exit 1)

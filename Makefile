SCRIPT := \
	for n in $$(seq 1 9); \
		do python3 src/main.py instance_test$$n.json out_test$$n.json; \
	done

run:
	@python3 src/main.py instance_smallest.json out_smallest.json;
	@$(SCRIPT)



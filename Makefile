STD_INSTANCES := \
	for n in $$(seq 1 10) ; do \
		for m in $$(seq 1 10) ; do \
		python3 src/main.py instance_$$n.json I$${n}S$${m}.json $$m ; \
		done \
	done

STATIC_SEED := \
	for n in $$(seq 1 10) ; do \
		python3 src/main.py instance_$$n.json out_$$n.json 0 ; \
	done

GEN_INSTANCES := \
	for n in $$(seq 1 10) ; do \
		python3 src/main.py instance_m$$n.json out_m$$n.json ; \
	done

run:
	@$(STATIC_SEED)
#	@$(STD_INSTANCES)
#	@$(GEN_INSTANCES)

gen:
	python3 src/gen.py instance_m1.json Instance_M001 4 600 2 1000 1 2 0.2
	python3 src/gen.py instance_m2.json Instance_M002 4 800 2 1000 1 2 0.4
	python3 src/gen.py instance_m3.json Instance_M003 6 800 2 1200 1 2 0.2
	python3 src/gen.py instance_m4.json Instance_M004 6 800 2 1200 2 2 0.4
	python3 src/gen.py instance_m5.json Instance_M005 6 1400 4 1200 2 3 0.2
	python3 src/gen.py instance_m6.json Instance_M006 6 1400 4 1200 2 3 0.4
	python3 src/gen.py instance_m7.json Instance_M007 8 1600 4 1400 2 3 0.2
	python3 src/gen.py instance_m8.json Instance_M008 8 1600 4 1400 3 3 0.4
	python3 src/gen.py instance_m9.json Instance_M009 8 1800 6 1400 3 4 0.2
	python3 src/gen.py instance_m10.json Instance_M010 8 1800 6 1400 3 4 0.4
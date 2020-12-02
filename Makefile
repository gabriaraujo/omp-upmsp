RUN_CONSTRUCTIVE := \
	for n in $$(seq 1 10) ; do \
		for m in $$(seq 1 5) ; do \
		python3 src/main.py instance_$$n.json constructive/I$${n}S$${m}.json -seed $$m ; \
		done \
	done

RUN_LAHC := \
	for n in $$(seq 1 10) ; do \
		for m in $$(seq 1 5) ; do \
		python3 src/main.py instance_$$n.json heuristic/lahc/I$${n}S$${m}.json -algorithm lahc -seed $$m ; \
		done \
	done

RUN_SA := \
	for n in $$(seq 1 10) ; do \
		for m in $$(seq 1 5) ; do \
		python3 src/main.py instance_$$n.json heuristic/sa/I$${n}S$${m}.json -algorithm sa -seed $$m ; \
		done \
	done

RUN_INVERSE_LAHC := \
	for n in $$(seq 1 10) ; do \
		for m in $$(seq 1 5) ; do \
		python3 src/main.py instance_$$n.json inverse/sa/I$${n}S$${m}.json -constructive premodel -algorithm lahc -seed $$m ; \
		done \
	done

RUN_INVERSE_SA := \
	for n in $$(seq 1 10) ; do \
		for m in $$(seq 1 5) ; do \
		python3 src/main.py instance_$$n.json inverse/sa/I$${n}S$${m}.json -constructive premodel -algorithm sa -seed $$m ; \
		done \
	done

RUN_FEEDBACK_LAHC := \
	for n in $$(seq 1 10) ; do \
		for m in $$(seq 1 5) ; do \
		python3 src/main.py instance_$$n.json feedback/lahc/I$${n}S$${m}.json -feedback 5 -algorithm lahc -seed $$m ; \
		done \
	done

RUN_FEEDBACK_SA := \
	for n in $$(seq 1 10) ; do \
		for m in $$(seq 1 5) ; do \
		python3 src/main.py instance_$$n.json feedback/sa/I$${n}S$${m}.json -feedback 5 -algorithm sa -seed $$m ; \
		done \
	done

GEN_INSTANCES := \
	for n in $$(seq 1 10) ; do \
		python3 src/main.py instance_m$$n.json out_m$$n.json ; \
	done

run:
	@$(RUN_CONSTRUCTIVE)

run-lahc:
	@$(RUN_LAHC)

run-sa:
	@$(RUN_SA)

run-inverse:
	@$(RUN_INVERSE_LAHC)
	@$(RUN_FEEDBACK_SA)

run-feedback:
	@$(RUN_FEEDBACK_LAHC)
	@$(RUN_FEEDBACK_SA)

all: run run-lahc run-sa run-inverse run-feedback

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
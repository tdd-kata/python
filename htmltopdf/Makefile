.PHONY: all
all: test

.PHONY: test
test: clean
	@echo "TODO: Testing"

.PHONY: clean
clean:
	@rm -f *.pdf
	@# rm -f *.html

.PHONY: docker-build
docker-build:
	docker build . -t htmltopdf:0.1.0

.PHONY: docker-run
docker-run:
	docker run -d --name htmltopdf -p 5000:5000 htmltopdf:0.1.0

version = 0.1.1

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
	sudo docker build . -t htmltopdf:${version}

.PHONY: docker-run
docker-run:
	sudo docker run -d --name htmltopdf -p 5000:5000 htmltopdf:${version}

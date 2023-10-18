version = 0.1.11
image_name = htmltopdf
container_name = htmltopdf

.PHONY: all
all: clean

.PHONY: clean
clean: docker-rmi
	@rm -f *.pdf
	@# rm -f *.html

.PHONE: run
run:
	python3 chromium-api.py

.PHONY: docker-build-chromium
docker-build-chromium:
	sudo docker build . -f Dockerfile-chromium -t ${image_name} -t ${image_name}:${version}

.PHONY: docker-build-webkit
docker-build-webkit:
	sudo docker build . -f Dockerfile-webkit -t ${image_name} -t ${image_name}:${version}

.PHONY: docker-run
docker-run:
	sudo docker run -d --name ${container_name} -p 5000:5000 ${image_name}:${version}

.PHONY: docker-stop
docker-stop:
	sudo docker rm -f ${container_name}

.PHONY: docker-logs
docker-logs:
	sudo docker logs -f ${container_name}

.PHONY: docker-rmi
docker-rmi:
	@# https://www.gnu.org/software/make/manual/html_node/Errors.html#Errors-in-Recipes
	-sudo docker rmi ${image_name}
	sudo docker rmi $$(sudo docker images '${image_name}' -a -q)

.PHONY: check-docker-layers
check-docker-layers:
	sudo docker history ${image_name}:${version}

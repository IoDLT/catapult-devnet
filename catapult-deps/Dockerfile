FROM ubuntu:18.04

WORKDIR /usr/src/app

RUN mkdir ./deps
ADD install_base_deps_ubuntu.sh .
ADD install_cat_deps.sh .

RUN chmod 744 install_base_deps_ubuntu.sh 
RUN chmod 744 install_cat_deps.sh

RUN ./install_base_deps_ubuntu.sh
RUN ./install_cat_deps.sh

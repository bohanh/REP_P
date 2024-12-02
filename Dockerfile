FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y gcc-11 g++-11 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 100 && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 100

RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    gnupg \
    lsb-release \
    software-properties-common \
    ca-certificates \
    build-essential \
    libncurses5-dev \
    libssl-dev \
    libffi-dev \
    python3-pip \
    python3-dev \
    unzip \
    tar \
    libgraphviz-dev \
    m4 \
    ocamlbuild \
    && apt-get clean

RUN apt-get install -y gcc-11 g++-11

RUN wget https://golang.org/dl/go1.18.1.linux-amd64.tar.gz -P /tmp && \
  tar -C /usr/local -xvzf /tmp/go1.18.1.linux-amd64.tar.gz && \
  ln -s /usr/local/go/bin/go /usr/bin/go && \
  rm /tmp/go1.18.1.linux-amd64.tar.gz

RUN wget https://download.java.net/java/GA/jdk21/fd2272bbf8e04c3dbaee13770090416c/35/GPL/openjdk-21_linux-x64_bin.tar.gz -P /tmp && \
  tar -xvzf /tmp/openjdk-21_linux-x64_bin.tar.gz -C /usr/local && \
  ln -s /usr/local/jdk-21/bin/java /usr/bin/java && \
  ln -s /usr/local/jdk-21/bin/javac /usr/bin/javac && \
  rm /tmp/openjdk-21_linux-x64_bin.tar.gz

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
  apt-get install -y nodejs=18.16.0-1nodesource1

RUN wget https://github.com/ocaml/ocaml/archive/refs/tags/4.13.1.zip -P /tmp && \
    unzip /tmp/4.13.1.zip -d /tmp && \
    cd /tmp/ocaml-4.13.1 && \
    ./configure && \
    make && \
    make install && \
    rm -rf /tmp/ocaml-4.13.1 /tmp/4.13.1.zip

RUN wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz -P /tmp && \
  tar -xvzf /tmp/Python-3.10.12.tgz -C /tmp && \
  cd /tmp/Python-3.10.12 && \
  ./configure --enable-optimizations && \
  make && \
  make install && \
  rm -rf /tmp/Python-3.10.12 /tmp/Python-3.10.12.tgz

RUN ln -sf /usr/local/bin/python3.10 /usr/bin/python3 && \
  ln -sf /usr/local/bin/pip3.10 /usr/bin/pip3

RUN apt-get autoremove -y && \
  apt-get clean

COPY . /workspace/
WORKDIR /workspace

RUN gcc --version && \
  go version && \
  java -version && \
  node -v && \
  ocaml -version && \
  python3 --version

CMD [ "bash" ]
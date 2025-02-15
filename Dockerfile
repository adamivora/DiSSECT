FROM sagemath/sagemath-dev:9.0

# Setup sage and jupyter
RUN sage -i database_kohel
RUN sage --pip3 install --no-cache-dir notebook

# Conform to mybinder
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV HOME /home/sage
ENV TARGET "${HOME}/dissect"
COPY . ${TARGET}

USER root
RUN usermod -l ${NB_USER} sage
RUN chown -R ${NB_UID} ${TARGET}

# Install DiSSECT
USER ${NB_USER}
WORKDIR ${TARGET}
RUN sage --pip3 install --upgrade -r requirements.txt
RUN sage --pip3 install --editable .
ENV PATH "${HOME}/sage/local/bin:${PATH}"
ENTRYPOINT []

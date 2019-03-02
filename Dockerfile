FROM mdstudio/cerise-mdstudio-base:0.3.2

COPY api /home/cerise/api
RUN chown -R cerise:cerise /home/cerise/api

COPY conf/config.yml /home/cerise/conf/config.yml

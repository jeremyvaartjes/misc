#!/bin/bash

QUANTIY=1
REGION=syd1
SIZE=s-1vcpu-512mb-10gb
SSH_KEY=INSERT_SSH_FINGERPRINT

counter=1
while [ $counter -le $QUANTIY ]
do
    agentid=$(uuidgen)
    echo -n "Starting up buildkite-do-${agentid}..."

    doctl compute droplet create buildkite-do-${agentid} \
        --image ubuntu-22-04-x64 \
        --enable-ipv6 \
        --region ${REGION} \
        --size ${SIZE} \
        --ssh-keys ${SSH_KEY} \
        --tag-name buildkite \
        --user-data-file ~/.my-scripts/bk-config.yml \
        > ~/.my-scripts/doctl.log

    ((counter++))
    echo " [done]"
done
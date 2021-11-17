#!/usr/bin/env bash

if [[ -z "${MY_ENV_VARIABLE}" ]]; then
    echo "The environment variable MY_ENV_VARIABLE is empty (zero length)"
else
    echo "The environment variable MY_ENV_VARIABLE is set to"
    echo "  ${MY_ENV_VARIABLE}"
fi
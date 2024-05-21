#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

alembic upgrade head
cd src
uvicorn main:app --reload --host 0.0.0.0 --port 8080
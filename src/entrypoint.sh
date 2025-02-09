#!/bin/bash
set -e
python3 -m uvicorn "large_data_api.main:create_app" --factory --host 0.0.0.0 --port 8000

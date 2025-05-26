#!/usr/bin/env bash

# Build web application
cd web || exit
npm ci
npm run build

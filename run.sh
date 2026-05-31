#!/bin/bash

# Minimal Jekyll build and serve script

bundle install
bundle exec jekyll serve --incremental --watch


case "${1:-serve}" in
  serve)
    serve
    ;;
  static)
    serve_static
    ;;
  *)
    echo "Usage: ./run.sh [serve|static]"
    exit 1
    ;;
esac
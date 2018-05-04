#!/usr/bin/env bash
swagger-codegen generate -i https://api.rokka.io/doc.json -l python -o . -c config.json
for i in patches/*.patch; do patch -p1 < $i; done

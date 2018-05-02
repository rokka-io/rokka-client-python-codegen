#!/usr/bin/env bash
swagger-codegen generate -i http://api.rokka.test/app_dev.php/api/doc.json -l python -o . -c config.json
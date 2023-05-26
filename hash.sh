#!/bin/bash

echo "Please Enter a Phrase to Hash:"
read phrase
echo -n $phrase | openssl dgst -sha256

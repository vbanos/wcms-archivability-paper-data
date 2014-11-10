#!/bin/bash

for i in {1..128} ;
do
    ( rqworker -b identify & )
done

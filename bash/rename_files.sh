#!/bin/bash

## convert spaces to underscores
for f in *; 
    do mv "$f" "`echo $f | tr "[:space:]" "_"`"; 
done

## change all uppercase to lowercase
for f in *; 
    do mv "$f" "`echo $f | tr "[:upper:]" "[:lower:]"`"; 
done

## remove any trailing underscores
for f in *; 
    do mv "$f" $(echo $f | sed -e 's/_$//'); 
done

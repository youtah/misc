#!/bin/bash
 
disphelp ()
{
    echo "this is your help"
    exit 0
}
 
while getopts u:d:p:f:h: option
do
    case "${option}"
    in
        u)
            USER=${OPTARG}
            ;;
        d)
            DATE=${OPTARG}
            ;;
        p)
            PRODUCT=${OPTARG}
            ;;
        f)
            FORMAT=$OPTARG
            ;;
        h)
            disphelp
            ;;
    esac
done
 
echo "The user ${USER} on date ${DATE} bought product ${PRODUCT} in a format of ${FORMAT}"


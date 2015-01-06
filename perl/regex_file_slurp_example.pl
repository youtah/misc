#!/usr/bin/env perl
 
use strict;
use warnings;
use feature 'say';
use Data::Dumper;
use File::Slurp;
 
my @wanted
    = grep { /\P{Alpha}/ }
    read_file('/usr/share/dict/words', chomp => 1 );
 
#print "$_\n" for @wanted;
say for @wanted;


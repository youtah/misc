#!/usr/bin/env perl

use strict;
use warnings;
use feature 'say';

my $money = shift;
my @billz = ( 100000, 10000, 5000, 1000, 100, 50, 20, 10, 5, 2, 1 );
my %prezz = (
                100000  => 'Wilson',
                10000   => 'Chase',
                5000    => 'Madison',
                1000    => 'Cleveland',
                500     => 'McKinley',
                100     => 'Franklin',
                50      => 'Grant',
                20      => 'Jackson',
                10      => 'Hamilton',
                5       => 'Lincoln',
                2       => 'Jefferson',
                1       => 'Washington'
            );

say "\$$money in the fewest number of bills would be: ";

for (my $index=0; $index<=$#billz; $index++ ) {
    my $current_bill = $billz[$index];
    my $divided = int($money / $current_bill);
    if ($divided > 0) {
        $money = $money-($divided*$current_bill);
    }
    my $current_bill_prez = $prezz{$current_bill};
    if ( $divided > 1 ) {
        say "There are $divided ".$current_bill_prez."s.";
    }
    if ( $divided == 1 ) {
        say "There is $divided $current_bill_prez.";
    }
}

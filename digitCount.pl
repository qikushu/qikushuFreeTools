#!/usr/bin/perl

use strict;
use warnings;

my %countHash;
while(<STDIN>) {
	chomp;
	if ($countHash{$_}) {
		$countHash{$_}++;
	} else {
		$countHash{$_} = 1;
	}
}

foreach my $i (keys(%countHash)) {
	print "$i\t$countHash{$i}\n"
}


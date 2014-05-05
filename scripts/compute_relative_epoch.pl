#!/usr/bin/perl

$USAGE = "$0 [querytweet-epoch-mapping] [qrel]\n";

$epoch = shift || die $USAGE;
$qrel = shift || die $USAGE;

open(FILE, "< $epoch");
while (<FILE>) {
    @arr = split;
    $TOPIC{$arr[0]} = $arr[2];
}
close(FILE);

open(FILE, "< $qrel");
while (<FILE>) {
    s/[\n\r]+$//;
    @arr = split;
    $diff = $TOPIC{$arr[0]} - $arr[4];
    print $_ . " $diff\n";
}
close(FILE);

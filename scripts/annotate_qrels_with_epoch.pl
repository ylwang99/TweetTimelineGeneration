#!/usr/bin/perl

$USAGE = "$0 [tweetid-epoch-mapping] [qrel]\n";

$epoch = shift || die $USAGE;
$qrel = shift || die $USAGE;

open(FILE, "< $epoch");
while (<FILE>) {
    @arr = split;
    $TWEETID{$arr[0]} = $arr[1];
}
close(FILE);

open(FILE, "< $qrel");
while (<FILE>) {
    s/[\n\r]+$//;
    @arr = split;
    print $_ . " " . $TWEETID{$arr[2]} . "\n";
}
close(FILE);

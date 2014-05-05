#!/usr/bin/perl

$f = shift;
$q = shift;

open(FILE, "< $f");
while (<FILE>) {
    @arr = split(/\t/, $_);
    $qtext = $arr[1];
    $qtext =~ s/"/\\"/g;
    $TOPIC{$arr[0]} = $qtext;
}
close(FILE);

open(FILE, "< $q");
while (<FILE>) {
    @arr = split(/\s+/, $_);

    $H{$arr[0]} .= "[ \"$arr[2]\", $arr[5], $arr[3] ],\n";
}
close(FILE);

print "var dataset = {\n";
foreach $k ( sort keys %H ) {
    $q = $TOPIC{$k};
    $k =~ /\d+/;
    $d = $& + 0.0;
    print "\"$d\" : { \"query\" : \"$q\", \n\"qrels\" : [ $H{$k} ] },\n";
}
print "};\n";

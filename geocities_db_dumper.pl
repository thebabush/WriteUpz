#!/usr/bin/perl

use strict;
use DBI;

my $qq = $ARGV[0];

print "ARGS: $qq\n";

my $dbh = DBI->connect(
    "dbi:mysql:dbname=geocities;host=icectf_mariadb",
    "geocities",
    "geocities",
    { RaiseError => 1 },
) or die $DBI::errstr;

my $sth = $dbh->prepare($qq);
$sth->execute();

my @row;
while (@row = $sth->fetchrow_array) {
    print join(", ", @row), "\n";
}

$sth->finish();
$dbh->disconnect();


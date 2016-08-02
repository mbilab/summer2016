#!/usr/bin/perl -w
use strict;
use CGI;
my $cgi = new CGI;
my $id = $cgi->param('id');
sleep 1; # pretend a long response time to show the loading message
print "Content-type: text/plain\n\n"; # watch out the content type is plain text
print "$id,<br />nice to meet you."; # but we still return HTML, since the handler use it as HTML

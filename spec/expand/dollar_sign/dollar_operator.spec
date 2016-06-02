# outside of a cluster definition the dollar sign is not a metacharacter
$foo
$foo

# inside a cluster, in the definition of 'baz' the dollar sign represents the contents of an adjacent key
@baz
bar1
bar2

%other_cluster:quuuux
qqqqq1
qqqqq2

%other_cluster:bazz
bar1
bar2


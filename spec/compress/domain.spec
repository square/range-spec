# Multiple hosts collapse to common domain
{bar,foo}.example.com
bar.example.com
foo.example.com

# Sorted
{bar,foo}.example.com
foo.example.com
bar.example.com

# Single host
foo.example.com
foo.example.com

# Multiple domains
{bar,foo}.a,{baz,qux}.b
baz.b
foo.a
qux.b
bar.a

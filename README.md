Range Spec
==========

A proof-of-concept language agnostic spec for the range query language. Range
libraries should be able to expand all expressions in `spec/expand`, and
compress result sets in `spec/compress`.

Each directory contains `.spec` files with the following format:

* Any line beginning with a `#` is a comment.
* First line is a range expression.
* Subsequent lines are results.
* Blank lines separate examples.

See `example` directory for a sample loader.

Sub-directories should be traversed when searching for `.spec` files. Any
`.yaml` files in the same directory as a spec should be used for the range
state to evaluate the expression against.

Drivers should verify that the library converts all examples in `spec/expand`
from expression to result, and the reverse for `spec/compress`.

Status
------

Skeleton only, very incomplete.

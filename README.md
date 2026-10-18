# rehearsal-python-example

A small, intentionally broken python project for verifying [Rehearsal](https://github.com/aman-a-shah/rehearsal) against a real GitHub repository. It contains ordinary source files and tests. Rehearsal generates the repair during a run.

## Reproduce

```sh
python -m unittest discover -s tests -v
```

One test should fail on `main`.

## Incident to investigate

Customers are overcharged for small orders. discounted_total should round the final discounted subtotal once to the nearest cent using ROUND_HALF_UP. An order of three items at $0.05 each with a 10% discount should cost $0.14, but it costs $0.15. Preserve validation of negative quantities and invalid discounts.

Import this repository into Rehearsal, use the test command above, and run a rehearsal. Review the generated diff and test output before creating a draft pull request. The broken default branch is kept as a repeatable example.

# useful-skills

Portable, reusable skills for AI agents. Each skill is self-contained, markdown-driven, and designed to plug into agent runtimes (Claude Code, Anthropic SDK Managed Agents, OpenAI Assistants, custom orchestrators) with minimal glue.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## What is a skill?

A skill is a directory with:

- **`SKILL.md`** — the entry point. YAML frontmatter declares `name` and `description` (with explicit TRIGGER / DO-NOT-TRIGGER conditions for the agent's router). The body is the workflow the agent executes.
- **`resources/`** — reference data the agent loads lazily (only when the workflow needs it).
- **`examples/`** — worked examples in the skill's declared output format, plus an anti-example showing what the skill refuses to do.

Skills here aim for three properties:

1. **Deterministic where possible.** The agent's decision points are reduced to lookups in structured resources, not free-form reasoning.
2. **Source-anchored.** Every claim, value, or principle traces back to a primary source. No LLM-generated reference data masquerading as canonical.
3. **Refuse-with-reframe.** Out-of-scope problems are rejected explicitly, with a hint at where the user should go instead.

## Skills in this repo

### Engineering & problem-solving

- **[`triz-engineering-solver`](triz-engineering-solver/SKILL.md)** — Apply Altshuller's TRIZ (Theory of Inventive Problem Solving) to resolve engineering contradictions. Uses the Ideal Final Result, 39 engineering parameters, 40 inventive principles, the Contradiction Matrix, Su-Field analysis with the 76 Standard Solutions, ARIZ-85C deep procedure, and the 8 trends of system evolution. Produces 3–5 concrete inventive concepts with ideality scores rather than compromise solutions.

## Using a skill with Claude Code

```bash
# clone into your skills directory
git clone https://github.com/<your-fork>/useful-skills ~/.claude/skills/useful-skills

# the skill is now available as e.g. `triz-engineering-solver`
# invoke it by describing a matching problem to Claude Code
```

For other runtimes (Anthropic SDK, OpenAI, custom), point the agent's system prompt or tool router at `SKILL.md` and grant filesystem access to the skill's directory.

## Repo layout

```
.
├── README.md
├── LICENSE                       MIT
├── CONTRIBUTING.md               anchor-cell verification protocol, style rules
└── triz-engineering-solver/
    ├── SKILL.md                  entry point — workflow, triggers, output template
    ├── resources/                lazily-loaded reference data
    │   ├── 39_parameters.md
    │   ├── 40_principles.md
    │   ├── 76_standard_solutions.md
    │   ├── contradiction_matrix.json
    │   ├── separation_principles.md
    │   ├── ariz_85c.md
    │   ├── evolution_trends.md
    │   ├── glossary.md
    │   └── output_template.md
    └── examples/
        ├── brake_disc.md         mechanical / thermal contradiction
        ├── battery_pack.md       physical contradiction via separation
        └── anti_example_misframed.md   refuse-with-reframe demo
```

## Status

- `triz-engineering-solver`: **release-ready**. Workflow complete. Contradiction matrix is the full Altshuller 39×39 — 1190 populated cells (with 292 cells legitimately empty per Altshuller's original; documented fallback for those). Three worked examples + one anti-example.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New skills welcome — they must follow the structure above, ship with examples + an anti-example, and source-anchor any reference data.

## License

MIT — see [LICENSE](LICENSE).

## Authors

- [Antropocosmist](https://github.com/Antropocosmist)
- Claude

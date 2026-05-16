# Contributing

Thanks for considering a contribution. This repo hosts portable skills for AI agents — each skill must be self-contained, deterministic where possible, and verifiable by a third party.

## Ground rules

1. **Every claim must be sourceable.** If a skill cites a methodology, technique, or dataset, the reference must trace back to a primary source (book, paper, recognised community resource). LLM-generated content masquerading as canonical reference data will be rejected.
2. **Skills are markdown-first.** A skill is consumed by an AI agent reading `SKILL.md` and lazily loading `resources/`. Code is allowed only when it gives the agent a capability that a markdown reference cannot.
3. **Examples are deliverables.** Each skill must include at least 2 worked examples following its declared output template, plus 1 anti-example showing what the skill should *refuse* to do (out-of-scope behaviour).
4. **Don't pad.** Three excellent examples are better than ten shallow ones.

## How to add a new skill

1. Create `<skill-name>/` at the repo root.
2. Inside it, write `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: <skill-name>
   description: <one paragraph — start with what the skill does, then list TRIGGER conditions and DO NOT TRIGGER conditions so an agent's router can match it correctly>
   ---
   ```
3. Add `resources/` for reference data (loaded lazily by the agent).
4. Add `examples/` with at least 2 worked examples + 1 anti-example.
5. Open a PR.

## Anchor-cell verification protocol (TRIZ matrix contributions)

The classic 39×39 Altshuller contradiction matrix is widely paraphrased online, but most freely available copies are LLM-generated or incomplete. **Any matrix contribution must satisfy the following anchor cells** (cross-referenced against Altshuller 1985):

```
(1, 3)  ⊇ {15, 8, 29, 34}
(1, 9)  ⊇ {2, 8, 15, 38}
(1, 14) ⊇ {28, 27, 18, 40}
(1, 27) ⊇ {3, 11, 1, 27}
(14, 1) ⊇ {1, 8, 40, 15}
```

**Match by set, not by order.** Multiple authoritative transcriptions (Altshuller 1985, Mann 2003, Salamatov 1999, the widely-circulated Casey-Perno-2007 XLS) reorder the same principle set for the same cell — different sources rank by ID, by Altshuller's suggested priority, or by frequency-in-patent-database. Reordering is normal; missing principles are not.

If a candidate dataset disagrees on the *set* for any anchor cell, **reject it** — it is not canonical Altshuller.

When submitting a replacement matrix:
- Include the source citation in `contradiction_matrix.json` under `meta.primary_source`.
- Run the anchor check before opening a PR.
- For cells whose source is uncertain, omit them entirely (the agent falls back to reasoning over the 40 principles) — never guess.

## Open contribution opportunities

- **`triz-engineering-solver`: add worked examples** from non-mechanical domains (electronics, chemical engineering, optics, biotech, software-with-physical-substrate) following the format of `examples/brake_disc.md` or `examples/heat_exchanger_fouling.md`.
- **`triz-engineering-solver`: add a `business-triz` companion skill** that adapts the workflow to non-physical contradictions (organisational, process, supply-chain) using Souchkov's Business TRIZ adaptation. Keep the engineering skill scoped to physical systems; the business adaptation is a separate skill.
- **New skills welcome** — see "How to add a new skill" above.

## Style

- Markdown only for docs. Use fenced code blocks with language identifiers.
- One blank line between paragraphs; no trailing whitespace.
- Cite sources inline with `Source:` markers in deliverables.
- Avoid emojis unless the skill's domain genuinely benefits from them.

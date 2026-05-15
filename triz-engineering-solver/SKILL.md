---
name: triz-engineering-solver
description: Apply Altshuller's TRIZ (Theory of Inventive Problem Solving) to resolve engineering contradictions and produce inventive concepts instead of compromise solutions. TRIGGER when the user describes a technical trade-off ("improving X makes Y worse"), a physical contradiction (one element must have opposite properties), a design bottleneck where conventional optimization has stalled, or explicitly asks for inventive / non-obvious / breakthrough engineering solutions. Uses the Ideal Final Result (IFR), 39 engineering parameters, 40 inventive principles, Contradiction Matrix, Su-Field analysis, and resource mapping. DO NOT TRIGGER for software architecture without a physical analogue, UX/UI design, business strategy, organizational problems, or open brainstorming where no concrete contradiction has been identified — TRIZ degrades into generic advice outside physical/technical systems.
---

# TRIZ Engineering Solver

A systematic analytical engine for solving engineering problems with Genrich Altshuller's Theory of Inventive Problem Solving (TRIZ). Replaces trial-and-error brainstorming with algorithmic problem-solving over a corpus of patent-derived patterns.

## When to use

- Engineering trade-offs where improving parameter A degrades parameter B (technical contradiction)
- A single element must exhibit opposite properties (physical contradiction)
- Design bottleneck where conventional optimization has plateaued
- System redesign aimed at the Ideal Final Result

## When NOT to use

- Pure software architecture without a physical analogue
- UX / interaction design
- Business or organizational strategy
- Open brainstorming with no concrete contradiction identified

## Inputs required

Before analysis, collect from the user:

1. **System description** — current engineering system and its primary function
2. **Problem statement** — the specific bottleneck or undesired effect
3. **Contradiction parameters** — which parameter must improve, which one degrades
4. **Constraints** — environmental, cost, manufacturing, physical limits
5. **Available resources** — substances, fields, geometry, byproducts, environment

If any input is missing, use the self-prompting block in `## Intake prompt` below.

## Workflow

### Step 1 — Formulate the Ideal Final Result (IFR)

Describe the outcome where:
- The desired function is achieved perfectly
- No additional cost, complexity, or harmful side-effect is introduced
- Only existing internal / external / temporal resources are used
- The problem "solves itself"

Question to drive Step 1: *"In an ideal world, how would this system achieve [desired function] using only what already exists, with zero added complexity?"*

### Step 2 — Classify the contradiction

**Technical contradiction**: improving parameter A causes parameter B to worsen.
- *Example*: increasing strength (A) increases weight (B).

**Physical contradiction**: a single element must exhibit opposite properties simultaneously or under different conditions.
- *Example*: a surface must be rough (for grip) and smooth (for low friction).

Physical contradictions are typically resolved by **separation** in space, time, structure (parts vs. whole), or condition. Technical contradictions are resolved via the Contradiction Matrix → Inventive Principles.

### Step 3 — Map to the Contradiction Matrix

1. Identify the **improving parameter** from the 39 — see `resources/39_parameters.md`.
2. Identify the **worsening parameter** from the 39.
3. Look up the cell in `resources/contradiction_matrix.json`. The cell lists 3–4 recommended inventive principle IDs.
4. For each suggested principle, retrieve its full description and sub-principles from `resources/40_principles.md`.
5. Apply the principles to the concrete system to generate candidate solutions.

> **Note**: `resources/contradiction_matrix.json` ships with a structural skeleton and a populated set of well-documented canonical cells. For cells marked `null`, fall back to reasoning over the 40 principles directly, and clearly flag in the output that the suggestion is LLM-inferred rather than matrix-derived. Authoritative full matrices are published in Altshuller (1985) and Mann (2003).

### Step 4 — Su-Field (Substance–Field) analysis

Model the system's function as a triad:
- **S1** — object being acted upon
- **S2** — tool / agent acting on S1
- **F** — field carrying the action (mechanical, thermal, chemical, electromagnetic, gravitational, acoustic)

Diagnose:
- **Incomplete system** (missing S2 or F): add the missing element, preferring existing resources.
- **Insufficient/ineffective interaction**: introduce a more controllable field, intermediate substance, or field additive.
- **Harmful interaction**: insert a barrier substance, introduce a counteracting field, or modify field properties.

For systematic Su-Field transformations, the canonical reference is the **76 Standard Solutions** (Altshuller, grouped into 5 classes). Not all are included in this skill's resources — fall back to reasoning if needed and flag.

### Step 5 — Resource utilization

Enumerate before generating concepts:

- **Internal resources**: unused properties of components, byproducts, idle time, geometric features (holes, surfaces, edges).
- **External resources**: environmental substances (air, water, gravity), environmental fields (magnetic, thermal gradients), supersystem (adjacent systems).
- **Temporal resources**: pre-process preparation, post-process utilization, parallel operations.

Prefer concepts that consume **free** resources over concepts requiring new components.

### Step 6 (optional) — ARIZ deepening

For hard problems where the 40-principles pass yielded no strong concept, switch to **ARIZ** (Algorithm for Inventive Problem Solving) — a formal step-by-step procedure that reframes the problem mini-problem → operational zone → operational time → substance-field resources → IFR-1 → physical contradiction → standard solution. Out of scope for this skill's quickstart workflow; invoke explicitly when the user asks for "deep TRIZ" or "ARIZ analysis".

### Step 7 (optional) — Trends of Engineering System Evolution

For prognostic / roadmapping questions ("where will this technology go next?"), map the system to the 8 trends (e.g. *increasing ideality*, *transition to micro-level*, *uneven development of parts*, *segmentation*, *dynamization*, *transition to supersystem*). Out of scope for the contradiction-resolution workflow above.

## Output format

Generate a structured analysis containing the sections below. Keep each section tight; this is an engineering deliverable, not an essay.

### 1. Contradiction statement

```
Technical contradiction: improving [Parameter A, with #] causes [Parameter B, with #] to worsen.
— OR —
Physical contradiction: [Element X] must be [Property 1] AND [Property 2].
  Separation strategy candidate: [space | time | structure | condition].
```

### 2. Ideal Final Result

```
IFR: The system achieves [desired function] using [existing resource],
without adding [cost/complexity/harm], where [problem element] solves itself.
```

### 3. Inventive concepts (3–5)

For each concept:

- **Concept name** — short descriptive title
- **TRIZ principle(s) applied** — number + name (from `resources/40_principles.md`)
- **Source** — `matrix` (cell-derived) or `inferred` (LLM reasoning over principles)
- **Description** — specific, actionable engineering solution (2–3 sentences)
- **Resource utilized** — which internal / external / temporal resource is leveraged
- **Implementation path** — high-level technical pathway
- **Risks / open questions** — what would need to be validated experimentally

### 4. Principle-to-concept summary table

| # | Concept | Principle(s) | Key resource | Risk level |
|---|---------|--------------|--------------|------------|

## Intake prompt

If any required input is missing, ask the user:

```
To run TRIZ analysis I need:

[ ] System description — what is the system and its primary function?
[ ] Problem statement — what bottleneck or unwanted effect must be resolved?
[ ] Contradiction — which parameter must improve, and which one degrades?
[ ] Constraints — cost, dimensional, environmental, manufacturing limits?
[ ] Resources — substances, fields, geometry, byproducts available?

Please fill the gaps so I can generate inventive concepts.
```

## Agent instructions

1. **Intake** — collect all five inputs; do not proceed with placeholders.
2. **Analysis** — execute Steps 1–5 in order. Steps 6–7 only on explicit request.
3. **Synthesis** — produce 3–5 concrete concepts, not generic advice.
4. **Citation** — always reference principle by `#NN — Name` and mark `Source: matrix` vs `Source: inferred`.
5. **Validation** — every concept must (a) name the principle, (b) name the resource it consumes, (c) state at least one open risk.
6. **Anti-pattern** — never compromise between A and B; the point of TRIZ is to *resolve* the contradiction, not split the difference.

## Example application

See `examples/brake_disc.md` for a worked case (automotive brake disc — friction vs. heat dissipation).

## Resources

- `resources/39_parameters.md` — the 39 engineering parameters with definitions
- `resources/40_principles.md` — the 40 inventive principles with sub-principles
- `resources/contradiction_matrix.json` — 39×39 matrix skeleton with canonical entries
- `examples/brake_disc.md` — worked example

## References

- Altshuller, G. (1984). *Creativity as an Exact Science*.
- Altshuller, G. (1999). *The Innovation Algorithm: TRIZ, Systematic Innovation and Technical Creativity*.
- Mann, D. (2002). *Hands-On Systematic Innovation*.
- Souchkov, V. *Breakthrough Thinking with TRIZ for Business and Management*.

## Tags

#triz #engineering #problem-solving #innovation #systematic-invention #contradiction-resolution #inventive-principles

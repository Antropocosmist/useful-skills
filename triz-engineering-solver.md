# TRIZ Engineering Solver

A systematic analytical engine for solving complex engineering problems using Genrich Altshuller's Theory of Inventive Problem Solving (TRIZ). This skill replaces trial-and-error brainstorming with algorithmic problem-solving to overcome engineering compromises and discover breakthrough innovations.

## Purpose

Apply TRIZ methodology to identify and resolve engineering contradictions, formulate ideal solutions, and generate actionable inventive concepts using proven patterns from thousands of patents.

## Usage

Invoke this skill when facing:
- Engineering trade-offs where improving one parameter degrades another
- Design bottlenecks requiring innovative solutions
- System optimization challenges
- Technical contradictions that seem unsolvable

## Input Requirements

Before analysis, gather the following information:

1. **System Description**: What is the current engineering system and its primary function?
2. **Problem Statement**: What specific problem or bottleneck needs resolution?
3. **Contradiction Parameters**: 
   - Which parameter are you trying to improve?
   - Which parameter degrades as a result?
4. **Constraints**: What environmental, cost, or physical constraints exist?
5. **Available Resources**: What materials, energy, fields, or system components are available?

## TRIZ Analysis Workflow

### Step 1: Formulate the Ideal Final Result (IFR)

Define the ideal outcome where:
- The desired function is achieved perfectly
- No additional cost, complexity, or harm is introduced
- Existing resources within or around the system are utilized
- The problem "solves itself"

**Prompt**: "In an ideal world, how would this system achieve [desired function] using only what already exists, with zero added complexity?"

### Step 2: Identify the Contradiction Type

Classify the problem:

**Technical Contradiction**: Improving parameter A causes parameter B to worsen
- Example: Increasing strength (A) increases weight (B)
- Example: Improving speed (A) reduces reliability (B)

**Physical Contradiction**: A single element must exhibit opposite properties
- Example: A component must be hot (for process A) and cold (for process B)
- Example: A surface must be rough (for grip) and smooth (for low friction)

### Step 3: Apply the Contradiction Matrix & 40 Inventive Principles

For **Technical Contradictions**, map to the TRIZ Contradiction Matrix:

**39 Engineering Parameters** (abbreviated list):
1. Weight of moving object
2. Weight of stationary object
3. Length of moving object
4. Length of stationary object
5. Area of moving object
6. Area of stationary object
7. Volume of moving object
8. Volume of stationary object
9. Speed
10. Force
11. Stress or pressure
12. Shape
13. Stability of object's composition
14. Strength
15. Duration of action by moving object
16. Duration of action by stationary object
17. Temperature
18. Illumination intensity
19. Use of energy by moving object
20. Use of energy by stationary object
21. Power
22. Loss of energy
23. Loss of substance
24. Loss of information
25. Loss of time
26. Quantity of substance/matter
27. Reliability
28. Measurement accuracy
29. Manufacturing precision
30. Object-affected harmful factors
31. Object-generated harmful factors
32. Ease of manufacture
33. Ease of operation
34. Ease of repair
35. Adaptability or versatility
36. Device complexity
37. Difficulty of detecting and measuring
38. Extent of automation
39. Productivity

**40 Inventive Principles** (core set):
1. Segmentation
2. Taking out / Extraction
3. Local quality
4. Asymmetry
5. Merging / Consolidation
6. Universality
7. Nested doll (Matryoshka)
8. Anti-weight / Counterweight
9. Preliminary anti-action
10. Preliminary action
11. Beforehand cushioning
12. Equipotentiality
13. The other way round / Inversion
14. Spheroidality / Curvature
15. Dynamics
16. Partial or excessive actions
17. Another dimension
18. Mechanical vibration
19. Periodic action
20. Continuity of useful action
21. Skipping / Rushing through
22. "Blessing in disguise" / Convert harm into benefit
23. Feedback
24. Intermediary
25. Self-service
26. Copying
27. Cheap short-living objects
28. Mechanics substitution
29. Pneumatics and hydraulics
30. Flexible shells and thin films
31. Porous materials
32. Color changes
33. Homogeneity
34. Discarding and recovering
35. Parameter changes
36. Phase transitions
37. Thermal expansion
38. Strong oxidants / Accelerated oxidation
39. Inert atmosphere
40. Composite materials

**Matrix Lookup Process**:
1. Identify the improving parameter (row)
2. Identify the worsening parameter (column)
3. Extract the 3-4 recommended principles from the intersection
4. Apply these principles to generate specific solutions

### Step 4: Su-Field (Substance-Field) Analysis

Analyze the system's functional model:
- **S1**: First substance (object being acted upon)
- **S2**: Second substance (tool/agent performing action)
- **F**: Field (energy/interaction: mechanical, thermal, chemical, electromagnetic, gravitational)

**Incomplete Systems** (missing elements):
- Add missing substance or field to complete the interaction
- Use available resources from the environment

**Inefficient Systems** (weak interaction):
- Introduce more controllable field
- Add intermediate substance
- Use field additives or modifiers

**Harmful Systems** (unwanted effects):
- Insert barrier substance
- Introduce counteracting field
- Modify field properties

### Step 5: Resource Utilization

Identify and leverage hidden resources:

**Internal Resources**:
- Unused properties of existing components
- Waste products or byproducts
- Idle time in process cycles
- Geometric features (holes, surfaces, edges)

**External Resources**:
- Environmental substances (air, water, gravity)
- Environmental fields (magnetic, thermal gradients)
- Supersystem resources (adjacent systems)

**Temporal Resources**:
- Pre-process preparation
- Post-process utilization
- Parallel operations

## Output Format

Generate a structured analysis containing:

### 1. Contradiction Definition
```
Technical Contradiction: Improving [Parameter A] causes [Parameter B] to worsen.
OR
Physical Contradiction: [Element X] must be [Property 1] and [Property 2] simultaneously.
```

### 2. Ideal Final Result Statement
```
IFR: The system achieves [desired function] using [existing resource], 
without adding [cost/complexity/harm], where [problem element] solves itself.
```

### 3. Inventive Concepts (3-5 solutions)

For each concept, provide:
- **Concept Name**: Brief descriptive title
- **TRIZ Principle Applied**: Which principle(s) from the 40
- **Description**: Specific, actionable engineering solution (2-3 sentences)
- **Resource Utilized**: What existing or free resource is leveraged
- **Implementation Approach**: High-level technical pathway

**Example Format**:
```
Concept 1: Segmented Thermal Zones
TRIZ Principle: #1 Segmentation, #3 Local Quality
Description: Divide the component into multiple thermal zones with independent 
temperature control. Each zone maintains optimal temperature for its specific 
function, eliminating the need for the entire component to be uniformly heated 
or cooled.
Resource Utilized: Existing thermal gradients in the system
Implementation: Apply zone-specific insulation and localized heating elements
```

### 4. Principle Explanation Summary
Brief table mapping each concept to its TRIZ principle with one-line rationale.

## Self-Prompting Mechanism

If any required input is missing, prompt the user with:

```
To apply TRIZ analysis, I need the following information:

[ ] System Description: What is the engineering system and its primary function?
[ ] Problem Statement: What specific bottleneck or challenge exists?
[ ] Contradiction: What parameter improves and what parameter worsens?
[ ] Constraints: What environmental, cost, or physical limits apply?
[ ] Resources: What materials, energy, or components are available?

Please provide the missing information so I can generate inventive solutions.
```

## Agent Instructions

When this skill is invoked:

1. **Intake Phase**: Collect all required inputs using the self-prompting mechanism
2. **Analysis Phase**: Execute the 5-step TRIZ workflow systematically
3. **Synthesis Phase**: Generate 3-5 specific, actionable concepts
4. **Documentation Phase**: Format output according to the structured template
5. **Validation Phase**: Ensure each concept clearly states which TRIZ principle was applied and why

**Key Principles for AI Agents**:
- Be specific, not generic. "Add a counterweight" is better than "balance the system"
- Reference actual TRIZ principles by number and name
- Explain the logical connection between the principle and the proposed solution
- Prioritize solutions that use existing resources over adding new components
- Focus on eliminating contradictions, not compromising between them

## Example Application

**Input**:
- System: Automotive brake disc
- Problem: Brake fade during prolonged use
- Contradiction: Increasing friction (for braking power) increases heat generation (causing fade)
- Constraints: Must fit existing wheel assembly, cost-sensitive
- Resources: Airflow from wheel rotation, existing disc geometry

**Output**:

**Contradiction**: Technical Contradiction - Improving friction (Parameter 10: Force) worsens heat dissipation (Parameter 17: Temperature increases)

**IFR**: The brake disc dissipates heat using the rotational airflow it already generates, without adding external cooling systems, where the disc cools itself during operation.

**Concept 1: Radial Ventilation Channels**
- TRIZ Principle: #1 Segmentation, #17 Another Dimension
- Description: Machine radial channels into the disc that act as centrifugal air pumps, drawing cool air from the center and expelling hot air at the perimeter. The faster the wheel spins, the more cooling occurs.
- Resource Utilized: Rotational kinetic energy (free resource)
- Implementation: CNC mill radial vanes between disc faces during manufacturing

**Concept 2: Phase-Change Material Integration**
- TRIZ Principle: #36 Phase Transitions, #35 Parameter Changes
- Description: Embed phase-change material (PCM) capsules within the disc structure that absorb heat by melting during braking, then release it gradually when cooling. Acts as thermal buffer.
- Resource Utilized: Latent heat capacity of PCM (thermal resource)
- Implementation: Cast disc with PCM-filled cavities or apply PCM coating

**Concept 3: Surface Microstructure Modification**
- TRIZ Principle: #3 Local Quality, #15 Dynamics
- Description: Create microscopic surface patterns that increase effective surface area by 300% without changing disc dimensions. Patterns also generate turbulent airflow for enhanced convection.
- Resource Utilized: Existing disc surface (geometric resource)
- Implementation: Laser texturing or chemical etching of friction surface

## References

- Altshuller, G. (1984). *Creativity as an Exact Science*
- Altshuller, G. (1999). *The Innovation Algorithm: TRIZ, systematic innovation and technical creativity*
- Mann, D. (2002). *Hands-On Systematic Innovation*
- TRIZ Contradiction Matrix (39x39 parameters)

## Tags

#triz #engineering #problem-solving #innovation #systematic-invention #contradiction-resolution #inventive-principles

---

**Skill Version**: 1.0
**Created**: 2026-04-23
**Portability**: Universal - applicable to any AI agent with reasoning capabilities
**Dependencies**: None - self-contained methodology
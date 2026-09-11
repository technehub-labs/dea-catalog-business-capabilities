---
id: BC-SR-A001
catalog: dea-catalog-business-capabilities
catalog_release_under_review: v1-alpha.4 (with v1-alpha.0..v1-alpha.4 history considered)
catalog_release_commit: 570830ab14a7b9436a4b230b67729ade65f13575
reviewer: (external review, identity withheld in transcription)
reviewer_affiliation: external
date_filed: 2026-09-10
filing_repo: technehub-labs/dea-catalog-business-capabilities
carrier_cr: CR-DEA-BC-12
status: fully-actioned
scope: Full catalog v1-alpha.0..v1-alpha.4: methodology, ECF semantic alignment, foundational gap analysis, repository/doc drift
---

# BC-SR-A001: Submittal Review of Business Capability Catalog v1-alpha.4

**Status:** triaged (see `submittal-reviews/README.md` § Lifecycle).
**Carrier CR:** [`change-requests/CR-DEA-BC-12.md`](../change-requests/CR-DEA-BC-12.md).
**Source:** external review filed 2026-09-10 against the released v1-alpha.4 catalog (commit `570830a`).

---

I reviewed the current Business Capability catalog, its methodology/taxonomy, the individual capability records, and the current ECF domain-grounding specification. My conclusion is that the catalog is substantially stronger than a conventional capability map, but there are some important foundational gaps: and, more importantly, several ECF coordinate assignments that appear semantically inconsistent with the ECF itself.

Business Capability catalog⁠
ECF / Metaframework⁠

1. Executive assessment

The catalog currently contains 26 canonical first-order capabilities. The repository has deliberately adopted the principle that capabilities are derived independently from the ECF and that the ECF merely provides contextual coordinates. That is architecturally correct. 

The current 26 cover a lot:

* Enterprise direction/governance
* Workforce
* Customers/partners/suppliers
* Offerings and marketing
* Operations
* Technology/information/analytics
* Assets/facilities
* Finance
* Risk/security/regulation/legal
* Continuity/change/innovation

So I would not expand the catalog aggressively. The first-order set should remain deliberately small.

However, I see four significant foundational gaps:

1. Organizational Design / Organization Management
2. Enterprise Performance Management
3. Generic Party / Stakeholder Relationship Management
4. Knowledge / Learning Management: possibly, but this one needs stronger evidence before admission.

And I see three major ECF-placement problems:

1. Strategy and Strategic Planning are placed in Governance & Existence, despite the ECF explicitly placing strategic direction in Strategy & Direction.
2. Asset, Facility and Technology Management are placed in Strategy & Direction, despite the ECF explicitly moving physical/virtual enabling resources into Enablement & Operations.
3. Supplier Management and Sourcing & Procurement are also placed in Strategy & Direction, where the semantic distinction between strategic sourcing and operational acquisition needs to be made much more carefully.

Those are more important than simply adding capabilities.

⸻

2. What the current catalog gets right

The 26-capability set is impressively disciplined.

The repository explicitly rejects the common mistake of turning the ECF’s 49 cells into 49 capabilities. It says the capability comes first and the coordinate second. 

That is exactly the right architecture:

Capability = what enduring ability exists
ECF = where/when that ability is contextualized

This distinction is particularly important because the ECF itself states that the 49 coordinates are classification contexts rather than entity containers. 

The catalog also has a good evidence discipline: candidate → observed → corroborated → normalized → ECF mapped → reviewed → canonical. 

I would preserve that rigor.

⸻

3. Current foundational landscape

The current 26 can be grouped roughly as follows:

ECF Domain	Current capabilities	Assessment
Governance & Existence	Enterprise Governance, Risk Management, Security Management, Regulation Management, Legal Matter Management, Continuity Management, Change Management, Strategy, Strategic Planning	Overloaded
Strategy & Direction	Asset Management, Facility Management, Technology Management, Supplier Management, Sourcing & Procurement	Semantically questionable / misplaced
Agency & Organization	Workforce Planning, Workforce Management	Under-represented
Party & Relationship	Marketing, Customer Management, Partner Management	Supplier currently elsewhere
Product & Value	Offering Management, Idea Management	Reasonable but innovation chain is thin
Enablement & Operations	Operations, Information Management, Analytics & Intelligence	Under-represented relative to domain definition
Finance & Accounting	Financial Stewardship, Financial Resource Management	Strong

This distribution is itself revealing.

The ECF has seven domains, but the capability population should not necessarily be numerically balanced. Nevertheless, the current distribution tells us where the conceptual model is probably underdeveloped.

⸻

4. Gap #1: Organizational Design / Organization Management

This is the clearest foundational gap.

The ECF explicitly defines Agency & Organization as owning:

* organizational design
* agent capacity planning
* acquisition/onboarding
* development/performance
* coordination/collaboration
* movement/transition. 

The catalog currently has:

* Workforce Planning
* Workforce Management

Workforce Planning is explicitly about determining the workforce required and when. 

Workforce Management covers acquiring, developing, deploying and releasing the workforce, including human and artificial agents. 

But neither capability is actually organization design.

That distinction matters enormously in the emerging enterprise model.

I would therefore investigate:

Organizational Design

The ability to design the enterprise’s organizational structures, roles, authorities, and coordination patterns through which agency is organized.

This becomes even more important because the ECF has deliberately evolved Agency & Organization beyond traditional HR. It explicitly includes human, artificial and hybrid agents. 

Why this is foundational

An enterprise needs to determine:

what agents exist → how they are organized → what authority they have → how they collaborate → how capacity is allocated.

Workforce Management addresses the agents.

Workforce Planning addresses future workforce requirements.

Organizational Design addresses the structure that makes the agents an enterprise.

I would rank this Priority 1.

⸻

5. Gap #2: Enterprise Performance Management

This is, in my view, the most important functional gap.

The catalog contains Analytics and Intelligence, but analytics is not the same thing as enterprise performance management.

The current capability is explicitly:

deriving decision-grade insight from information. 

That’s an intelligence capability.

But the ECF Strategy & Direction domain explicitly includes:

* objectives and targets
* strategic planning
* strategic adaptation. 

The enterprise needs an enduring ability to:

define → measure → evaluate → govern → adapt performance.

That is not merely analytics.

I’d investigate a capability such as:

Enterprise Performance Management

The ability to define, monitor, evaluate, and improve enterprise performance against intended objectives and targets.

Potential ECF:

Primary: Strategy & Direction × Operate
Secondary: Strategy & Direction × Improve
possibly Finance & Accounting × Operate as a contextual coordinate.

This would give the framework an important closed loop:

Strategy → Planning → Performance → Insight → Adaptation → Change

At present, that loop is incomplete.

And this matters because the broader OpenDEAM objective is explicitly a cycle of Describe → Assess → Identify Gap → Decide → Transform → Measure → Reassess. 

Without a first-order performance capability, the capability catalog doesn’t fully express the Measure/Reassess portion of that loop.

I would rank this Priority 1.

⸻

6. Gap #3: Generic Party / Stakeholder Relationship Management

This is more subtle.

The ECF definition of Party & Relationship is actually broader than the current catalog.

It explicitly says the domain encompasses:

customer, supplier, partner, regulator, community

and that the domain owns the enterprise’s external relationship fabric. 

But the catalog has:

* Customer Management
* Partner Management
* Marketing

and Supplier Management is currently elsewhere.

The ECF itself makes an important statement:

a single party can simultaneously be customer, supplier and partner.

That creates a conceptual tension.

The current catalog is organized around roles whereas the ECF is organized around party/relationship as the underlying semantic subject.

Customer Management is explicitly about the customer relationship. 

Partner Management is about peer relationships. 

Supplier Management is about those who supply the enterprise. 

That is useful operationally, but I think OpenDEAM needs to distinguish:

Party & Relationship capability

from

role-specific relationship capabilities.

I would therefore investigate:

Relationship Management

The ability to establish, govern, develop, and terminate relationships with external parties across their lifecycle.

Then:

* Customer Management → specialization
* Supplier Management → specialization
* Partner Management → specialization
* Regulator Relationship Management → specialization
* Community/Stakeholder Relationship Management → specialization

This would align the catalog much more tightly with the ECF’s own assertion that Party & Relationship is MECE-complete for the external environment. 

I would not necessarily canonize this immediately. It deserves a boundary/evidence investigation because it could also become an abstract grouping parent rather than a first-order capability.

Priority: 1-2.

⸻

7. Gap #4: Knowledge / Organizational Learning

There is a potentially important gap between:

Information Management

and

Analytics & Intelligence.

Information Management currently governs, structures and stewards information across its lifecycle. 

Analytics & Intelligence derives insight from that information. 

But neither explicitly captures the enterprise’s ability to:

* retain organizational knowledge
* learn from experience
* institutionalize lessons
* transfer knowledge
* build organizational memory
* convert experience into improved capability

This becomes especially important in an enterprise containing human + AI agents.

I’d investigate:

Knowledge Management

The ability to capture, structure, preserve, share, and apply organizational knowledge and learning.

Potential placement:

Agency & Organization × Improve

with secondary participation in:

Enablement & Operations × Operate

But I would be cautious.

The ECF domain grounding says Agency & Organization includes development, performance, collaboration and organizational knowledge archiving. 

Information Management already owns information.

Therefore this could easily become an unnecessary abstraction unless the evidence demonstrates that Knowledge is a distinct durable business object, rather than a semantic property of Information or Agency.

So:

Investigate: do not automatically add.

Priority: 2-3.

⸻

8. The bigger issue: ECF coordinates

This is where I think the current catalog needs more serious correction.

A. Strategy is in the wrong domain

The current record says:

Strategy → Governance & Existence × Conceive. 

But the ECF itself explicitly says:

Governance & Existence authorizes but does not direct; Strategy & Direction directs within the authorized frame.

And Strategy & Direction explicitly includes:

* purpose and ambition
* environmental sensing
* strategic choices
* objectives and targets
* strategic planning
* strategic adaptation. 

Therefore:

Current

Strategy → Governance & Existence × Conceive

Recommended

Strategy → Strategy & Direction × Conceive

with perhaps:

Strategy & Direction × Improve

as secondary.

This isn’t a minor coordinate preference.

It creates a direct contradiction between the capability catalog and the ECF’s domain boundary.

⸻

9. Strategic Planning has the same problem

Current:

Strategic Planning → Governance & Existence × Conceive. 

But the ECF explicitly lists Strategic Planning inside Strategy & Direction. 

Therefore this should almost certainly be:

Strategy & Direction × Conceive

possibly with:

Strategy & Direction × Improve

depending on the lifecycle semantics.

This is probably the highest-confidence coordinate correction in the catalog.

⸻

10. Asset Management is probably misplaced

Current:

Asset Management → Strategy & Direction × Build, with Operate and Retire secondaries. 

But the ECF grounding says something very important:

physical resources moved to Enablement & Operations as enablers.

And Enablement & Operations explicitly includes:

physical and virtual infrastructure

and states that physical resources previously associated with Supply & Resources now live there as enablers. 

Therefore the current placement produces a semantic tension.

Asset Management is not primarily about direction.

It is about the lifecycle stewardship of the enterprise’s physical/non-financial assets.

I’d recommend investigating:

Asset Management → Enablement & Operations × Build

with:

* Operate
* Improve
* Retire

as legitimate secondaries.

This would be much more consistent with the ECF’s explicit treatment of physical resources.

⸻

11. Facility Management is likewise questionable

Current:

Facility Management → Strategy & Direction × Activate, then Operate. 

But the capability itself is:

the ability to provide and operate the enterprise’s physical places. 

That sounds almost definitionally like Enablement & Operations.

The ECF says physical infrastructure is part of Enablement & Operations. 

I’d therefore strongly consider:

Facility Management → Enablement & Operations × Activate

with:

Operate

secondary.

This is another high-confidence correction.

⸻

12. Technology Management deserves special treatment

This one is more nuanced.

The catalog deliberately moved Technology Management to:

Strategy & Direction × Build → Operate → Improve

and explains that technology is being treated as an estate rather than simply an operational enabler. 

I understand the reasoning.

However, the ECF explicitly states:

Technology, platforms, and physical infrastructure are positioned as enablers of execution.

So the framework now has a potentially problematic distinction:

Technology as an estate

→ Strategy & Direction

Technology as an enabler

→ Enablement & Operations

That distinction is intellectually defensible, but it risks creating two semantic homes for the same capability object.

I would not immediately move Technology Management.

Instead, I recommend a formal boundary decision:

Technology Management

should mean:

stewardship of the enterprise technology estate

while

Technology Enablement

is a sub-concern of Enablement & Operations:

use of technology to enable execution.

That distinction should be made explicit in the capability catalog and ECF mapping rules.

Otherwise future catalog contributors will continually debate whether cloud, platforms, applications, networks, AI agents, etc. belong in Strategy or Enablement.

⸻

13. Supplier Management and Procurement need reconsideration

Current:

Supplier Management → Strategy & Direction × Build. 

Sourcing & Procurement → Strategy & Direction × Build. 

This is probably the least convincing part of the current coordinate set.

Supplier Management is fundamentally a relationship capability.

The ECF explicitly says suppliers are external parties belonging to Party & Relationship. 

So I would strongly favor:

Supplier Management

Party & Relationship × Conceive / Operate

rather than Strategy & Direction × Build.

For:

Sourcing & Procurement

I would consider:

Enablement & Operations × Build

with perhaps:

Strategy & Direction × Conceive/Design

as a secondary context for strategic sourcing.

That gives a much cleaner distinction:

Strategy
→ decide sourcing posture

Party
→ manage supplier relationship

Enablement
→ execute acquisition

Finance
→ account for monetary exchange

That is precisely the kind of cross-domain semantic separation the ECF is designed to provide.

⸻

14. The ECF coordinate philosophy itself is good: but needs one refinement

The repository currently uses:

one primary coordinate + honest secondary coordinates

and defines primary as the earliest initiation point. 

I like the principle.

But I think “earliest initiation” is becoming too dominant as a coordinate selection heuristic.

For example:

* Supplier Management → Build because the supply base is “built”
* Strategy → Conceive because strategy exists when enterprise is conceived
* Risk → Conceive because risk posture is constituted
* Facility → Activate because facility becomes usable
* Technology → Build because technology estate is acquired

This produces coordinates that can be technically defensible while still being semantically unintuitive.

I’d introduce a stronger rule:

Primary coordinate should represent the capability’s semantic center of gravity, not merely its earliest lifecycle initiation.

Then use lifecycle participation as secondary coordinates.

That would produce a more useful capability heatmap.

For example:

Operations

Enablement & Operations × Operate

is obvious and excellent. 

Customer Management

Party & Relationship × Operate

is also intuitive. 

But:

Strategy

Governance & Existence × Conceive

is technically motivated but semantically misleading.

This distinction should become an explicit ECF mapping principle.

⸻

15. A particularly important observation: the catalog is too concentrated around “Governance & Existence”

The current model has a large collection of capabilities anchored there:

* Strategy
* Strategic Planning
* Enterprise Governance
* Risk
* Legal
* Regulation
* Security
* Continuity
* Change

Some of these unquestionably belong there.

But Strategy and Strategic Planning clearly do not.

Once those are moved, the domain becomes more coherent:

Governance & Existence

“Is the enterprise legitimate, controlled, accountable and able to persist?”

→ Governance
→ Risk
→ Regulation
→ Legal
→ Security
→ Continuity

Strategy & Direction

“Where is the enterprise going and what does it prioritize?”

→ Strategy
→ Strategic Planning
→ Performance Management
→ perhaps strategic resource choices

That is much cleaner.

⸻

16. The catalog also needs a stronger “closed-loop enterprise” capability structure

I would conceptualize the foundational capabilities as a set of interacting loops:

Direction loop

Strategy → Strategic Planning → Performance Management → Analytics & Intelligence → Strategy Adaptation

Value loop

Marketing → Offering Management → Customer Management → Operations

Resource loop

Workforce Planning → Workforce Management

Asset Management → Facility/Technology Management

Financial Stewardship → Financial Resource Management

Enterprise protection loop

Risk → Security → Continuity → Change

External ecosystem loop

Party/Relationship → Customer / Supplier / Partner specializations

This gives the catalog architectural coherence rather than merely a list of capabilities.

⸻

17. My recommended foundational additions

I would therefore create the following investigation queue:

Priority	Candidate	Recommendation
P1	Organizational Design	Strong candidate for canonical capability
P1	Enterprise Performance Management	Strong candidate for canonical capability
P1	Relationship Management	Investigate generic parent vs role-specific capabilities
P2	Knowledge Management	Evidence investigation required
P2	Service Management	Investigate whether Operations already absorbs it
P2	Quality Management	Investigate whether Operations/Assurance already absorbs it
P3	Stakeholder Management	Likely specialization of Relationship Management
P3	Enterprise Architecture Management	Probably specialization/model construct rather than first-order capability

I would not add all of these.

The target should probably remain somewhere around 28-32 first-order capabilities, not 50-100.

⸻

18. Recommended ECF corrections

My current recommendation would be:

Capability	Current	Recommended
Strategy	Governance × Conceive	Strategy & Direction × Conceive
Strategic Planning	Governance × Conceive	Strategy & Direction × Conceive
Supplier Management	Strategy × Build	Party & Relationship × Conceive/Operate
Sourcing & Procurement	Strategy × Build	Enablement & Operations × Build
Asset Management	Strategy × Build	Enablement & Operations × Build
Facility Management	Strategy × Activate	Enablement & Operations × Activate
Technology Management	Strategy × Build	Keep provisionally; formalize boundary
Security Management	Governance × Design	Keep; possibly E&O secondary
Continuity Management	Governance × Design	Keep
Risk Management	Governance × Conceive	Keep
Operations	E&O × Operate	Keep
Information Management	E&O × Operate	Keep provisionally
Analytics & Intelligence	E&O × Operate	Keep provisionally

The strongest corrections are Strategy, Strategic Planning, Asset Management, Facility Management, Supplier Management and Sourcing & Procurement.

⸻

19. One architectural issue I would fix immediately

There is also some repository/documentation drift.

The README says the catalog is now populated with 26 canonical capabilities, but the Entity Definition table still says:

Catalog Status: planned

even though the repository explicitly says the catalog is populated and canonical. 

Likewise, the repository is described against OpenDEAM v0.2.1, while the catalog pins the metamodel at 1.0.0 and the ECF conformance contract at 1.0.0. 

That should be cleaned up before further capability expansion because otherwise consumers won’t know which version is normative.

⸻

20. My overall verdict

The capability methodology is good.

I would not redesign the methodology.

The evidence ladder, first-order concept, specialization boundary, ability test, and “capability before coordinate” principle are strong. 

The capability set is approximately 80-85% of the way to a strong enterprise-general foundation.

The most important missing concepts are:

Organizational Design
Enterprise Performance Management
Generic Relationship Management

with Knowledge Management deserving investigation.

But the bigger immediate issue is coordinate integrity.

The ECF itself says Strategy & Direction owns strategic planning and deliberate trajectory, while Enablement & Operations owns physical/virtual enabling mechanisms. 

Therefore the current assignments of:

Strategy → Governance

and

Asset / Facility / potentially Technology → Strategy

deserve formal reconsideration.

The catalog should not merely be ECF-conformant syntactically; its mappings should be ECF-semantically explanatory.

That distinction is important if OpenDEAM is ultimately going to use the ECF as an actual architectural coordinate system rather than simply as metadata.

My recommended next step

I would not start adding new capabilities yet.

I would first run a focused “Business Capability ↔ ECF Semantic Alignment” change cycle:

BC-ECF-01: Revalidate all 26 primary coordinates against the normative ECF domain boundaries, specifically applying a new rule:

Primary ECF coordinate represents the capability’s semantic center of gravity; secondary coordinates represent legitimate lifecycle participation. Earliest initiation is evidence for placement, not by itself the placement rule.

Then correct the six high-confidence mappings above.

After that, conduct the evidence investigation for the three proposed foundational gaps: Organizational Design, Enterprise Performance Management, and Relationship Management: before admitting anything else.

That would make the catalog considerably more coherent and, importantly, would make the ECF × Business Capability relationship itself a much stronger part of OpenDEAM’s architecture rather than just a classification overlay.  
---

## Triage summary (added by the catalog owner, 2026-09-10)

Each item from BC-SR-A001 §17, §18, §19 is classified as follows. See CR-DEA-BC-12 §"Scope of this CR" for the carrier-side action plan.

| Review section | Item | Class | Carrier action |
|---|---|---|---|
| §4 | Gap #1: Organizational Design | P1 (reviewer) | Open investigation track A (evidence-led) |
| §5 | Gap #2: Enterprise Performance Management | P1 (reviewer) | Open investigation track B (evidence-led) |
| §6 | Gap #3: Relationship Management (generic parent) | P1-P2 (reviewer) | Open investigation track C (boundary-led) |
| §7 | Gap #4: Knowledge Management | P2 (reviewer) | Defer to backlog pending evidence |
| §8.A | Strategy coordinate (Governance→Strategy & Direction) | High confidence | Land in CR-DEA-BC-12 §"ECF re-mapping" |
| §9 | Strategic Planning coordinate (same move) | High confidence | Land in CR-DEA-BC-12 §"ECF re-mapping" |
| §10 | Asset Management coordinate (Strategy→Enablement & Operations) | High confidence | Land in CR-DEA-BC-12 §"ECF re-mapping" |
| §11 | Facility Management coordinate (Strategy→Enablement & Operations) | High confidence | Land in CR-DEA-BC-12 §"ECF re-mapping" |
| §12 | Technology Management coordinate (boundary decision) | Medium confidence | Open investigation; do NOT move in this CR |
| §13 | Supplier Management + Sourcing & Procurement (Strategy→Party/Enablement) | High confidence | Land in CR-DEA-BC-12 §"ECF re-mapping" |
| §14 | ECF mapping rule refinement ("semantic center of gravity" vs "earliest initiation") | Method change | Open as follow-on method-CR; not in BC-12 |
| §15 | Concentration around Governance & Existence (after §8/§9 moves) | Architectural observation | Implicitly addressed by the §8/§9 moves |
| §16 | Closed-loop capability structure | Architectural proposal | Informs investigation track B (Performance Management) |
| §17 (rest) | Service Management, Quality Management, Stakeholder Management, EAM | P2-P3 | Defer to backlog; revisit after the three investigations close |
| §19 | README status field "planned" → "populated" | Doc drift | Land in CR-DEA-BC-12 §"Repo-doc drift" |
| §19 | OpenDEAM version pin (repo described against v0.2.1, metamodel pinned to 1.0.0) | Doc drift | Land in CR-DEA-BC-12 §"Repo-doc drift" |

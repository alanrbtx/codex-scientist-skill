# Submission Audit

Use this reference when creating, updating, packaging, or independently checking a paper artifact.

Scale the audit to the requested deliverable. A local correction needs a build when applicable and
inspection of affected content and pages; include any pagination or reference changes it causes.
Use the full checklist for submission readiness, a release package, or a broad layout change.
Do not rebuild archives or repeat passed checks unless the artifact changed or a finding warrants it.

## Contents

- [Identify the canonical variant](#identify-the-canonical-variant)
- [Build from a clean environment](#build-from-a-clean-environment)
- [Audit the PDF itself](#audit-the-pdf-itself)
- [Audit anonymity and identity](#audit-anonymity-and-identity)
- [Audit the source archive](#audit-the-source-archive)
- [Verify propagation and destination state](#verify-propagation-and-destination-state)
- [Recheck venue-specific rules](#recheck-venue-specific-rules)
- [Suggested lightweight checks](#suggested-lightweight-checks)
- [Handoff checklist](#handoff-checklist)

## Identify the canonical variant

Keep these variants separate:

- anonymous conference submission;
- author-identified preprint;
- camera-ready or accepted manuscript;
- public reproducibility package;
- internal development draft.

Resolve the exact target from the request and existing context before editing or copying. Ask only
if a material ambiguity remains. Never update a submitted or public artifact when the user
authorized only a new working version.

Record the canonical source directory, PDF name, archive name, page limit, anonymity state, and
required acknowledgment or author block. Treat every copy as a distinct artifact until byte or hash
identity is verified.

## Build from a clean environment

Use the workspace's authorized execution environment and obey its local/remote restrictions.
Compile from a clean extraction or clean auxiliary state so stale files cannot mask missing
dependencies.

Check the full build transcript for:

- errors and undefined control sequences;
- missing figures, bibliography, fonts, or style files;
- unresolved citations and references;
- multiply defined labels;
- overfull boxes and clipped content;
- nonportable shell escape or absolute paths.

A successful exit code is necessary but not sufficient.

## Audit the PDF itself

Verify:

- page size and page count;
- required margins on every page based on visible ink, not only text boxes;
- no clipped equations, captions, tables, headers, or figures;
- embedded fonts and absence of prohibited bitmap or Type 3 fonts;
- readable figures at print scale;
- selectable text and sensible extraction order;
- correct metadata, title, authors, and anonymity;
- consistent references, numbering, and hyperlinks;
- no comments, hidden annotations, tracked changes, or accidental file paths;
- no bad characters introduced by copy/paste into submission fields.

Render every page to an image and inspect it visually. Automated margin overlays can include the
page's background or annotations; confirm the actual offending ink before changing layout.

For margin repairs, prefer local changes to the offending figure, table, equation, or caption.
Avoid global font or margin reductions that weaken the whole document or violate the template.

## Audit anonymity and identity

For anonymous submission, search extracted text and PDF metadata for:

- author names and affiliations;
- email addresses and personal URLs;
- acknowledgments, grants, institutions, and laboratories;
- repository or dataset links that reveal identity;
- embedded document author and creator fields.

For an author-identified version, verify that the title page, author order, affiliations,
acknowledgment wording, and contact information are present and exact. Do not accidentally ship the
anonymous PDF inside an author archive or vice versa.

## Audit the source archive

Include only files needed for a clean build:

- manuscript source;
- bibliography and style/class files allowed by the venue;
- figures and tables;
- small generated data files required by the source;
- explicit build instructions only when permitted.

Exclude auxiliary files, caches, temporary renders, editor state, system metadata, credentials,
logs with private paths, and unrelated drafts.

Then:

1. list the archive contents;
2. extract it into a fresh temporary directory;
3. rebuild using only the archive;
4. compare page count and extracted text with the canonical PDF;
5. visually sample or compare every rendered page;
6. compute and record checksums for the PDF and archive.

Do not call an archive updated merely because a new file was created. Verify that it contains the
intended source and reproduces the intended PDF.

## Verify propagation and destination state

For each delivery step, check the destination:

- local canonical PDF equals the newly built PDF;
- archive contains the canonical source and figures;
- uploaded submission preview preserves layout and characters;
- public repository or release points to the intended commit and artifacts;
- checksums and filenames match the handoff note.

Do not infer success from a copy, upload, push, or API response alone. Re-open, re-download, query,
or hash the destination where possible.

## Recheck venue-specific rules

Rules change. Verify current official requirements for:

- page and file-size limits;
- paper size and margins;
- font and PDF version constraints;
- anonymity and supplementary-material policy;
- acknowledgments and generative-AI disclosure;
- hyperlinks, videos, appendices, and external repositories;
- keyword taxonomy and submission-field character restrictions.

Use the official venue source rather than a remembered prior-year rule. When the submission system
offers a controlled vocabulary or preview, treat it as the final source of truth.

## Suggested lightweight checks

Use equivalent tools available in the authorized environment:

- PDF metadata and geometry inspection;
- font inventory;
- text extraction and targeted search;
- page rendering;
- bounding-box or ink-bound analysis;
- archive listing and clean extraction;
- checksums and byte comparison.

Tool output does not replace visual review. If the workspace forbids local project execution,
perform compilation and project scripts remotely while keeping local activity to file inspection,
editing, and permitted transfer commands.

## Handoff checklist

Report:

- exact canonical PDF and source/archive paths;
- variant and anonymity state;
- page count and format;
- build and visual-audit result;
- font, metadata, reference, and margin result;
- archive clean-rebuild result;
- checksums;
- any unresolved warning that could affect submission.

Use “verified” only for checks actually performed.

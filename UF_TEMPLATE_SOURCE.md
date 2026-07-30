# UF template source and proposal adaptation

The project uses the University of Florida Thesis & Dissertation Support
Center's official LaTeX template downloaded on July 30, 2026:

- Template page: https://it.ufl.edu/helpdesk/graduate-resources/ms-word--latex-templates/
- Archive: `Dissertation___Thesis_Example_File.zip`
- Official `ufdissertation.cls` SHA-256:
  `7e004fcce7c491749c4ef3f3348c111967aa68ebef97b932ca4667231716cf56`

The official class is retained as the formatting base. A local `proposalMode`
extension changes only the front-matter workflow:

- replaces the dissertation title page with a Ph.D. proposal title page;
- omits copyright, dedication, acknowledgements, and biographical sketch;
- labels the abstract as `PROPOSAL ABSTRACT`;
- retains UF margins, typography, spacing, headings, page numbers, table of
  contents, lists of tables and figures, captions, and reference formatting.

The project is configured for LuaLaTeX and TeX Live 2025 through `latexmkrc`,
consistent with UF's current compiler guidance. The source supplies PDF 2.0
language metadata and alternative text for every included figure. Full tagged
PDF output is not enabled in this migration: the official class's custom
`titlesec`/`titletoc` front matter produces an invalid tag stack under the
available TeX Live 2025 tagging code. Accessibility conformance must therefore
be validated separately before a final dissertation deposit.

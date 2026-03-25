# Project Goal
- Create a YAML based test framework to feed and verify test data into Tiny-Tapeout projects

# Planning & Progress tracking
- Keep an up to date file "ROADMAP.md" with the next 5 steps and all past steps having checkboxes.
  - If necessary split steps into 2-5 additional substeps if the complexity of the task is high.

## Solving
- For each problem first draft three different solutions and then choose the best one.
   - Insert each problem with timestamp (heading) and each variant solutions (sub-heading)
     with one sentence of the reasoning at the top of "DECISION.md".
- Before publishing a pull request to GitHub, pull main from the  origin and resolve all merge conflicts.

## Finishing
- Check the boxes of solved tasks in the ROADMAP.md
- Be sure all /src/data have generated /waveforms
- Ensure that in `src/docs/TTIHP26A_PROJECTS.md`, the "Summary" column links to the corresponding `src/docs/tt{ID}.md` file if it exists.

# Project structure
- ROADMAP.md - Planned & finished tasks of the product
- README.md - Overview of the product
- HOWTO.md - Usage instruction of the product
- / - Keep only GEMINI.md, HOWTO.md, README.md, DECISION.md, DISCARDED.md, ROADMAP.md, requirements.txt and .gitignore in the root directory
- /specifications - Download and store original specification, add ".original." in the name before the extension
- /specifications - NEVER change ".original." files
- /specifications - Convert "non .md" files for caching and readability purpose to Markdown
- /src/scripts - Tools to verify the data and generate the waveforms/documents
- /src/schema  - The schema of the test data files
- /src/data    - Instances of the test schema
- /waveforms      - Generate timing diagramm files from every data file
- /src/docs    - Generate documentation for each test set
- /test   - Test cases for all tasks, used to verify everything in src
- /.github/workflows - For every push on every branch, re-generate all deliverables from the sources

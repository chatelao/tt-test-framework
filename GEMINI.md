# Project Goal
- Create a YAML based test framework to feed and verify test data into Tiny-Tapeout projects
- 

# Planning & Progress tracking
- Keep an up to date file "ROADMAP.md" with the next 5 steps and all past steps having checkboxes.
  - Chapter Planned: Human added tasks, don't modify their content only execute them if next/ready and move if done.
  - Chapter Proposed: Before sending the PR add here things you would like to add and/or improve.
  - Chapter Finished: Before sending the PR move and insert finished task at first place into the chapter.

## Planning
- If necessary split steps into 2-5 additional substeps if the complexity of the task is high.

## Solving
- For each problem  first draft three different solutions and then choose the best one.
- Track the discarded solutions to discard as 1-2 sentences with timestamp in "DISCARDED.md".
- Before publishing a pull request to GitHub, pull main from the  origin and resolve all merge conflicts.

## Finishing
- Check the boxes of solved tasks in the ROADMAP.md an

# Project structure
- ROADMAP.md - Planned & finished tasks of the product
- README.md - Overview of the product
- HOWTO.md - Usage instruction of the product
- / - Keep only GEMINI.md, HOWTO.md, README.md and ROADMAP.md in the root directory
- /specifications - Download and store original specification, add ".original." in the name before the extension
- /specifications - NEVER change ".original." files
- /specifications - Convert "non .md" files for caching and readability purpose to Markdown
- /design - Keep a human well readable design specification, write them before implementing
- /design - Keep a human well readable design specification, write them before implementing
- /src/schema  - The schema of the test data files
- /src/data    - Instances of the test schema
- /src/scripts - Tools to verify the data and generate the images/documents
- /src/docs    - The documentation generated based on the data
- /src/images  - Images generated from the data
- /test   - Test cases for all tasks, used to verify everything in src
- /.github/workflows - For every push on every branch, re-generate all deliverables from the sources

# Design Documentation Rules
- For each standard cell, maintain a Markdown file in `/design` with layer-by-layer ASCII art.
- The ASCII art should follow the character mapping defined in `specifications/MODELING_GUIDELINES.md`.

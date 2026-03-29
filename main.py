import streamlit as st
from datetime import date

st.set_page_config(page_title="Thesis Progress Dashboard", layout="wide")

# ---------- Sidebar ----------
st.sidebar.title("Thesis Progress")
st.sidebar.markdown("LOTS + Platform")
section = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Project Context",
        "What I Have Done",
        "Payload Evolution",
        "LASSO Implementation Steps",
        "Current Understanding",
        "Problems / Open Questions",
        "Next Steps",
        "Meeting Notes",
    ],
)

# ---------- Reusable data ----------
project_title = "Thesis / Research Progress Report"
today = date.today().strftime("%d %B %Y")

completed_tasks = [
    "Read and understood the LOTS paper and its main methodology.",
    "Studied and understood the mock / prototype implementation of the LOTS codebase.",
    "Had a meeting with Mattia on 5 March to discuss the project and the current platform.",
    "Was added as a contributor to the Fashion Design AI GitHub repository.",
    "Successfully ran the project code locally and analyzed how the pipeline works.",
    "Reviewed the implementation step-by-step to understand the components and workflow of the system.",
    "Implemented the LASSO tool on both frontend and backend.",
    "Connected LOTS to the platform so the platform can use LASSO-based inputs.",
    "Added sketch drawing interaction using mouse / trackpad.",
    "Added the possibility to upload a sketch and then use LASSO regions on top of it.",
    "Updated the payload structure so the platform can send LASSO information to the generation pipeline.",
    "Changed the logic for non-selected regions: areas outside the selected LASSO region now use the layer description.",
    "Supported local region descriptions for each LASSO and also global description handling.",
    "Tested previously successful sketches shared by Davide Talon on my own system and verified that the outputs were also strong locally.",
    "Validated that uploaded sketches + LASSO regions + descriptions can now be prepared correctly before generation.",
    "Planned the Streamlit update to clearly show the old payload vs the new payload and to support a more tree-structured explanation of the data flow.",
    "Started preparing a more flexible drawing workflow that can later support pen-based sketching on iPad-like devices."
]

open_questions = [
    "How exactly was the dataset prepared for LOTS?",
    "How should the final evaluation compare different interaction modalities in the future user study?",
    "What is the best final UI form for sketching: browser canvas, uploaded sketch, or tablet-based drawing?"
]

next_steps = [
   "Improve UI design of front-end part",
    "Test and Debug",
    "Refactor codes"
]

lasso_steps = [
    {
        "title": "Added LASSO region-selection interface",
        "desc": "Implemented an interactive LASSO selection tool in the frontend so the user can draw free-form regions on the image/canvas. The tool captures the polygon coordinates of the selected region instead of relying on rectangular bounding boxes."
    },
    {
        "title": "Extracted polygon coordinates",
        "desc": "When the user completes a LASSO selection, the system records the ordered list of (x, y) coordinates representing the polygon. These coordinates define the exact region selected by the user."
    },
    {
        "title": "Converted polygon to binary mask",
        "desc": "The polygon coordinates are converted into a binary mask with the same resolution as the image. Pixels inside the polygon are set to 1 and pixels outside are set to 0. This mask becomes the region-of-interest representation used by the pipeline."
    },
    {
        "title": "Attached mask to the payload structure",
        "desc": "The generated mask is stored as part of the input object sent to the backend. This allows the platform to send precise LASSO-defined regions to LOTS instead of only sending a coarse global input."
    },
    {
        "title": "Integrated mask into the LOTS processing pipeline",
        "desc": "The mask is forwarded through the generation pipeline so downstream modules can use it to restrict processing to the selected region. This enables localized editing or generation instead of modifying the whole image."
    },
    {
        "title": "Supported multiple LASSO regions",
        "desc": "The system allows multiple LASSO selections. Each region is stored separately with its own geometry and description, enabling fine-grained control over multiple parts of the design."
    },
    {
        "title": "Defined fallback behavior for non-selected regions",
        "desc": "A key design decision was added after team discussion: regions that are not selected by LASSO should not be left undefined. Instead, non-selected areas now take their conditioning from the corresponding layer description."
    },
    {
        "title": "Validated the workflow with real sketch examples",
        "desc": "Tested the LASSO-enhanced workflow using sketches that had previously produced good results in earlier platform testing. The same sketches were tested locally and the results were also strong, confirming that the integration logic is functioning correctly."
    }
]

# ---------- Header ----------
st.title(project_title)
st.caption(f"Updated for professor and project team • 30 March 2026")
st.divider()

# ---------- Sections ----------
if section == "Overview":
    st.header("Overview")
    c1, c2 = st.columns([2, 1])

    with c1:
        st.markdown(
            """
            This dashboard summarizes the work completed so far for my thesis/project.
            The goal is to clearly communicate:

            - what the project is about,
            - what I have already understood,
            - what I have implemented,
            - what changed in the platform and payload design,
            - what remains unclear,
            - and what I plan to do next.
            """
        )

    with c2:
        st.info(
            """
            **Main objective**

            Extend the existing platform by integrating LOTS with a LASSO-based interaction workflow,
            so that users can define local regions, provide structured descriptions, and generate outputs
            with more precise control. Later, this will support evaluation and a possible user study.
            """
        )

elif section == "Project Context":
    st.header("Project Context")
    st.markdown(
        """
        The project started from an existing platform/tool shared by the team.
        My current focus is not only understanding the system, but also extending it in a technically meaningful way.

        At this stage, the project involves:
        - an existing AI-based fashion/design-related workflow,
        - the LOTS generation pipeline,
        - integration of a LASSO-based interaction method,
        - a more flexible payload design for region-level control,
        - and later a possible user study to compare interaction modalities.
        """
    )

    st.subheader("People involved")
    st.write("- Professor Marco Cristani")
    st.write("- Mattia Mondo")
    st.write("- Yiming Wang")
    st.write("- Davide Talon")
    st.write("- Loris Bazzani")

elif section == "What I Have Done":
    st.header("What I Have Done Until Now")

    st.markdown(
        """
        This section presents my progress in a structured, week-by-week format,
        showing how the work evolved from understanding the system to actively extending it.
        """
    )

    # -------- Phase 1 --------
    st.subheader("Phase 1 — Before First Meeting (Understanding Stage)")

    phase1 = [
        "Read and understood the LOTS paper and its main methodology.",
        "Studied and understood the mock / prototype implementation of the LOTS codebase.",
        "Successfully ran the project code locally and analyzed how the pipeline works.",
        "Reviewed the implementation step-by-step to understand the components and workflow of the system.",
        "Had a meeting with Mattia on 5 March to discuss the project and the current platform.",
        "Was added as a contributor to the Fashion Design AI GitHub repository.",
        "Implemented the first version of LASSO tool on frontend."
    ]

    for i, task in enumerate(phase1, start=1):
        st.markdown(f"**{i}.** {task}")

    st.markdown("### Demo Video — Phase 1")
    st.video("report/videos/phase1_demo.mp4")
    st.caption(
        "Initial stage of the project: early system exploration, local execution, and first frontend LASSO implementation."
    )

    # -------- Phase 2 --------
    st.subheader("Phase 2 — First Week (Integration & Core Implementation)")

    phase2 = [
        "Implemented the LASSO tool on backend.",
        "Connected LOTS to the platform so the platform can send generation requests to the real model instead of the mock implementation.",
        "Added sketch drawing interaction using mouse / trackpad.",
        "Updated the payload structure so the platform can send LASSO information to the generation pipeline.",
        "Changed the logic for non-selected regions: areas outside the selected LASSO region now use the layer description.",
        "Supported local region descriptions for each LASSO and also global description handling.",
        "Changed the payload structure to handle non-selected regions after using the LASSO tool."
    ]

    for i, task in enumerate(phase2, start=1):
        st.markdown(f"**{i}.** {task}")

    # -------- Phase 3 --------
    st.subheader("Phase 3 — Second Week (Refinement, Validation & Design Decisions)")

    phase3 = [
        "Added the possibility to upload a sketch and then use LASSO regions on top of it.",
        "Tested previously successful sketches shared by Davide Talon on my own system and verified that the outputs were also strong locally.",
        "Validated that uploaded sketches + LASSO regions + descriptions can now be prepared correctly before generation.",
        "Set up the LOTS model on the University of Verona server to enable faster GPU-based testing and overcome local hardware limitations.",
        "Extended the LASSO tool to a more advanced version (LASSO v2) by adding add/remove region functionality, making the interaction more flexible and user-friendly.",
        "Performed debugging and validation of the full pipeline, including sketch processing, mask generation, and payload preparation.",
        "Designed and implemented a structured format for storing sketches, LASSO regions, masks, and associated descriptions, enabling consistent data handling across the pipeline."
    ]

    for i, task in enumerate(phase3, start=1):
        st.markdown(f"**{i}.** {task}")

    st.markdown("### Demo Video — Phase 3")
    st.video("report/videos/phase3_demo.mp4")
    st.caption(
        "Refined workflow: sketch upload, LASSO v2 interaction, add/remove region support, and structured preparation for generation."
    )

elif section == "Payload Evolution":
    st.header("Payload Evolution")

    st.markdown(
        """
        One of the most important technical updates is the change in the payload structure.
        The old structure was more limited and did not properly represent LASSO-based local control.
        The new structure is more expressive and better aligned with the platform's interaction logic.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Previous payload idea")
        st.code(
            """{
  "sketch": "...",
  "description": "...",
  "layers": [
    {
      "layer_id": 0,
      "description": "..."
    }
  ]
}""",
            language="json",
        )

        st.caption(
            "This structure is simple, but it does not clearly represent region-level selection or local descriptions."
        )

    with col2:
        st.subheader("Updated payload idea")
        st.code(
            """{
  "global_description": "overall garment / scene description",
  "sketch": "...",
  "layers": [
    {
      "layer_id": 0,
      "layer_description": "description for non-selected area of this layer",
      "lasso_regions": [
        {
          "region_id": 0,
          "polygon": [[x1, y1], [x2, y2], [x3, y3]],
          "mask": "binary mask",
          "description": "local description for selected region"
        }
      ]
    }
  ]
}""",
            language="json",
        )

        st.caption(
            "This structure supports global conditioning, layer-level fallback, and local region control."
        )

    st.subheader("Key design logic")
    st.markdown(
        """
        - **Selected LASSO regions** use their own local descriptions.
        - **Non-selected regions** use the corresponding **layer description**.
        - A **global description** can still be used as overall context.
        """
    )

    st.subheader("Tree-structured view of the new payload")
    st.code(
        """Payload
├── global_description
├── sketch
└── layers
    ├── layer_1
    │   ├── layer_description
    │   └── lasso_regions
    │       ├── lasso_region_1
    │       │   ├── polygon
    │       │   ├── mask
    │       │   └── description
    │       └── lasso_region_2
    │           ├── polygon
    │           ├── mask
    │           └── description
    └── layer_2
        ├── layer_description
        └── lasso_regions
            └── ...""",
        language="text",
    )

    st.subheader("Why the new payload is better")
    st.markdown(
        """
        The new payload is better because it matches the real interaction logic of the platform.
        It makes explicit:
        - what the user selected,
        - what the user did not select,
        - which text belongs to a region,
        - and which text belongs to the whole layer or the whole sketch.
        """
    )

elif section == "LASSO Implementation Steps":
    st.header("Technical Explanation of the LASSO Tool")
    st.markdown(
        """
        This section focuses on the technical implementation of the LASSO tool:
        how the user interaction is represented, how the selected region is transformed into a usable format,
        and how that information is passed through the system pipeline.
        """
    )

    for i, step in enumerate(lasso_steps, start=1):
        st.markdown(f"### Step {i}. {step['title']}")
        st.write(step["desc"])

    st.subheader("LASSO Data Flow")
    st.code(
        """User draws or uploads sketch
        ↓
User selects free-form region with LASSO
        ↓
Polygon vertices are collected
        ↓
Polygon is rasterized into a binary mask
        ↓
Mask + local description are attached to the layer object
        ↓
Non-selected region keeps layer description
        ↓
Structured payload is sent to backend / LOTS pipeline
        ↓
Generation uses local + layer + global conditioning""",
        language="text",
    )

    st.subheader("Input Structure Example")
    st.code(
        """{
  "global_description": "overall design description",
  "layers": [
    {
      "layer_id": 0,
      "layer_description": "used for non-selected area",
      "lasso_regions": [
        {
          "polygon": [[x1, y1], [x2, y2], [x3, y3], ...],
          "mask": "binary mask with same height/width as the image",
          "description": "local description for the selected area"
        }
      ]
    }
  ]
}""",
        language="json",
    )

    st.subheader("Mask Generation Logic")
    st.code(
        """1. Receive ordered polygon points from the LASSO tool
2. Create an empty mask with image resolution H x W
3. Fill the polygon interior with value 1
4. Keep all pixels outside the polygon as 0
5. Attach the mask to the corresponding LASSO region object
6. Preserve layer description for non-selected regions
7. Pass the final structured payload to downstream modules""",
        language="text",
    )

    st.subheader("Why this matters technically")
    st.markdown(
        """
        The key technical contribution of the LASSO tool is that it replaces coarse image interaction with
        **pixel-level region selection**. Instead of applying processing to a whole layer or broad area,
        the system can now receive a precise region-of-interest mask derived directly from the user's free-form input.

        Combined with the updated payload, this makes localized conditioning possible in a much cleaner and more explainable way.
        """
    )

elif section == "Current Understanding":
    st.header("Current Understanding")

    st.success("What I understand well")
    st.markdown(
        """
        - The LOTS architecture and its overall generation workflow.
        - How the frontend, backend, and model pipeline connect to support end-to-end generation.
        - How LASSO-based interaction can be integrated into the platform as a region-level control mechanism.
        - How polygon-based user selections are transformed into binary masks for downstream processing.
        - How the payload needed to evolve to support hierarchical conditioning through global, layer-level, and region-level descriptions.
        - Why non-selected regions require explicit fallback behavior and how layer descriptions solve that problem.
        - How uploaded sketches and directly drawn sketches can both be incorporated into the same workflow.
        - The practical differences between local testing and GPU-server-based testing for this system.
        - How structured storage of sketches, masks, LASSO regions, and descriptions improves consistency across the pipeline.
        """
    )

    st.warning("What is still uncertain")
    st.markdown(
        """
        - The exact dataset preparation and preprocessing pipeline originally used for LOTS.
        - The best final form of the user-facing drawing interface for usability and experimentation.
        - The final evaluation setup for comparing different interaction modalities.
        - How much the current design choices improve user control in a formal evaluation setting.
        """
    )

elif section == "Problems / Open Questions":
    st.header("Problems / Open Questions")

    for i, q in enumerate(open_questions, start=1):
        st.markdown(f"**Q{i}.** {q}")

    st.subheader("Important design question already addressed")
    st.info(
        """
        A major earlier question was:
        **What happens in regions that are not selected by LASSO?**

        The current solution is:
        **non-selected regions use the layer description**, while selected regions use their own local description.
        """
    )

elif section == "Next Steps":
    st.header("Next Steps")

    for i, step in enumerate(next_steps, start=1):
        st.markdown(f"**{i}.** {step}")

elif section == "Meeting Notes":
    st.header("Meeting Notes")
    st.markdown(
        """
        Use this section to report meeting outcomes in a clean way.
        """
    )

    with st.expander("Initial communication with professor"):
        st.write("- Initial project direction received")
        st.write("- Publication / user-study idea discussed")
        st.write("- Need for a clear technical contribution and evaluation direction noted")

    with st.expander("Meeting with Mattia 5th of March"):
        st.write("- Discussed the current platform")
        st.write("- Discussed how LASSO could be integrated into the platform")
        st.write("- Identified that the input pipeline and payload needed changes")

    with st.expander("Team discussion 17th of March"):
        st.write("- Key question raised: what should happen in non-selected regions?")
        st.write("- Current decision: non-selected regions should use layer descriptions")
        st.write("- Selected LASSO regions keep their own local descriptions")
        st.write("- The updated payload should reflect this hierarchy clearly")

    with st.expander("Team discussion — 24 March"):
        st.write("The team provided specific action points to improve the workflow and evaluation readiness.")

        st.markdown("**Requested tasks:**")
        st.write("1. Create clear documentation of the system and workflow.")
        st.write("2. Use sketches that already produced strong results for validation.")
        st.write("3. Save and track experiments for reproducibility.")

        st.markdown("**My implementation:**")
        st.write(
            "1. Created and continuously updated the Streamlit report to document the system, workflow, and design decisions.")
        st.write(
            "2. Tested sketches previously shared by Davide Talon and confirmed that they also produce strong results both on my local machine and on the GPU server.")
        st.write(
            "3. Designed and implemented a structured system for saving experiments, including sketches, LASSO regions, masks, and associated descriptions after each generation request.")

        st.success(
            "All requested tasks from this meeting have been implemented and validated in the current workflow."
        )

st.divider()
st.caption("End of report")
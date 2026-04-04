import streamlit as st
from datetime import date
from pathlib import Path

st.set_page_config(page_title="Thesis Progress Dashboard", layout="wide")

BASE_DIR = Path(__file__).resolve().parent


def show_video_if_available(relative_path: str, caption: str, missing_message: str):
    video_path = BASE_DIR / relative_path
    if video_path.exists() and video_path.is_file():
        st.video(str(video_path))
        st.caption(caption)
    else:
        st.warning(missing_message)


def show_image_if_available(relative_path: str, caption: str, missing_message: str, use_column_width=True):
    image_path = BASE_DIR / relative_path
    if image_path.exists() and image_path.is_file():
        st.image(str(image_path), caption=caption, use_container_width=use_column_width)
    else:
        st.warning(missing_message)


def show_experiment_image(relative_path: str, fallback_label: str):
    image_path = BASE_DIR / relative_path
    if image_path.exists() and image_path.is_file():
        st.image(str(image_path), caption=fallback_label, use_container_width=True)
    else:
        st.info(f"{fallback_label} not added yet. Put the file at: `{relative_path}`")


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
        "Experiments",
        "Block Diagram",
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

# Example experiment content
experiment_global_description = (
    "A coordinated casual outfit composed of a relaxed short-sleeve top and wide-leg pants, "
    "with localized control over garment details using either LASSO-selected regions or per-layer descriptions."
)

layer_based_descriptions = [
    {
        "layer_name": "Layer 1 — Shirt",
        "description": "a relaxed-fit short-sleeve t-shirt with a V-shaped neckline, slightly dropped shoulders, and a softly curved hem"
    },
    {
        "layer_name": "Layer 2 — Inner Neck Layer",
        "description": "a layered inner neckline detail with a contrasting undershirt visible at the collar, forming a double-layer V-neck effect"
    },
    {
        "layer_name": "Layer 3 — Pants",
        "description": "a pair of high-waisted, wide-leg pants with a relaxed fit, elastic waistband, and straight full-length legs"
    },
]

lasso_based_layers = [
    {
        "layer_name": "Layer 1 — Shirt",
        "layer_description": "a relaxed-fit short-sleeve t-shirt with a V-shaped neckline, slightly dropped shoulders, and a softly curved hem",
        "regions": [
            {
                "region_name": "Region 1 — Neckline",
                "description": "a layered inner neckline detail with a visible inner collar, creating a double-layer V-neck effect"
            },
            {
                "region_name": "Region 2 — Sleeves",
                "description": "short sleeves with a relaxed silhouette and soft folded hems"
            }
        ]
    },
    {
        "layer_name": "Layer 2 — Pants",
        "layer_description": "a pair of high-waisted, wide-leg pants with a relaxed fit and straight full-length legs",
        "regions": [
            {
                "region_name": "Region 1 — Waistband",
                "description": "an elastic waistband with gathered fabric detail"
            }
        ]
    }
]

# ---------- Header ----------
st.title(project_title)
st.caption("Updated for professor and project team • 30 March 2026")
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

    st.subheader("Phase 1 — Before First Meeting (Understanding Stage)")

    phase1 = [
        "Read and understood the LOTS paper and its main methodology.",
        "Studied and understood the mock / prototype implementation of the LOTS codebase.",
        "Successfully ran the project code locally and analyzed how the pipeline works.",
        "Reviewed the implementation step-by-step to understand the components and workflow of the system.",
        "Had a meeting with Mattia on 5 March to discuss the project and the current platform.",
        "Was added as a contributor to the Fashion Design AI GitHub repository.",
        "Implemented the first version of the LASSO tool on the frontend."
    ]

    for i, task in enumerate(phase1, start=1):
        st.markdown(f"**{i}.** {task}")

    st.markdown("### Demo Video — Phase 1")
    show_video_if_available(
        "videos/phase1_demo.MP4",
        "Initial stage of the project: early system exploration, local execution, and first frontend LASSO implementation.",
        "Phase 1 demo video is not available in this deployment."
    )

    st.subheader("Phase 2 — First Week (Integration & Core Implementation)")

    phase2 = [
        "Implemented the LASSO tool on the backend.",
        "Connected LOTS to the platform so the platform can send generation requests to the real model instead of the mock implementation.",
        "Added sketch drawing interaction using mouse / trackpad.",
        "Updated the payload structure so the platform can send LASSO information to the generation pipeline.",
        "Changed the logic for non-selected regions: areas outside the selected LASSO region now use the layer description.",
        "Supported local region descriptions for each LASSO and also global description handling.",
        "Changed the payload structure to handle non-selected regions after using the LASSO tool."
    ]

    for i, task in enumerate(phase2, start=1):
        st.markdown(f"**{i}.** {task}")

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
    show_video_if_available(
        "videos/phase3_demo.mp4",
        "Refined workflow: sketch upload, LASSO v2 interaction, add/remove region support, and structured preparation for generation.",
        "Phase 3 demo video is not available in this deployment."
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

elif section == "Experiments":
    st.header("Experiments")

    st.markdown(
        """
        This section presents a qualitative comparison across multiple experiments
        between two conditioning strategies:

        **A. LASSO-based interaction**
        - Local regions are selected on a full sketch
        - Each region has a local description

        **B. Layer-based interaction**
        - The design is decomposed into layers
        - Each layer has its own description

        Each experiment shows both approaches side by side.
        """
    )

    experiments = [
        "exp1", "exp2", "exp3", "exp4",
        "exp5", "exp6", "exp7", "exp8"
    ]


    st.divider()
    st.subheader(f"Experiment: EX1")

    base_path = f"experiments/exp1"

    # ---------- Visual comparison ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### LASSO-based result")
        show_experiment_image(
            f"{base_path}/lasso_result.png",
            f"exp1 - LASSO result"
        )

    with col2:
        st.markdown("### Layer-based result")
        show_experiment_image(
            f"{base_path}/layer_result.png",
            f"exp1 - Layer result"
        )

    # ---------- Inputs ----------
    st.markdown("### Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_experiment_image(
            f"{base_path}/full_sketch.png",
            "Full sketch"
        )

    with col2:
        show_experiment_image(
            f"{base_path}/lasso_overlay.png",
            "LASSO regions"
        )


    # ---------- Descriptions (optional, can customize later) ----------
    with st.expander("Descriptions (LASSO vs Layer)"):
        st.markdown("**LASSO-based descriptions**")
        st.write("- Region 1: a plain, regular fit, crew-necked top with no waistline")
        st.write("- Layer: a floral, single-breasted, symmetrical blazer jacket with set-in sleeves, notched lapels and welt pockets")

        st.markdown("**Layer-based descriptions**")
        st.write("- Layer 1: a floral, single-breasted, symmetrical blazer jacket with set-in sleeves, notched lapels and welt pockets")
        st.write("- Layer 2: a plain, regular fit, crew-necked top with no waistline")

    st.divider()
    st.subheader(f"Experiment: EX2")

    base_path = f"experiments/exp2"

    # ---------- Visual comparison ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### LASSO-based result")
        show_experiment_image(
            f"{base_path}/lasso_result.png",
            f"exp2 - LASSO result"
        )

    with col2:
        st.markdown("### Layer-based result")
        show_experiment_image(
            f"{base_path}/layer_result.png",
            f"exp2 - Layer result"
        )

    # ---------- Inputs ----------
    st.markdown("### Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_experiment_image(
            f"{base_path}/full_sketch.png",
            "Full sketch"
        )

    with col2:
        show_experiment_image(
            f"{base_path}/lasso_overlay.png",
            "LASSO regions"
        )

    with col3:
        show_experiment_image(
            f"{base_path}/lasso_overlay2.png",
            "LASSO regions 2"
        )

    # ---------- Descriptions (optional, can customize later) ----------
    with st.expander("Descriptions (LASSO vs Layer)"):
        st.markdown("**LASSO-based descriptions**")
        st.write("- Region 1: low-waisted, dotted, symmetrical, fly-front, straight pants with curved pockets")
        st.write("- Region 2: a striped, single-breasted blazer jacket with a regular fit, normal waist, above-the-hip length, notched lapel, welt pockets, and set-in sleeves with wrist-length cuffs")
        st.write("- Layer: a floral, tight-fitting blouse with a normal waist, single-breasted front, symmetrical design, a flap pocket, a shirt collar and wrist-length sleeves")

        st.markdown("**Layer-based descriptions**")
        st.write("- Layer 1: low-waisted, dotted, symmetrical, fly-front, straight pants with curved pockets")
        st.write("- Layer 2: a striped, single-breasted blazer jacket with a regular fit, normal waist, above-the-hip length, notched lapel, welt pockets, and set-in sleeves with wrist-length cuffs")
        st.write("- Layer 3: a floral, tight-fitting blouse with a normal waist, single-breasted front, symmetrical design, a flap pocket, a shirt collar and wrist-length sleeves")

    st.divider()
    st.subheader(f"Experiment: EX3")

    base_path = f"experiments/exp3"

    # ---------- Visual comparison ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### LASSO-based result")
        show_experiment_image(
            f"{base_path}/lasso_result.png",
            f"exp3 - LASSO result"
        )

    with col2:
        st.markdown("### Layer-based result")
        show_experiment_image(
            f"{base_path}/layer_result.png",
            f"exp3 - Layer result"
        )

    # ---------- Inputs ----------
    st.markdown("### Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_experiment_image(
            f"{base_path}/full_sketch.png",
            "Full sketch"
        )

    with col2:
        show_experiment_image(
            f"{base_path}/lasso_overlay.png",
            "LASSO regions"
        )

    with col3:
        show_experiment_image(
            f"{base_path}/lasso_overlay2.png",
            "LASSO regions 2"
        )

    # ---------- Descriptions (optional, can customize later) ----------
    with st.expander("Descriptions (LASSO vs Layer)"):
        st.markdown("**LASSO-based descriptions**")
        st.write("- Region 1: loose, fly-front, maxi-length plain pants with a straight cut and symmetrical design")
        st.write(
            "- Region 2: a regular, floral, symmetrical, zip-up bomber jacket with no waistline, above-the-hip length, wrist-length set-in sleeves and a stand-away collar")
        st.write(
            "- Layer: a loose-fitting, classic-length, dotted t-shirt with a round neckline and no waistline")

        st.markdown("**Layer-based descriptions**")
        st.write("- Layer 1: loose, fly-front, maxi-length plain pants with a straight cut and symmetrical design")
        st.write(
            "- Layer 2: a regular, floral, symmetrical, zip-up bomber jacket with no waistline, above-the-hip length, wrist-length set-in sleeves and a stand-away collar")
        st.write(
            "- Layer 3: a loose-fitting, classic-length, dotted t-shirt with a round neckline and no waistline")

    st.divider()
    st.subheader(f"Experiment: EX4")

    base_path = f"experiments/exp4"

    # ---------- Visual comparison ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### LASSO-based result")
        show_experiment_image(
            f"{base_path}/lasso_result.png",
            f"exp4 - LASSO result"
        )

    with col2:
        st.markdown("### Layer-based result")
        show_experiment_image(
            f"{base_path}/layer_result.png",
            f"exp4 - Layer result"
        )

    # ---------- Inputs ----------
    st.markdown("### Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_experiment_image(
            f"{base_path}/full_sketch.png",
            "Full sketch"
        )

    with col2:
        show_experiment_image(
            f"{base_path}/lasso_overlay.png",
            "LASSO regions"
        )


    # ---------- Descriptions (optional, can customize later) ----------
    with st.expander("Descriptions (LASSO vs Layer)"):
        st.markdown("**LASSO-based descriptions**")
        st.write("- Region 1: a double-breasted, floral jacket with peak lapels, two flap pockets, two welt pockets, wrist-length set-in sleeves and a buckled opening")
        st.write(
            "- Layer: regular, maxi length, symmetrical and straight sailor pants with a fly opening and a striped pattern")

        st.markdown("**Layer-based descriptions**")
        st.write("- Layer 1: a double-breasted, floral jacket with peak lapels, two flap pockets, two welt pockets, wrist-length set-in sleeves and a buckled opening")
        st.write(
            "- Layer 2: regular, maxi length, symmetrical and straight sailor pants with a fly opening and a striped pattern")

    st.divider()

    st.subheader(f"Experiment: EX5")

    base_path = f"experiments/exp5"

    # ---------- Visual comparison ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### LASSO-based result")
        show_experiment_image(
            f"{base_path}/lasso_result.png",
            f"exp5 - LASSO result"
        )

    with col2:
        st.markdown("### Layer-based result")
        show_experiment_image(
            f"{base_path}/layer_result.png",
            f"exp5 - Layer result"
        )

    # ---------- Inputs ----------
    st.markdown("### Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_experiment_image(
            f"{base_path}/full_sketch.png",
            "Full sketch"
        )

    with col2:
        show_experiment_image(
            f"{base_path}/lasso_overlay.png",
            "LASSO regions"
        )


    # ---------- Descriptions (optional, can customize later) ----------
    with st.expander("Descriptions (LASSO vs Layer)"):
        st.markdown("**LASSO-based descriptions**")
        st.write("- Region 1: a pair of tight, maxi, symmetrical leggings pants with a fly opening, a floral pattern, and a curved pocket")
        st.write(
            "- Layer: a loose, above-the-hip, plain sweatshirt with no waistline, a symmetrical design and two flap pockets")

        st.markdown("**Layer-based descriptions**")
        st.write("- Layer 1: a pair of tight, maxi, symmetrical leggings pants with a fly opening, a floral pattern, and a curved pocket")
        st.write(
            "- Layer 2: a loose, above-the-hip, plain sweatshirt with no waistline, a symmetrical design and two flap pockets")

    st.divider()

    st.subheader(f"Experiment: EX6")

    base_path = f"experiments/exp6"

    # ---------- Visual comparison ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### LASSO-based result")
        show_experiment_image(
            f"{base_path}/lasso_result.png",
            f"exp6 - LASSO result"
        )

    with col2:
        st.markdown("### Layer-based result")
        show_experiment_image(
            f"{base_path}/layer_result.png",
            f"exp6 - Layer result"
        )

    # ---------- Inputs ----------
    st.markdown("### Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_experiment_image(
            f"{base_path}/full_sketch.png",
            "Full sketch"
        )

    with col2:
        show_experiment_image(
            f"{base_path}/lasso_overlay.png",
            "LASSO regions"
        )


    # ---------- Descriptions (optional, can customize later) ----------
    with st.expander("Descriptions (LASSO vs Layer)"):
        st.markdown("**LASSO-based descriptions**")
        st.write("- Region 1: A plain, regular fit, black collar, stars on it")
        st.write(
            "- Layer: a leather, single-breasted, welt pockets")

        st.markdown("**Layer-based descriptions**")
        st.write("- Layer 1: a leather, single-breasted, welt pockets")
        st.write(
            "- Layer 2: A plain, regular fit, black collar, stars on it")

    st.divider()

    st.subheader(f"Experiment: EX7")

    base_path = f"experiments/exp7"

    # ---------- Visual comparison ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### LASSO-based result")
        show_experiment_image(
            f"{base_path}/lasso_result.png",
            f"exp7 - LASSO result"
        )

    with col2:
        st.markdown("### Layer-based result")
        show_experiment_image(
            f"{base_path}/layer_result.png",
            f"exp7 - Layer result"
        )

    # ---------- Inputs ----------
    st.markdown("### Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_experiment_image(
            f"{base_path}/full_sketch.png",
            "Full sketch"
        )

    with col2:
        show_experiment_image(
            f"{base_path}/lasso_overlay.png",
            "LASSO regions"
        )


    # ---------- Descriptions (optional, can customize later) ----------
    with st.expander("Descriptions (LASSO vs Layer)"):
        st.markdown("**LASSO-based descriptions**")
        st.write("- Region 1: a loose-fitting, cropped short-sleeve t-shirt with a round crew neckline, dropped shoulders")
        st.write(
            "- Layer: A pair of high-waisted, wide-leg pants with a relaxed fit, elastic waistband, and straight full-length legs")

        st.markdown("**Layer-based descriptions**")
        st.write("- Layer 1: a loose-fitting, cropped short-sleeve t-shirt with a round crew neckline, dropped shoulders")
        st.write(
            "- Layer 2: A pair of high-waisted, wide-leg pants with a relaxed fit, elastic waistband, and straight full-length legs")

    st.divider()
    st.divider()
    st.subheader(f"Experiment: EX8")

    base_path = f"experiments/exp8"

    # ---------- Visual comparison ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### LASSO-based result")
        show_experiment_image(
            f"{base_path}/lasso_result.png",
            f"exp8 - LASSO result"
        )

    with col2:
        st.markdown("### Layer-based result")
        show_experiment_image(
            f"{base_path}/layer_result.png",
            f"exp8 - Layer result"
        )

    # ---------- Inputs ----------
    st.markdown("### Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_experiment_image(
            f"{base_path}/full_sketch.png",
            "Full sketch"
        )

    with col2:
        show_experiment_image(
            f"{base_path}/lasso_overlay.png",
            "LASSO regions"
        )


    # ---------- Descriptions (optional, can customize later) ----------
    with st.expander("Descriptions (LASSO vs Layer)"):
        st.markdown("**LASSO-based descriptions**")
        st.write("- Region 1: V-shaped neckline")
        st.write(
            "- Layer: a relaxed-fit short-sleeve t-shirt, slightly dropped shoulders, and a softly curved hem")

        st.markdown("**Layer-based descriptions**")
        st.write("- Layer 1: a relaxed-fit short-sleeve t-shirt, slightly dropped shoulders, and a softly curved hem")
        st.write(
            "- Layer 2: V-shaped neckline")

    st.divider()

    st.subheader("Overall Observation")
    st.markdown(
        """
        Across multiple experiments, the comparison highlights differences between
        region-based and layer-based conditioning.

        LASSO-based interaction enables fine-grained local control on a single sketch,
        while layer-based interaction provides a more structured decomposition of the design.

        These experiments provide a qualitative basis for evaluating controllability
        and interaction design in the system.
        """
    )

elif section == "Block Diagram":
    st.header("System Block Diagram")

    st.markdown(
        """
        This section summarizes the actual implemented workflow, from the user interaction in the frontend
        to the final request sent to the LOTS server.

        In the current system, the request does **not** go directly from the frontend to the AI engine.
        Instead, the pipeline is:

        **Frontend → Backend API → AI Engine → LOTS server**

        Another important point is that **LASSO regions are not sent directly to LOTS as region objects**.
        They are first processed inside the AI engine and converted into LOTS-compatible
        **local sketch + local description pairs**.
        """
    )

    st.subheader("Text Version of the Diagram")
    st.code(
        """User
│
├── Draws sketch on canvas or uploads sketch
├── Adds global description
├── Adds layer descriptions
└── Optionally selects local regions with LASSO and adds region descriptions
        ↓
Frontend Platform
│
├── Manages canvas interaction
├── Stores sketch image
├── Stores layers
└── Stores LASSO regions
        ↓
Backend API (/api/generate)
│
├── Receives frontend JSON request
├── Validates request structure
├── Checks canvas, layers, and lasso region consistency
└── Forwards valid request to AI Engine
        ↓
Structured Request Sent to AI Engine
│
├── canvas
├── global_prompt
├── sketch_image
├── reference_image
├── layers[]
│   ├── id
│   ├── name
│   ├── description
│   └── image_data
└── lasso_regions[]
    ├── id
    ├── layer_id
    ├── description
    ├── points
    └── mask
        ↓
AI Engine
│
├── validates payload again
├── normalizes request fields
├── saves debug artifacts
├── loads full sketch image
├── loads layer images
├── for each valid layer:
│   └── creates one local sketch + one local description
├── for each LASSO region:
│   ├── uses region mask or polygon points
│   ├── extracts a local sketch crop from the source image
│   └── pairs it with the region description
└── converts everything into LOTS-compatible payload format
        ↓
Payload Sent to LOTS Server
│
├── global_description
├── local_description[]
└── sketch[]
        ↓
LOTS Server / LOTS Model
│
├── receives one global description
├── receives multiple local descriptions
└── receives multiple local sketch images
        ↓
Generated Output
│
├── generated image returned by LOTS
├── debug files saved by AI Engine
├── masks and local sketches saved
└── experiment bundle saved for qualitative comparison""",
        language="text"
    )

    st.subheader("Actual Request Format Received by the Backend API")
    st.code(
        """{
  "canvas": {
    "width": 1024,
    "height": 1024
  },
  "global_prompt": "overall design description",
  "sketch_image": "base64_full_sketch",
  "reference_image": "optional_base64_reference",
  "layers": [
    {
      "id": 1,
      "name": "shirt",
      "description": "layer-level description",
      "image_data": "optional_base64_layer_image"
    }
  ],
  "lasso_regions": [
    {
      "id": "region_1",
      "layer_id": 1,
      "description": "region-level description",
      "points": [x1, y1, x2, y2, x3, y3],
      "mask": "optional_base64_mask"
    }
  ]
}""",
        language="json"
    )

    st.subheader("Actual Payload Sent by the AI Engine to the LOTS Server")
    st.code(
        """{
  "global_description": "overall design description",
  "local_description": [
    "layer-level description 1",
    "layer-level description 2",
    "region-level description 1",
    "region-level description 2"
  ],
  "sketch": [
    "base64_layer_image_1",
    "base64_layer_image_2",
    "base64_region_crop_1",
    "base64_region_crop_2"
  ]
}""",
        language="json"
    )

    st.subheader("Important Clarification")
    st.info(
        """
        In the current implementation, the backend API forwards the structured request to the AI engine,
        and the AI engine performs the main preprocessing step.

        This means:
        - the frontend sends **layers** and **lasso_regions** to the backend,
        - the backend forwards them to the AI engine,
        - the AI engine converts them into LOTS-compatible inputs,
        - and the LOTS server receives only:
          **one global description, a list of local descriptions, and a list of local sketch images**.
        """
    )

    st.subheader("Input / Output Example")
    in_col, out_col = st.columns(2)

    with in_col:
        st.markdown("### Inputs to the overall system")
        st.markdown(
            """
            - Full sketch or uploaded sketch
            - Global description
            - Layer descriptions
            - Optional layer images
            - LASSO-selected regions
            - Region-level local descriptions
            """
        )

    with out_col:
        st.markdown("### Outputs from the overall system")
        st.markdown(
            """
            - Generated fashion image
            - Saved debug request files
            - Saved masks
            - Saved local sketch crops
            - Saved experiment bundle for comparison
            """
        )

    st.subheader("Why this diagram matters")
    st.markdown(
        """
        This updated diagram reflects the implemented architecture more accurately.

        In particular, it clarifies:
        - that the backend API is an explicit stage between the frontend and AI engine,
        - that request validation happens before AI-engine processing,
        - that LASSO regions are used for preprocessing rather than being sent directly to LOTS,
        - and that the AI engine acts as the conversion layer between the interactive platform and the LOTS server.
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
            "1. Created and continuously updated the Streamlit report to document the system, workflow, and design decisions."
        )
        st.write(
            "2. Tested sketches previously shared by Davide Talon and confirmed that they also produce strong results both on my local machine and on the GPU server."
        )
        st.write(
            "3. Designed and implemented a structured system for saving experiments, including sketches, LASSO regions, masks, and associated descriptions after each generation request."
        )

        st.success(
            "All requested tasks from this meeting have been implemented and validated in the current workflow."
        )

st.divider()
st.caption("End of report")
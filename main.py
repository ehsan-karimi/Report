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
    "Implemented Lasso Tool, Front and back both."
]

open_questions = [
    "How did you prepare the dataset for LOTS?"
]

next_steps = [
    "Validate the LASSO tool with more realistic user interactions.",
    "Measure whether LASSO-based region selection improves usability and control.",
    "Clean the implementation and document the code changes clearly.",
    "Prepare visual examples showing the full workflow from selection to generation.",
    "Define an evaluation plan for the technical part and the future user study.",
    "Complete the AI engine part in platform with the real model",
    "Test the whole platform that is connected to AI model"
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
        "title": "Attached mask to the layer input structure",
        "desc": "The generated mask is stored as part of the layer input object sent to the backend. This allows each layer to contain multiple LASSO-defined regions representing precise user selections."
    },
    {
        "title": "Integrated mask into the processing pipeline",
        "desc": "The mask is forwarded through the generation pipeline so downstream modules can use it to restrict processing to the selected region. This enables localized editing or generation instead of modifying the whole image."
    },
    {
        "title": "Supported multiple LASSO regions per layer",
        "desc": "The system allows multiple LASSO selections within a single layer. Each region is stored separately and converted to its own mask, enabling fine-grained control over multiple parts of the design."
    },
    {
        "title": "Validated mask generation and pipeline integration",
        "desc": "Tested the system by running the platform after integrating the LASSO tool and verifying that the generated masks correctly match the drawn regions and are correctly passed to the backend processing stage."
    }
]

# ---------- Header ----------
st.title(project_title)
st.caption(f"Prepared for professor and project team • {today}")
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
            - what I have completed,
            - what remains unclear,
            - and what I plan to do next.
            """
        )
    with c2:
        st.info(
            """
            **Main objective**

            Understand the existing platform and define how a LASSO-based component can improve or extend it, Then we will do a user study to understand which modality is the best for the case at hand.
            """
        )


elif section == "Project Context":
    st.header("Project Context")
    st.markdown(
        """
        The project started from the platform/tool shared by the team.
        My current focus is understanding the existing system and studying how to integrate a LASSO-based method in a meaningful way.

        At this stage, the project appears to involve:
        - an existing AI-based fashion/design-related workflow,
        - a possible improvement through LASSO,
        - and later a user study to evaluate which interaction or modeling choice works best.
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
    for i, task in enumerate(completed_tasks, start=1):
        st.markdown(f"**{i}.** {task}")

    st.subheader("Detailed summary")
    st.markdown(
        """
        So far, my work has mainly focused on understanding the project scope and reducing ambiguity.
        I first studied the material and links shared by the professor. After that, I had a meeting with Mattia,
        where I tried to understand the current platform and how much of the proposed LASSO direction was already defined.

        One important outcome is that the current integration of LASSO is not yet clearly specified.
        Because of that, a big part of my progress has been analytical work: understanding the existing engine,
        identifying where LASSO might fit, and turning a vague project idea into a concrete technical plan.
        """
    )

elif section == "LASSO Implementation Steps":
    st.header("Technical Explanation of the LASSO Tool")
    st.markdown(
        """
        This section focuses only on the technical implementation of the LASSO tool:
        how the user interaction is represented, how the selected region is transformed into a usable format,
        and how that information is passed through the system pipeline.
        """
    )

    for i, step in enumerate(lasso_steps, start=1):
        st.markdown(f"### Step {i}. {step['title']}")
        st.write(step["desc"])

    st.subheader("LASSO Data Flow")
    st.code(
        """User draws free-form region on canvas
        ↓
Polygon vertices are collected
        ↓
Polygon is rasterized into a binary mask
        ↓
Mask is attached to the selected layer object
        ↓
Layer data is sent to backend / AI engine
        ↓
Downstream processing uses the mask as region-of-interest""",
        language="text",
    )

    st.subheader("Input Structure Example")
    st.code(
        """{
  \"layers\": [
    {
      \"layer_id\": 0,
      \"regions\": [
        {
          \"polygon\": [[x1, y1], [x2, y2], [x3, y3], ...],
          \"mask\": \"binary mask with same height/width as the image\"
        },
        {
          \"polygon\": [[x1, y1], [x2, y2], [x3, y3], ...],
          \"mask\": \"binary mask\"
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
5. Store the generated mask in the corresponding layer region object
6. Pass the mask to downstream processing modules""",
        language="text",
    )

    st.subheader("Why this matters technically")
    st.markdown(
        """
        The key technical contribution of the LASSO tool is that it replaces coarse image interaction with
        **pixel-level region selection**. Instead of applying processing to a whole layer or a broad area,
        the system can now receive a precise region-of-interest mask derived directly from the user's free-form input.
        This makes the interaction more flexible and allows localized processing in the pipeline.
        """
    )

elif section == "Current Understanding":
    st.header("Current Understanding")

    st.success("What I understand well")
    st.markdown(
        """
        - There is already an existing platform/pipeline.
        - LOTS Architecture.
        - Platform Architecture.
        - How should Lasso tool work in this platform.
        - The task is not to start from zero, but to improve or extend what already exists.
        - Before implementation, the pipeline needs to be little bit change.
        """
    )

    st.warning("What is still uncertain")
    st.markdown("""
        - Dataset that used for LOTS.
        """)

elif section == "Problems / Open Questions":
    st.header("Problems / Open Questions")

    for i, q in enumerate(open_questions, start=1):
        st.markdown(f"**Q{i}.** {q}")

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

    with st.expander("Meeting with professor"):
        st.write("- Initial project direction received")
        st.write("- Publication/user-study idea discussed")

    with st.expander("Meeting with Mattia"):
        st.write("- Discussed the current platform")
        st.write("- Noted that LASSO integration is not yet clearly defined")

st.divider()

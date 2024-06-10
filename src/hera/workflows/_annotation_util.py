"""Utility functions for manipulating typing.Annotated."""

from typing import Optional, Union

from hera.workflows.artifact import Artifact
from hera.workflows.parameter import Parameter

try:
    from typing import Annotated, get_args  # type: ignore
except ImportError:
    from typing_extensions import Annotated, get_args


def get_input_annotation(annotation: Annotated) -> Optional[Union[Parameter, Artifact]]:
    """Return unique Parameter or Artifact associated with an annotation, if one exists."""
    meta_annotations = [md for md in get_args(annotation)[1:] if isinstance(md, (Parameter, Artifact))]
    if len(meta_annotations) > 1:
        raise ValueError("Annotated inputs/outputs may only have one Parameter or Artifact annotation.")
    elif len(meta_annotations) == 1:
        return meta_annotations[0].copy()
    else:
        return None

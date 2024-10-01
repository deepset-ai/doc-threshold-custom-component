from typing import List
from haystack import Document
from dc_custom_component.thresholders.thresholder import Thresholder


def test_thresholder_empty() -> None:
    documents: List[Document] = []
    thresholder = Thresholder(threshold=0.5)
    assert thresholder.run(documents)["documents"] == []


def test_thresholder_nonempty() -> None:
    documents: List[Document] = [
        Document(content="a", score=0.6),
        Document(content="b", score=0.4),
    ]
    thresholder = Thresholder(threshold=0.5)
    assert thresholder.run(documents)["documents"] == [Document(content="a", score=0.6)]

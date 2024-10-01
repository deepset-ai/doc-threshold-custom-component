from typing import List, Dict
from haystack import Document, component


@component
class Thresholder:
    """
    A component that takes a list of documents and returns only
    those documents whose score is greater than a given threshold.
    """

    def __init__(
        self,
        threshold: float,
    ):
        self.threshold = threshold

    @component.output_types(documents=List[Document])
    def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
        """
        Filter documents based on the score.

        :param documents: List of documents to filter.
        :returns: List of documents whose score is greater than the threshold.
        """
        return {"documents": [doc for doc in documents if doc.score >= self.threshold]}

from typing import Annotated

from fastapi import Depends

from api.user.models import Therapist
from api.user.repositories import TherapistRepository


class TherapistRecommendationService:

    def __init__(
        self,
        therapist_repo: Annotated[TherapistRepository, Depends()]
    ):
        self._therapist_repo = therapist_repo

    def run(self, expertises: list[int]) -> list[Therapist]:
        therapists = self._therapist_repo.get_therapists_by_expertise(expertises)

        return sorted(therapists, key=lambda t: self._sort_by_expertise_relevance(t, expertises), reverse=True)

    @staticmethod
    def _sort_by_expertise_relevance(therapist: Therapist, expertises: list[int]):
        relevance_score = 0
        for expertise in therapist.expertises:
            relevance_score += expertises.count(expertise)

        return relevance_score

from enum import StrEnum


class Gender(StrEnum):
    MALE = "Чоловік"
    FEMALE = "Жінка"


class MarriageStatus(StrEnum):
    SINGLE = "Неодружений/незаміжня"
    MARRIED = "Одружений/заміжня"
    DIVORCED = "Розлучен(ий/а)"
    SEPARATED = "Живу окремо"
    WIDOWED = "Вдова/вдівець"


class TherapistExpertiseEnum(StrEnum):
    CBT = "Когнітивно-поведінкова терапія"
    HUMANISTIC = "Гуманістична терапія"
    PTSD = "ПТСР"
    EXISTENTIAL = "Екзистенційна терапія"
    GROUP = "Сімейна та парна терапія"
    NEURO = "Нейропсихологія"
    CLINICAL = "Клінічна психологія"
    STRESS_ANXIETY = "Управління стресом та тривогою"
    COUNSELING = "Консультативна психологія"
    GRIEF_LOSS = "Консультації з питань горя та втрат"
    ADDICTION = "Консультації з питань залежності"
    CRISIS = "Кризове втручання"


EXPERTISE_CODES = {
    1: TherapistExpertiseEnum.CBT,
    2: TherapistExpertiseEnum.HUMANISTIC,
    3: TherapistExpertiseEnum.PTSD,
    4: TherapistExpertiseEnum.EXISTENTIAL,
    5: TherapistExpertiseEnum.GROUP,
    6: TherapistExpertiseEnum.NEURO,
    7: TherapistExpertiseEnum.CLINICAL,
    8: TherapistExpertiseEnum.STRESS_ANXIETY,
    9: TherapistExpertiseEnum.COUNSELING,
    10: TherapistExpertiseEnum.GRIEF_LOSS,
    11: TherapistExpertiseEnum.ADDICTION,
    12: TherapistExpertiseEnum.CRISIS
}

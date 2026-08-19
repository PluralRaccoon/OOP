"""
Quest 1: The Quest Board Parser (Data Boundaries & Exhaustiveness)

The Scenario:
You are programming the Guild's Quest Board. The board receives a raw JSON feed of new quests from villages. 
You need to parse this messy dictionary into strict Python objects, calculate their danger levels, and route them correctly.

The Raw JSON Input:
JSON

[
  {
    "quest_id": "Q-001",
    "target_monster": "Rathalos",
    "objective_type": "hunt",
    "zenny_reward": 8600,
    "environment_hazards": ["volcanic_heat"]
  },
  {
    "quest_id": "Q-002",
    "target_monster": "Zinogre",
    "objective_type": "capture",
    "zenny_reward": 12000
  }
]

Your Mission:
Build a QuestManager class with the following requirements:

    The Typing: Define a TypedDict for the raw JSON. 
    The objective_type must be a Literal["hunt", "capture", "repel"]. 
    The environment_hazards key might be missing entirely, so type it appropriately.

    The Model: Create a @dataclass called GuildQuest to hold the cleaned data. 
    Use field(default_factory=...) to ensure quests without hazards get an empty list, not a shared mutable list.

    Function 1: ingest_quests(raw_data: list[dict]) -> list[GuildQuest]
        A method that takes the JSON payload and converts it into your dataclasses.

    Function 2: calculate_danger_level(quest: GuildQuest) -> str
        Use a modern match/case statement on the objective_type. 
        Return "High" for capture, "Medium" for hunt, and "Low" for repel. Crucially, include assert_never to guarantee the type checker will warn you if the Guild adds a "slay" objective later.

    Function 3: dispatch_quest(quest: GuildQuest) -> None
        A method that prints out a formatted string for the Hunters, utilizing the danger level.
"""

from typing import TypedDict, Literal, NotRequired, assert_never
from dataclasses import dataclass, field

class Quest(TypedDict):
    quest_id: str
    target_monster: str
    objective_type: Literal["hunt", "capture", "repel"]
    zenny_reward: int
    environment_hazards: NotRequired[list[str]]

@dataclass(slots=False)
class GuildQuest:
    quest_id: str
    target_monster: str
    objective_type: Literal["hunt", "capture", "repel"]
    zenny_reward: int
    environment_hazards: list[str] = field(default_factory=list)

def ingest_quests(raw_data: list[Quest]) -> list[GuildQuest]:
    cleaned_quests: list[GuildQuest] = []
    for quest in raw_data:
        new_quest = GuildQuest(
            quest_id=quest["quest_id"],
            target_monster=quest["target_monster"],
            objective_type=quest["objective_type"],
            zenny_reward=quest["zenny_reward"],
            environment_hazards=quest.get("environment_hazards", [])
        )

        cleaned_quests.append(new_quest) 

    return cleaned_quests

def calculate_danger_level(quest: GuildQuest) -> str:
    match quest.objective_type:
        case "capture":
            return "High"
        case "hunt":
            return "Medium"
        case "repel":
            return "Low"
        case _:
            assert_never(quest.objective_type)
        
def dispatch_quest(quest: GuildQuest) -> None:
    print("--- *Horn sound* ---")
    print("Get ready Hunter, for your next quest: ")
    print(f"Target: {quest.target_monster}")
    print(f"Danger Level: {calculate_danger_level(quest)}")
    print(f"Objective: {quest.objective_type}")

    if quest.environment_hazards:
        print("-> Take care of hazards:", *quest.environment_hazards)

    print(f"Reward: {quest.zenny_reward} Zenny.")
    print("--- Quest Begins ---")

from questboardparser import GuildQuest, Quest, dispatch_quest, ingest_quests

def main() -> None:
    quests: list[Quest] = [
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

    cleaned_quests: list[GuildQuest] = ingest_quests(quests)
    dispatch_quest(cleaned_quests[0])

if __name__ == "__main__":
    main()
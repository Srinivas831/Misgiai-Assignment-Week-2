# recommender.py

from agents_data import agents

def extract_keywords(task):
    return task.lower().split()

def recommend_agents(task):
    keywords = extract_keywords(task)
    scored_agents = []

    for name, data in agents.items():
        score = 0
        explanation = []

        for kw in keywords:
            if kw in [lang.lower() for lang in data["languages"]]:
                score += 2
                explanation.append(f"✅ Matches language: {kw}")
            if kw in [s.lower() for s in data["strengths"]]:
                score += 2
                explanation.append(f"✅ Matches strength: {kw}")
            if kw in [t.lower() for t in data["ideal_tasks"]]:
                score += 3
                explanation.append(f"✅ Matches ideal task: {kw}")
            if kw in [w.lower() for w in data["weaknesses"]]:
                score -= 3
                explanation.append(f"⚠️ Matches weakness: {kw}")

        if "offline" in keywords and data["offline_support"]:
            score += 1
            explanation.append("✅ Supports offline usage")

        scored_agents.append({
            "name": name,
            "score": score,
            "explanation": explanation,
            "agent_info": {
                "languages": data["languages"],
                "strengths": data["strengths"],
                "weaknesses": data["weaknesses"],
                "ideal_tasks": data["ideal_tasks"],
                "requires_setup": data["requires_setup"],
                "offline_support": data["offline_support"]
            }
        })

    # Sort by score descending
    top_agents = sorted(scored_agents, key=lambda x: x["score"], reverse=True)[:3]

    return top_agents

if __name__ == "__main__":
    task = input("🔍 Enter your coding task: ")
    results = recommend_agents(task)

    print("\n🎯 Top Recommended Agents:\n")
    for agent in results:
        print(f"🔹 {agent['name']} (Score: {agent['score']})")
        for reason in agent["explanation"]:
            print(f"  - {reason}")
        print()

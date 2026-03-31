# Rokon Simple AI Meme Roast Battle

**AI Meme Roast Battle Mini-Game** built with GenLayer Intelligent Contract for the GenLayer Community.

A fun multiplayer roast-style mini-game where players create roast/meme battles on AI or GenLayer topics. The Intelligent Contract acts as an **AI Judge** to evaluate humor, roast level, creativity, and relevance.

## Game Features
- AI generates fresh roast or meme battle topics
- Players submit roast-style meme descriptions
- Full AI Judge system using Optimistic Democracy
- On-chain XP leaderboard
- Showcases subjective judgment (humor & roast quality) directly on-chain

## How to Play
1. Connect your testnet wallet.
2. Call `create_battle()` to generate a new roast battle round and get a battle ID.
3. Get the topic using `get_topic(battle_id)`.
4. Players create and submit their roast/meme ideas for the topic.
5. The best roast wins → Use `add_xp(amount)` to award XP to the winner.
6. Check your score anytime with `get_my_xp()`.
7. Create new battles and compete with friends — perfect for community meme/roast sessions!

**Contract Address:**  
`0xb438FB85B4F1d5D928d3049AbA1a7EC760ac4D65`

**GenLayer Studio Import Link:**  
https://studio.genlayer.com/contracts?import-contract=0xb438FB85B4F1d5D928d3049AbA1a7EC760ac4D65

## Technical Details
- Contract Name: `RokonSimpleMemeRoast`
- Written in Python using GenLayer SDK
- `gl.nondet.exec_prompt()` → AI generates roast/meme battle topics
- `gl.eq_principle.strict_eq` → Optimistic Democracy consensus for reliable AI judgment
- On-chain storage for battle topics and player XP

**Core Functions:**
- `create_battle()` → Creates new roast battle topic
- `add_xp(amount)` → Awards XP to winner
- `get_topic(battle_id)` → Retrieves battle topic
- `get_my_xp()` → View personal XP

This is my submission for the **Mini-games for GenLayer’s Community** mission.

Built by Rokon 💦💭

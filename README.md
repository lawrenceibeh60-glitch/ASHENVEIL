# ASHENVEIL

> **When the light fades, hope remains.**

ASHENVEIL is a planned third-person, single-player medieval fantasy RPG built with **Panda3D and Python**. It aims to combine exploration, action combat, memorable characters, meaningful choices, and an emotionally grounded story shaped by themes of faith, redemption, mercy, justice, truth, and hope.

The project is in its **foundation / pre-production stage**. This repository is the home for the game's source code, design documentation, original narrative, tools, and development history.

---

## Project at a glance

| Area | Direction |
|---|---|
| Working title | ASHENVEIL |
| Genre | Third-person action RPG |
| Setting | Original medieval fantasy world |
| Visual direction | Stylized realism |
| Core experience | Exploration, combat, story, discovery |
| Engine | Panda3D |
| Main language | Python |
| Initial target | Windows PC |
| Play mode | Offline, single-player |
| Modelling approach | Browser-based modelling tools, procedural geometry, and properly licensed asset packs |
| Blender | **Not part of this project's workflow** |

The initial target is a compact, carefully crafted world rather than a huge, mostly empty open world. Quality of locations, atmosphere, characters, and encounters takes priority over map size.

## Creative vision

ASHENVEIL is intended to feel cinematic, emotional, mysterious, and meaningful. Its world should tell stories through places, people, objects, conversations, discoveries, and the consequences of player decisions.

### Narrative themes

The story will explore:

- Faith and hope in difficult circumstances
- Redemption, repentance, and forgiveness
- Humility and sacrificial love
- Justice, mercy, and truth
- Grief, corruption, greed, fear, and reconciliation
- The consequences of revenge and the possibility of choosing compassion

The narrative will combine direct biblical inspiration and respectful engagement with Scripture with an original fantasy world, characters, history, and conflicts. Fictional worldbuilding will be clearly distinguished from biblical teaching. Faith will not be reduced to a purchasable statistic, morality meter, or experience-point system.

## World and story

The working setting is the ancient kingdom of **Elarion**, a land in decline. Its people live with the consequences of corruption, fear, grief, broken relationships, and an ancient event whose true history has been deliberately buried.

The player takes the role of a wanderer who arrives in a remote frontier region. Through exploration, relationships, encounters, discoveries, and difficult decisions, the player gradually uncovers what happened and why the kingdom is changing.

### Planned regions

1. **Greyhaven** — The starting settlement, with merchants, farmers, families, and a small chapel. Its ordinary people and personal struggles introduce the world.
2. **Thornwood** — A forest of wildlife, hidden paths, abandoned places, and traces of an older history.
3. **Oldwatch** — A ruined fortress holding political and historical secrets.
4. **Ashen Marsh** — A dangerous region connected to an ancient tragedy.
5. **The Hollow** — An underground complex tied to the central revelation.

These are planned locations, not completed game levels. Their layouts, quests, and final content may evolve during development.

## Gameplay vision

### Player and exploration

Planned systems include:

- Third-person movement and camera controls
- Walking, running, jumping, and contextual interaction
- Collision-aware traversal and designated climbing routes
- Swimming where appropriate to the world
- Exploration rewards, hidden locations, documents, inscriptions, and environmental clues
- Resource gathering and world interactions
- Weather and day/night atmosphere
- Puzzles, locks, and secrets

### Combat

Combat is intended to be responsive and deliberate, with some Souls-lite influence without making the game unnecessarily punishing.

Planned combat features:

- Light and heavy attacks
- Blocking, dodging, and parrying
- Lock-on targeting
- Stamina and health systems
- Weapon-specific moves and animations
- Contextual finishers
- Enemy reactions and readable attack patterns

The first weapon focus is the sword. Later equipment may include shields, two-handed weapons, spears, and bows. Any supernatural or special abilities will be designed to fit the world's narrative rules.

### Enemies and encounters

Planned enemy categories include wildlife, human threats such as bandits, supernatural creatures, elite enemies, and bosses. Enemy variety should come from behaviour, tactics, and encounter design—not just increased health.

### Character development

The proposed attributes are:

- Strength
- Endurance
- Agility
- Wisdom
- Resolve
- Perception

Potential skill paths include Warrior, Ranger, and Arcanist. The intention is to allow combinations rather than lock the player into a rigid class.

### NPCs, dialogue, and choices

NPCs should feel like people with their own concerns and roles in the world. Planned features include:

- Dialogue trees and character-specific conversations
- NPC schedules and daily routines where practical
- Relationship states and quest involvement
- Reactions to important player decisions
- Branching quests and consequences

Choices will not simply be reduced to a good/evil score. The writing will explore difficult tensions such as justice versus revenge, mercy versus enabling harm, and truth versus comfort.

### RPG systems

Planned supporting systems include inventory, equipment, items, loot, progression, skills, quests, dialogue, interactions, and save/load.

## Initial playable target

The first meaningful playable slice should be small enough to finish and test, but complete enough to prove the game's foundations.

The target is:

- One playable character
- A small, explorable village area
- A connected forest area
- Basic third-person movement and camera
- A working sword combat loop
- Two enemy types
- At least one NPC with working dialogue
- One complete quest
- One mini-boss encounter
- Basic inventory and interaction
- Working save/load

This is a development target, not a claim that these features already exist.

## Technology and production approach

### Runtime

- **Panda3D** for the game runtime, rendering, scene management, and application loop.
- **Python** for gameplay systems, tools, data processing, and project automation.
- **Panda3D Actor** for animated characters.
- **Bullet physics** for appropriate physics and collision tasks.
- **Panda3D task manager** for scheduled runtime updates.
- **DirectGUI initially**, with a custom-styled interface planned as the game develops.
- **JSON** for configuration and structured game content.
- **SQLite may be used** for structured local save data if it proves useful.

The game is intended to run offline without mandatory accounts, online services, or a hosted backend.

### Models and assets

Blender is explicitly excluded from the planned workflow.

The intended asset pipeline uses browser-based modelling tools such as **Spline** and **Blockbench**, external asset packs with suitable licences, and procedural geometry created with Python where appropriate.

The preferred interchange format is **GLB/glTF**, using panda3d-gltf where compatible. Asset imports must be tested for geometry, skeletons, animations, materials, textures, and transparency. OBJ may be used as a fallback for static geometry when appropriate.

Procedural Python tools may generate or help construct terrain, hills, buildings, trees, vegetation, bridges, paths, decorations, and simple effects.

No asset pack will be treated as free to use merely because it can be downloaded. Each external asset must have its licence checked. Required attribution and restrictions must be respected and recorded.

### Performance goals

The game should be designed with low-to-mid-range Windows PCs in mind. A 60 FPS goal on suitable hardware is a stretch target, not a guaranteed minimum. Performance will be measured on actual hardware early, and visual complexity will be balanced against stability and frame rate.

## Planned project structure

The exact structure may change as implementation reveals better boundaries. The intended organization is:

    ASHENVEIL/
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── LICENSE
    ├── config/
    │   ├── game.json
    │   ├── graphics.json
    │   └── controls.json
    ├── engine/
    │   ├── core/
    │   ├── rendering/
    │   ├── physics/
    │   ├── audio/
    │   ├── input/
    │   ├── scenes/
    │   └── events/
    ├── gameplay/
    │   ├── player/
    │   ├── combat/
    │   ├── enemies/
    │   ├── npc/
    │   ├── quests/
    │   ├── dialogue/
    │   ├── inventory/
    │   ├── progression/
    │   └── interactions/
    ├── world/
    │   ├── regions/
    │   ├── greyhaven/
    │   ├── thornwood/
    │   ├── oldwatch/
    │   ├── ashen_marsh/
    │   └── hollow/
    ├── ui/
    │   ├── menus/
    │   ├── hud/
    │   ├── inventory/
    │   ├── dialogue/
    │   └── settings/
    ├── assets/
    │   ├── characters/
    │   ├── animations/
    │   ├── environments/
    │   ├── buildings/
    │   ├── props/
    │   ├── weapons/
    │   ├── textures/
    │   ├── audio/
    │   └── effects/
    ├── data/
    │   ├── quests/
    │   ├── dialogue/
    │   ├── items/
    │   ├── enemies/
    │   ├── characters/
    │   └── lore/
    ├── narrative/
    │   ├── story/
    │   ├── scripture/
    │   ├── characters/
    │   └── world_history/
    ├── tools/
    │   ├── asset_validator/
    │   ├── asset_importer/
    │   └── world_builder/
    ├── saves/
    └── tests/

Generated files, local saves, private credentials, and large source assets should be handled deliberately and should not be committed unless the project needs them in version control.

## Development roadmap

The roadmap describes intended work. A milestone is only marked complete when its implementation exists in the repository and has been tested. A planned feature is not considered finished simply because it appears in this document.

| Milestone | Scope | Status |
|---|---|---|
| M0 — Production foundation | Repository structure, Panda3D setup, dependency management, asset import foundation, launchable test scene, automated checks | ⬜ Planned |
| M1 — Player foundation | Third-person camera, movement, jumping, interaction, animation, collision and physics | ⬜ Planned |
| M2 — Combat foundation | Sword combat, blocking, dodging, stamina, health/damage, enemy behaviour | ⬜ Planned |
| M3 — World foundation | Greyhaven, terrain, vegetation, buildings, interiors, atmosphere, region transitions | ⬜ Planned |
| M4 — RPG systems | Inventory, equipment, attributes, progression, items, skills, interaction | ⬜ Planned |
| M5 — Narrative systems | Dialogue, NPC routines, quests, branching decisions, events, save/load | ⬜ Planned |
| M6 — First vertical slice | Playable opening, village, forest, dungeon section, quests, mini-boss, cinematics, audio | ⬜ Planned |
| M7 — Full content production | Remaining regions, story chapters, enemies, bosses, side quests, equipment, abilities, endings | ⬜ Planned |
| M8 — Polish and release preparation | Optimization, bug fixing, accessibility, graphics settings, Windows packaging and installation tests | ⬜ Planned |

### M0 acceptance criteria

The first foundation milestone should not be considered complete until:

1. The project can be installed from documented dependencies.
2. The game launches without a fatal error.
3. A test scene renders.
4. At least one external 3D asset can be imported and displayed.
5. The project has a repeatable test/check process.
6. Setup and run instructions are documented.

## Development principles

- Build working systems rather than visual placeholders presented as finished features.
- Keep gameplay systems modular and testable.
- Prefer small, connected, memorable environments over empty scale.
- Test asset compatibility before building production workflows around a tool or format.
- Track third-party asset sources and licence requirements.
- Keep the game playable offline.
- Test performance early, especially on modest hardware.
- Document meaningful architecture and gameplay decisions.
- Do not mark roadmap items complete until they have been implemented and verified.

## Current status

**Current phase:** Repository and project foundation.

Completed:
- [x] Public GitHub repository created.
- [x] Proprietary All Rights Reserved licence added.

Not yet implemented or verified:
- [ ] Panda3D application and launch entry point
- [ ] Dependency setup
- [ ] Initial scene and rendering
- [ ] Asset import pipeline
- [ ] Player controller and camera
- [ ] Combat, enemies, NPCs, quests, and RPG systems
- [ ] World regions and narrative content
- [ ] Save/load
- [ ] Automated tests and Windows packaging

Repository: https://github.com/lawrenceibeh60-glitch/ASHENVEIL

## Licence and permissions

The repository is public for visibility, but the project is **not open source**. The root LICENSE file contains the project's proprietary All Rights Reserved terms.

Unless written permission is granted by the copyright holder, viewing the repository does not grant permission to copy, modify, redistribute, republish, or commercially use project materials.

Third-party assets, libraries, fonts, audio, and other dependencies remain subject to their own licences. The project's proprietary licence does not replace or override those terms.

For permission requests, contact the repository owner through GitHub.

---

*ASHENVEIL is being built step by step. This README records the intended direction and current status; implementation and verified progress take precedence over plans.*

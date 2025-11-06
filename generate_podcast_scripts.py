#!/usr/bin/env python3
"""
Script to generate podcast scripts for Azure AZ-204 training course.
Combines intro.md, exercises.md, and az-204.md into audio-friendly podcast.md
"""

import os
from pathlib import Path

def find_topics_with_complete_scripts():
    """Find all topics that have intro.md, exercises.md, and az-204.md"""
    scripts_dir = Path("scripts")
    topics = []

    for topic_dir in sorted(scripts_dir.iterdir()):
        if not topic_dir.is_dir():
            continue

        intro_file = topic_dir / "intro.md"
        exercises_file = topic_dir / "exercises.md"
        az204_file = topic_dir / "az-204.md"

        if intro_file.exists() and exercises_file.exists() and az204_file.exists():
            # Check if podcast.md already exists
            podcast_file = topic_dir / "podcast.md"
            if not podcast_file.exists():
                topics.append(topic_dir.name)

    return topics

def main():
    topics = find_topics_with_complete_scripts()

    print(f"Found {len(topics)} topics needing podcast scripts:\n")

    # Group into batches of 10 for processing
    batch_size = 10
    batches = [topics[i:i+batch_size] for i in range(0, len(topics), batch_size)]

    print(f"Organized into {len(batches)} batches:\n")
    for i, batch in enumerate(batches, 1):
        print(f"Batch {i}: {len(batch)} topics")
        for topic in batch:
            print(f"  - {topic}")
        print()

if __name__ == "__main__":
    main()

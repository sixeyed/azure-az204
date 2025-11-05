#!/usr/bin/env python3
"""
Generate exercises-intro.md and AZ-204-intro.md files for all topics.
These files serve as brief transitions between the main sections.
"""

import os
import re
from pathlib import Path

SCRIPTS_DIR = Path("scripts")

def extract_title(content):
    """Extract the main title from a markdown file."""
    match = re.search(r'^#\s+(.+?)(?:\s*-\s*(.+?))?$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Azure Topic"

def extract_key_exercises(exercises_content):
    """Extract the main exercise topics from the exercises file."""
    exercises = []
    # Find all exercise headings
    for match in re.finditer(r'^##\s+(Exercise \d+:?\s*)?(.+?)$', exercises_content, re.MULTILINE):
        exercise_title = match.group(2).strip()
        if exercise_title not in ['Opening', 'Introduction', 'Conclusion', 'Cleanup', 'Lab Challenge']:
            exercises.append(exercise_title)
    return exercises[:6]  # Return first 6 exercises

def extract_key_exam_topics(az204_content):
    """Extract key exam topics from the AZ-204 file."""
    topics = []
    # Find major section headings that are numbered
    for match in re.finditer(r'^###\s+(\d+\.)\s+(.+?)$', az204_content, re.MULTILINE):
        topic = match.group(2).strip()
        topics.append(topic)
    return topics[:5]  # Return first 5 topics

def generate_exercises_intro(topic_name, intro_content, exercises_content):
    """Generate the exercises-intro.md content."""
    title = extract_title(intro_content)
    exercises = extract_key_exercises(exercises_content)

    content = f"""# {title} - Hands-On Exercises Introduction

## Transition to Practical Work

Now that we've covered the concepts, let's put them into practice. In the upcoming exercises, you'll get hands-on experience working with {title.lower() if not title.startswith('Azure') else title[6:].lower()}.

## What You'll Do

In this hands-on session, we'll walk through several practical exercises:
"""

    for i, exercise in enumerate(exercises, 1):
        content += f"\n**{exercise}** - You'll see how to work with this step by step"
        if i < len(exercises):
            content += "\n"

    content += """

These exercises will give you practical experience with the Azure CLI and Portal, reinforcing the concepts we discussed in the introduction.

## Following Along

As we work through each exercise, I'll be demonstrating the commands and showing you the results. You can follow along in your own Azure subscription, or simply watch to understand the workflow.

Let's dive into the exercises!
"""

    return content

def generate_az204_intro(topic_name, intro_content, az204_content):
    """Generate the AZ-204-intro.md content."""
    title = extract_title(intro_content)
    exam_topics = extract_key_exam_topics(az204_content)

    content = f"""# {title} - AZ-204 Exam Focus Introduction

## Transition to Exam Preparation

Great work on completing the hands-on exercises! Now let's shift our focus to what you need to know for the AZ-204 certification exam.

## What's Covered in This Section

In this exam-focused section, we'll cover the key topics that frequently appear on the AZ-204:
"""

    for topic in exam_topics:
        content += f"\n- {topic}"

    content += """

We'll also look at important CLI commands you should memorize, common exam scenarios and how to approach them, and best practices that align with Microsoft's recommended patterns.

## Why This Matters

The AZ-204 exam tests not just your ability to use Azure services, but your understanding of when and how to apply them correctly. This section bridges the gap between hands-on practice and exam success.

Let's explore the exam-specific knowledge you need to master this topic!
"""

    return content

def process_topic(topic_dir):
    """Process a single topic directory."""
    intro_file = topic_dir / "intro.md"
    exercises_file = topic_dir / "exercises.md"
    az204_file = topic_dir / "az-204.md"

    # Check if all required files exist
    if not (intro_file.exists() and exercises_file.exists() and az204_file.exists()):
        print(f"⚠️  Skipping {topic_dir.name}: missing required files")
        return False

    # Read existing content
    intro_content = intro_file.read_text()
    exercises_content = exercises_file.read_text()
    az204_content = az204_file.read_text()

    # Generate new intro files
    exercises_intro = generate_exercises_intro(topic_dir.name, intro_content, exercises_content)
    az204_intro = generate_az204_intro(topic_dir.name, intro_content, az204_content)

    # Write new files
    (topic_dir / "exercises-intro.md").write_text(exercises_intro)
    (topic_dir / "AZ-204-intro.md").write_text(az204_intro)

    print(f"✅ Generated intro files for {topic_dir.name}")
    return True

def main():
    """Main function to process all topics."""
    if not SCRIPTS_DIR.exists():
        print(f"Error: {SCRIPTS_DIR} directory not found!")
        return

    # Get all topic directories
    topic_dirs = [d for d in SCRIPTS_DIR.iterdir() if d.is_dir()]
    topic_dirs.sort()

    print(f"Found {len(topic_dirs)} topic directories")
    print("=" * 60)

    success_count = 0
    for topic_dir in topic_dirs:
        if process_topic(topic_dir):
            success_count += 1

    print("=" * 60)
    print(f"\n✅ Successfully generated intro files for {success_count}/{len(topic_dirs)} topics")

if __name__ == "__main__":
    main()

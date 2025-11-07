#!/usr/bin/env python3
"""
Script to add metadata to slides.md files based on intro.md narration.
Maps each v-click to a corresponding sentence from the intro.md script.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Dict
import difflib

def extract_sentences(text: str) -> List[str]:
    """Extract sentences from markdown text, cleaning up formatting."""
    # Remove markdown headers
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    # Remove bullet points and list markers
    text = re.sub(r'^\s*[-*]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove markdown bold/italic markers
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Filter out empty and very short sentences
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

    return sentences

def find_best_matching_sentence(content: str, sentences: List[str]) -> Tuple[str, str]:
    """Find the best matching sentence for slide content."""
    # Clean the content for comparison
    content_clean = re.sub(r'[^a-zA-Z0-9\s]', '', content.lower())
    content_words = set(content_clean.split())

    best_match = ""
    best_score = 0

    for sentence in sentences:
        sentence_clean = re.sub(r'[^a-zA-Z0-9\s]', '', sentence.lower())
        sentence_words = set(sentence_clean.split())

        # Calculate word overlap
        if len(sentence_words) > 0:
            overlap = len(content_words & sentence_words)
            score = overlap / len(sentence_words)

            # Also use difflib for similarity
            similarity = difflib.SequenceMatcher(None, content_clean, sentence_clean).ratio()
            combined_score = (score + similarity) / 2

            if combined_score > best_score:
                best_score = combined_score
                best_match = sentence

    # Extract search anchor (key phrase) - use first 3-5 significant words
    if best_match:
        words = best_match.split()
        # Skip common starting words
        start_idx = 0
        skip_words = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'and', 'or'}
        while start_idx < len(words) and words[start_idx].lower() in skip_words:
            start_idx += 1

        # Take 3-5 words for search anchor
        anchor_words = words[start_idx:min(start_idx + 5, len(words))]
        search_anchor = ' '.join(anchor_words)
        # Clean up punctuation from anchor
        search_anchor = re.sub(r'[.,!?;:]$', '', search_anchor)
    else:
        search_anchor = content[:50]  # Fallback

    return best_match, search_anchor

def extract_slide_content(slide_block: str) -> str:
    """Extract meaningful text content from a slide block."""
    # Remove HTML/XML tags
    content = re.sub(r'<[^>]+>', ' ', slide_block)
    # Remove mermaid diagrams
    content = re.sub(r'```mermaid.*?```', '', content, flags=re.DOTALL)
    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    # Remove carbon icons
    content = re.sub(r'<carbon-[^>]+/>', '', content)
    # Clean whitespace
    content = re.sub(r'\s+', ' ', content).strip()
    return content

def process_slides_file(intro_path: Path, slides_path: Path) -> str:
    """Process a slides.md file and add metadata."""
    # Read intro.md and extract sentences
    with open(intro_path, 'r', encoding='utf-8') as f:
        intro_content = f.read()

    sentences = extract_sentences(intro_content)
    print(f"  Found {len(sentences)} sentences in intro.md")

    # Read slides.md
    with open(slides_path, 'r', encoding='utf-8') as f:
        slides_content = f.read()

    # Find all v-click blocks
    lines = slides_content.split('\n')
    result_lines = []
    i = 0
    metadata_added = 0
    used_sentences = set()  # Track used sentences to avoid repetition

    while i < len(lines):
        line = lines[i]

        # Check if this is a v-click opening tag
        if '<v-click>' in line:
            # Check if metadata already exists on previous line
            if i > 0 and 'METADATA:' in result_lines[-1]:
                # Metadata already exists, skip
                result_lines.append(line)
                i += 1
                continue

            # Extract the content of this v-click block
            v_click_content = []
            j = i + 1
            depth = 1
            while j < len(lines) and depth > 0:
                if '<v-click>' in lines[j]:
                    depth += 1
                if '</v-click>' in lines[j]:
                    depth -= 1
                    if depth == 0:
                        break
                v_click_content.append(lines[j])
                j += 1

            content_text = extract_slide_content('\n'.join(v_click_content))

            # Only add metadata if there's meaningful content
            if content_text and len(content_text) > 10:
                # Find best matching sentence
                sentence, anchor = find_best_matching_sentence(content_text, sentences)

                # Avoid using the same sentence multiple times for very different content
                if sentence and sentence not in used_sentences:
                    used_sentences.add(sentence)
                    # Add metadata comment
                    metadata = f"""<!--
METADATA:
sentence: {sentence}
search_anchor: {anchor}
-->"""
                    result_lines.append(metadata)
                    metadata_added += 1
                elif sentence:
                    # Reuse sentence but adjust anchor based on current content
                    metadata = f"""<!--
METADATA:
sentence: {sentence}
search_anchor: {anchor}
-->"""
                    result_lines.append(metadata)
                    metadata_added += 1

        result_lines.append(line)
        i += 1

    print(f"  Added {metadata_added} metadata blocks")
    return '\n'.join(result_lines)

def main():
    """Process all topics in the repository."""
    base_dir = Path('/home/user/azure-az204')
    scripts_dir = base_dir / 'scripts'
    slides_dir = base_dir / 'slides'

    # Find all topics with both intro.md and slides.md
    topics = []
    for script_topic_dir in sorted(scripts_dir.iterdir()):
        if not script_topic_dir.is_dir():
            continue

        intro_file = script_topic_dir / 'intro.md'
        slides_file = slides_dir / script_topic_dir.name / 'slides.md'

        if intro_file.exists() and slides_file.exists():
            topics.append((script_topic_dir.name, intro_file, slides_file))

    print(f"Found {len(topics)} topics to process\n")

    for topic_name, intro_path, slides_path in topics:
        print(f"Processing: {topic_name}")
        try:
            updated_content = process_slides_file(intro_path, slides_path)

            # Write back the updated slides.md
            with open(slides_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"  ✓ Updated {slides_path}\n")
        except Exception as e:
            print(f"  ✗ Error: {e}\n")
            continue

    print(f"\n✓ Processed all {len(topics)} topics")

if __name__ == '__main__':
    main()

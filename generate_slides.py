#!/usr/bin/env python3
"""
Generate Slidev slides.md files from intro.md scripts for AZ-204 course.

This script processes each topic's intro.md script and generates a clean
slides.md file with progressive builds, mermaid diagrams, and iconify icons.
"""

import os
import re
import glob
from pathlib import Path


def parse_intro_script(intro_path):
    """Parse intro.md file and extract sections."""
    with open(intro_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = []
    current_section = None
    current_content = []

    lines = content.split('\n')
    for line in lines:
        if line.startswith('## '):
            if current_section:
                sections.append({
                    'title': current_section,
                    'content': '\n'.join(current_content).strip()
                })
            current_section = line[3:].strip()
            current_content = []
        elif line.startswith('# '):
            # Main title
            if current_section:
                sections.append({
                    'title': current_section,
                    'content': '\n'.join(current_content).strip()
                })
            current_section = line[2:].strip()
            current_content = []
        else:
            current_content.append(line)

    if current_section:
        sections.append({
            'title': current_section,
            'content': '\n'.join(current_content).strip()
        })

    return sections


def extract_title_from_script(sections):
    """Extract the main topic title."""
    if sections:
        first_title = sections[0]['title']
        # Remove "- Introduction" or similar suffixes
        title = re.sub(r'\s*-\s*(Introduction|Narration Script).*$', '', first_title, flags=re.IGNORECASE)
        return title.strip()
    return "Azure Topic"


def create_cover_slide(title):
    """Generate the cover slide."""
    # Map common topics to relevant icons
    icon_map = {
        'docker': 'logos:docker-icon',
        'container': 'logos:docker-icon',
        'kubernetes': 'logos:kubernetes',
        'aci': 'logos:docker-icon',
        'aks': 'logos:kubernetes',
        'app service': 'vscode-icons:file-type-azure',
        'appservice': 'vscode-icons:file-type-azure',
        'function': 'vscode-icons:file-type-azure',
        'cosmos': 'vscode-icons:file-type-azure',
        'storage': 'vscode-icons:file-type-azure',
        'sql': 'vscode-icons:file-type-sql',
        'virtual machine': 'bi:pc-display',
        'vm': 'bi:pc-display',
        'network': 'carbon:network-4',
        'vnet': 'carbon:network-4',
        'key vault': 'mdi:key',
        'keyvault': 'mdi:key',
        'apim': 'carbon:api',
        'api': 'carbon:api',
        'redis': 'logos:redis',
        'monitor': 'carbon:chart-line',
        'application insights': 'carbon:chart-line',
        'log analytics': 'carbon:chart-line',
        'servicebus': 'mdi:bus',
        'service bus': 'mdi:bus',
        'event': 'carbon:event',
        'arm': 'vscode-icons:file-type-azure',
        'bicep': 'vscode-icons:file-type-bicep',
    }

    icon = 'vscode-icons:file-type-azure'
    title_lower = title.lower()
    for keyword, mapped_icon in icon_map.items():
        if keyword in title_lower:
            icon = mapped_icon
            break

    return f"""---
theme: default
layout: cover
---

# {title}

<div class="abs-bottom-4">
  <iconify-icon icon="{icon}" style="font-size: 4rem;" />
</div>"""


def create_section_slide(section):
    """Create a slide for a section with progressive builds."""
    title = section['title']
    content = section['content']

    # Skip if section is mostly empty
    if not content or len(content.strip()) < 20:
        return None

    # Check for special section types
    if 'welcome' in title.lower() or 'opening' in title.lower():
        return create_welcome_slide(title, content)
    elif 'what is' in title.lower() or 'what are' in title.lower():
        return create_concept_slide(title, content)
    elif 'benefit' in title.lower() or 'advantage' in title.lower():
        return create_benefits_slide(title, content)
    elif 'when to use' in title.lower() or 'use case' in title.lower():
        return create_use_cases_slide(title, content)
    elif "we'll cover" in title.lower() or "you'll learn" in title.lower():
        return create_learning_objectives_slide(title, content)
    elif 'architecture' in title.lower():
        return create_architecture_slide(title, content)
    elif 'key concept' in title.lower():
        return create_concepts_slide(title, content)
    elif 'prerequisite' in title.lower() or 'getting started' in title.lower():
        return create_prerequisites_slide(title, content)
    else:
        return create_generic_slide(title, content)


def create_welcome_slide(title, content):
    """Create a welcome/intro slide."""
    # Extract first meaningful sentence
    sentences = re.split(r'[.!?]\s+', content)
    first_line = sentences[0] if sentences else content[:100]

    return f"""---
layout: center
class: text-center
---

# Welcome

<div class="text-2xl mt-8" v-click>

{first_line}

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>"""


def create_concept_slide(title, content):
    """Create a concept explanation slide with diagram."""
    # Extract key points
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

    # Try to create a simple flow diagram
    diagram = """```mermaid
graph LR
    A[Your Application] --> B[Package as Container]
    B --> C[Deploy to Azure]
    C --> D[Running in Cloud]

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
```"""

    first_para = paragraphs[0] if paragraphs else content[:200]

    return f"""---
layout: center
---

# {title}

<div v-click>

{diagram}

</div>

<div class="mt-8 text-center" v-click>

{first_para[:150]}...

</div>"""


def create_benefits_slide(title, content):
    """Create a benefits slide with icons."""
    # Extract bullet points or create from paragraphs
    benefits = []

    # Check for bullet points with bold markers
    bullet_pattern = re.findall(r'\*\*([^*]+)\*\*:?\s*([^*\n]+)', content)
    if bullet_pattern:
        for benefit, desc in bullet_pattern[:5]:
            benefits.append(f"{benefit}: {desc.strip()[:80]}")
    else:
        # Split by paragraphs
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and len(p) > 20]
        for para in paragraphs[:5]:
            # Get first sentence
            first_sent = para.split('.')[0]
            if first_sent:
                benefits.append(first_sent.strip())

    benefit_items = '\n\n'.join([f'<div v-click>\n<iconify-icon icon="mdi:check-circle" class="text-green-500" /> {b}\n</div>'
                                   for b in benefits])

    return f"""---
layout: two-cols
---

# {title}

{benefit_items}

::right::

<div class="flex items-center justify-center h-full" v-click>
  <iconify-icon icon="carbon:chart-line-smooth" style="font-size: 8rem; color: #4caf50;" />
</div>"""


def create_use_cases_slide(title, content):
    """Create use cases slide with icons."""
    # Extract bullet points
    use_cases = re.findall(r'-\s*\*\*([^*]+)\*\*:?\s*([^\n]+)', content)
    if not use_cases:
        use_cases = [(line.strip('- ').strip(), '') for line in content.split('\n') if line.strip().startswith('-')][:5]

    case_items = []
    icons = ['mdi:web', 'mdi:cog', 'mdi:code-braces', 'mdi:test-tube', 'mdi:lightning-bolt']
    for i, (case, desc) in enumerate(use_cases[:5]):
        icon = icons[i % len(icons)]
        text = case if not desc else f"{case}: {desc[:60]}"
        case_items.append(f'<div v-click>\n<iconify-icon icon="{icon}" /> {text}\n</div>')

    cases_html = '\n\n'.join(case_items)

    return f"""---
layout: center
---

# {title}

<div class="grid grid-cols-1 gap-4 mt-8">

{cases_html}

</div>"""


def create_learning_objectives_slide(title, content):
    """Create learning objectives slide with flow."""
    # Extract numbered or bulleted items
    objectives = []

    # Try numbered list first
    numbered = re.findall(r'\d+\.\s*\*\*([^*]+)\*\*', content)
    if numbered:
        objectives = numbered
    else:
        # Try bullet points
        bullets = re.findall(r'-\s*([^\n]+)', content)
        if bullets:
            objectives = bullets[:5]

    # Create mermaid flow
    if len(objectives) >= 3:
        nodes = []
        connections = []
        for i, obj in enumerate(objectives[:5]):
            node_id = chr(65 + i)  # A, B, C, ...
            label = obj.strip()[:30].replace('[', '').replace(']', '')
            nodes.append(f"    {node_id}[{label}]")
            if i > 0:
                connections.append(f"    {chr(65 + i - 1)} --> {node_id}")

        diagram = f"""```mermaid
graph LR
{chr(10).join(nodes)}
{chr(10).join(connections)}

    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#e8f5e9,stroke:#4caf50
    style C fill:#fff3e0,stroke:#ff9800
    style D fill:#f3e5f5,stroke:#9c27b0
    style E fill:#fce4ec,stroke:#e91e63
```"""
    else:
        diagram = ""

    obj_items = '\n\n'.join([f'<div v-click>\n<iconify-icon icon="mdi:check-circle" class="text-blue-500" /> {obj.strip()}\n</div>'
                               for obj in objectives])

    if diagram:
        return f"""---
layout: center
---

# {title}

<div v-click>

{diagram}

</div>"""
    else:
        return f"""---
layout: center
---

# {title}

<div class="mt-8">

{obj_items}

</div>"""


def create_architecture_slide(title, content):
    """Create architecture overview slide."""
    # Try to identify components mentioned in Azure handles vs You control
    azure_handles = re.findall(r'-\s*([^\n]+)', re.split(r'Azure handles:?', content)[-1].split('You control')[0]) if 'Azure handles' in content else []
    you_control = re.findall(r'-\s*([^\n]+)', re.split(r'You control:?', content)[-1].split('\n\n')[0]) if 'You control' in content else []

    diagram = """```mermaid
graph TB
    User[Your Application] --> Azure[Azure Platform]
    Azure --> Compute[Compute]
    Azure --> Network[Network]
    Azure --> Storage[Storage]
    Azure --> Security[Security]

    style User fill:#e3f2fd,stroke:#2196f3
    style Azure fill:#0078d4,stroke:#fff,color:#fff
    style Compute fill:#4caf50,stroke:#fff,color:#fff
    style Network fill:#ff9800,stroke:#fff,color:#fff
    style Storage fill:#9c27b0,stroke:#fff,color:#fff
    style Security fill:#e91e63,stroke:#fff,color:#fff
```"""

    return f"""---
layout: two-cols
---

# {title}

<div v-click>

{diagram}

</div>

::right::

<div class="mt-8">

<div v-click>
<h3>Azure Manages</h3>
<ul>
{''.join([f'<li>{item[:50]}</li>' for item in azure_handles[:3]])}
</ul>
</div>

<div v-click class="mt-4">
<h3>You Control</h3>
<ul>
{''.join([f'<li>{item[:50]}</li>' for item in you_control[:3]])}
</ul>
</div>

</div>"""


def create_concepts_slide(title, content):
    """Create key concepts slide."""
    # Extract concepts with bold markers
    concepts = re.findall(r'\*\*([^*]+)\*\*:?\s*([^*\n]+)', content)

    concept_items = []
    for i, (concept, desc) in enumerate(concepts[:4]):
        concept_items.append(f"""<div v-click>
<h3 class="text-xl font-bold">{concept}</h3>
<p class="text-sm">{desc.strip()[:100]}</p>
</div>""")

    concepts_html = '\n\n'.join(concept_items)

    return f"""---
layout: center
---

# {title}

<div class="grid grid-cols-2 gap-6 mt-8">

{concepts_html}

</div>"""


def create_prerequisites_slide(title, content):
    """Create prerequisites slide."""
    # Extract bullet points
    prereqs = re.findall(r'-\s*([^\n]+)', content)

    if not prereqs:
        return None

    prereq_items = '\n\n'.join([f'<div v-click>\n<iconify-icon icon="mdi:checkbox-marked-circle" class="text-blue-500" /> {p.strip()}\n</div>'
                                  for p in prereqs[:5]])

    return f"""---
layout: center
class: text-center
---

# {title}

<div class="mt-12">

{prereq_items}

</div>

<div class="mt-12" v-click>
  <iconify-icon icon="carbon:rocket" style="font-size: 3rem; color: #0078d4;" />
</div>"""


def create_generic_slide(title, content):
    """Create a generic content slide."""
    # Get first paragraph
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    text = paragraphs[0][:200] if paragraphs else content[:200]

    return f"""---
layout: center
---

# {title}

<div class="text-xl mt-8" v-click>

{text}

</div>"""


def generate_slides(intro_path):
    """Generate slides.md content from intro.md script."""
    sections = parse_intro_script(intro_path)

    if not sections:
        return None

    title = extract_title_from_script(sections)

    slides = [create_cover_slide(title)]

    # Skip the first section if it's just the title
    start_idx = 1 if sections[0]['title'].strip() == title else 0

    for section in sections[start_idx:]:
        slide = create_section_slide(section)
        if slide:
            slides.append(slide)

    return '\n\n---\n\n'.join(slides)


def process_topic(topic_name, base_path):
    """Process a single topic: generate slides.md and delete 0xx.md files."""
    intro_path = base_path / 'scripts' / topic_name / 'intro.md'
    slides_dir = base_path / 'slides' / topic_name

    if not intro_path.exists():
        print(f"⚠️  No intro.md found for {topic_name}")
        return False

    if not slides_dir.exists():
        print(f"⚠️  No slides directory found for {topic_name}")
        return False

    print(f"Processing {topic_name}...")

    # Generate new slides
    slides_content = generate_slides(intro_path)

    if not slides_content:
        print(f"❌ Failed to generate slides for {topic_name}")
        return False

    # Write slides.md
    slides_path = slides_dir / 'slides.md'
    with open(slides_path, 'w', encoding='utf-8') as f:
        f.write(slides_content)

    print(f"✅ Generated {slides_path}")

    # Delete 0xx.md files
    old_files = list(slides_dir.glob('0*.md'))
    for old_file in old_files:
        old_file.unlink()
        print(f"🗑️  Deleted {old_file.name}")

    return True


def main():
    """Main function to process all topics."""
    base_path = Path('/home/user/azure-az204')
    slides_dir = base_path / 'slides'

    # Get all topic directories
    topics = sorted([d.name for d in slides_dir.iterdir() if d.is_dir()])

    print(f"Found {len(topics)} topics to process\n")

    success_count = 0
    failed_topics = []

    for topic in topics:
        if process_topic(topic, base_path):
            success_count += 1
        else:
            failed_topics.append(topic)
        print()

    print(f"\n{'='*60}")
    print(f"✅ Successfully processed: {success_count}/{len(topics)} topics")

    if failed_topics:
        print(f"❌ Failed topics: {', '.join(failed_topics)}")

    return 0 if not failed_topics else 1


if __name__ == '__main__':
    exit(main())

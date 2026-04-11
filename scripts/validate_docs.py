#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

REQUIRED_HEADINGS = {
    "vendors": [
        "## 一句话判断",
        "## 官方入口",
        "## 接口形态",
        "## 平台边界",
        "## 能力范围",
        "## 备注",
    ],
    "protocols": [
        "## 一句话定义",
        "## 官方来源",
        "## 核心对象",
        "## 关键流程",
        "## 备注",
    ],
}

EXCLUDE = {
    DOCS / "vendors" / "README.md",
    DOCS / "protocols" / "README.md",
}

LEGACY_PATTERNS = [
    "收录状态：待补充",
    "官方资料待补",
    "待补字段",
    "重点整理内容",
    "优先级：",
]

errors = []

for path in sorted((DOCS / "vendors").glob("*/README.md")):
    if path in EXCLUDE:
        continue
    text = path.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS["vendors"]:
        if heading not in text:
            errors.append(f"[vendors] {path.relative_to(ROOT)} missing heading: {heading}")
    for pattern in LEGACY_PATTERNS:
        if pattern in text:
            errors.append(f"[vendors] {path.relative_to(ROOT)} contains legacy placeholder: {pattern}")

for path in sorted((DOCS / "protocols").glob("*/README.md")):
    if path in EXCLUDE:
        continue
    text = path.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS["protocols"]:
        if heading not in text:
            errors.append(f"[protocols] {path.relative_to(ROOT)} missing heading: {heading}")
    for pattern in LEGACY_PATTERNS:
        if pattern in text:
            errors.append(f"[protocols] {path.relative_to(ROOT)} contains legacy placeholder: {pattern}")

if errors:
    print("Document validation failed:\n")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("Document validation passed.")

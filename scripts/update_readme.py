#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if rel.name == "README.md":
            continue
        if any(part.startswith(".") for part in rel.parts):
            continue
        files.append(rel)
    return sorted(files, key=lambda item: item.as_posix().lower())


def link_for(path: Path) -> str:
    return quote(path.as_posix())


def build_readme(files: list[Path]) -> str:
    lines = [
        "# Java Notes Public",
        "",
        "此 README 由 `scripts/update_readme.py` 自动生成，按目录索引当前项目中的 Markdown 笔记。",
        "",
        "## 笔记目录",
        "",
    ]

    if not files:
        lines.extend(["暂无 Markdown 笔记。", ""])
        return "\n".join(lines)

    current_dir: Path | None = None
    for rel in files:
        if rel.parent != current_dir:
            current_dir = rel.parent
            lines.extend(["", f"### {current_dir.as_posix()}", ""])
        title = rel.stem
        lines.append(f"- [{title}]({link_for(rel)})")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    README.write_text(build_readme(markdown_files()), encoding="utf-8")


if __name__ == "__main__":
    main()

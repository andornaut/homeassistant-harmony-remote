"""Validate YAML syntax and duplicate keys without resolving application tags."""

from pathlib import Path

import yaml


class Loader(yaml.SafeLoader):
    pass


def mapping(loader, node, deep=False):
    seen, result = set(), {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise SystemExit(f"{path}:{key_node.start_mark.line + 1}: duplicate key {key!r}")
        seen.add(key)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
Loader.add_multi_constructor("", lambda loader, suffix, node: None)

excluded = (".github", "ergogen/footprints", "ergogen/kb_ergogen_helper")
paths = sorted(
    path
    for path in Path(".").rglob("*")
    if path.suffix in (".yaml", ".yml")
    and not any(path.as_posix().startswith(prefix + "/") for prefix in excluded)
)
if not paths:
    raise SystemExit("No YAML files matched: the gate checked nothing")
for path in paths:
    print(path)
    with path.open(encoding="utf-8") as source:
        yaml.load(source, Loader=Loader)

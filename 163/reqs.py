from distutils.version import LooseVersion


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    updated = []
    for old_req, new_req in zip(
        old_reqs.strip().splitlines(), new_reqs.strip().splitlines()
    ):
        name, old_version = [value.strip() for value in old_req.split("==")]
        new_version = new_req.split("==")[1].strip()

        if LooseVersion(new_version) > LooseVersion(old_version):
            updated.append(name)

    return updated

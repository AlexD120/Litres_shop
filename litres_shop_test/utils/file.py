def abs_path_from_project(relative_path: str):
    import litres_shop_test
    from pathlib import Path

    return (
        Path(litres_shop_test.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )

from pytest_metadata.plugin import metadata_key


def pytest_configure(config):
    metadata = config.stash[metadata_key]


    metadata["Project"] = "Acting Office - Bookkeeping"
    metadata["Automation Tool"] = "Selenium WebDriver"
    metadata["Framework"] = "Pytest"
    metadata["Environment"] = "Test"
    metadata["Automation Script Created By"] = "Ranveer Singh Sankhala"
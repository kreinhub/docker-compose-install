def test_pip_is_installed(host):
    pip = host.package("python3-pip")
    assert pip.is_installed

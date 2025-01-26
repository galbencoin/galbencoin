from galbencoin.cryptography import hash

def test_string():
    assert hash.string("jhon") == "74591af8230f8d40bcc8143dc743b5ab0a76fadd63d2e7bb21d570a265c49ddd6e3fcff0e7bec5bf0c676f3c38a76283d437656ca25f29173721d0219cf7a5a8"
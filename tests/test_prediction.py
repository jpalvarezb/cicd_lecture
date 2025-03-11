from cicd.ml_logic.predictions import predict

def test_int_return():
    assert isinstance(predict(10,34.789), int)

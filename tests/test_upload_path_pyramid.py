from unittest.mock import MagicMock, patch
from upload_path_pyramid import get_upload_path


@patch("upload_path_pyramid.open")
@patch("upload_path_pyramid.os")
@patch("upload_path_pyramid.shutil")
def test_get_upload_path(copyfileobj, osmock, openmock):
    """Test that returned file path."""

    req = MagicMock()
    req.POST["_file"] = "abc.csv"
    assert get_upload_path(req._file, "/tmp", "csv").startswith("/tmp")
    osmock.rename.assert_called_once()
    osmock.remove.assert_called_once()
    copyfileobj.copyfileobj.assert_called_once()

from fastapi.testclient import TestClient

from wildfire_ai.main import app

client = TestClient(app)


def test_detect_accepts_jpeg():
    response = client.post(
        "/detect",
        files={
            "file": (
                "test.jpg",
                b"fake image content",
                "image/jpeg",
            )
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "filename": "test.jpg",
        "detections": [],
        "inference_time_ms": 0.0,
    }

def test_detect_rejects_unsupported_media_type():
    response = client.post(
        "/detect",
        files={
            "file": (
                "document.pdf",
                b"fake pdf content",
                "application/pdf",
            )
        },
    )

    assert response.status_code == 415
    assert response.json() == {
        "detail": "Unsupported image type: application/pdf"
    }

def test_detect_rejects_oversized_image():
    oversized_content = b"x" * (10 * 1024 * 1024 + 1)

    response = client.post(
        "/detect",
        files={
            "file": (
                "large.jpg",
                oversized_content,
                "image/jpeg",
            )
        },
    )

    assert response.status_code == 413
    assert response.json() == {
        "detail": "Image exceeds the maximum allowed size of 10 MB."
    }

def test_detect_rejects_file_without_filename():
    response = client.post(
        "/detect",
        files={
            "file": (
                "",
                b"some content",
                "image/jpeg",
            )
        },
    )

    assert response.status_code == 422

def test_detect_accepts_png():
    response = client.post(
        "/detect",
        files={
            "file": (
                "test.png",
                b"fake png content",
                "image/png",
            )
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "filename": "test.png",
        "detections": [],
        "inference_time_ms": 0.0,
    }
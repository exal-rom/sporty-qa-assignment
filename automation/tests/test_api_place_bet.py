import requests

BASE_URL = "https://qae-assignment-tau.vercel.app"
USER = "candidate-rmJCQj360K"

def test_api_rejects_stake_below_minimum():
    """
    API validation: stake below minimum must return 422.
    """
    payload = {
        "matchId": "1",
        "selection": "HOME",
        "stake": 0.5
    }

    response = requests.post(
        f"{BASE_URL}/api/place-bet",
        json=payload,
        headers={"x-user-id": USER}
    )

    assert response.status_code == 422


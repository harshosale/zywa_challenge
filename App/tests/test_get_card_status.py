import pytest
import nest_asyncio

nest_asyncio.apply()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user,mobile_number,card_id,status,comments",
    [
        pytest.param(
            "super_user_token",
            "585949014",
            "ZYW8890",
            "EXCEPTION",
            "User not available",
        ),
        pytest.param(
            "super_user_token", "585949014", "ZYW8827", "DELIVERED", "DELIVERED"
        ),
    ],
)
async def testUser(client, user, mobile_number, card_id, status, comments, request):
    user = request.getfixturevalue(user)
    response = await client.get(
        "/get_card_status",
        headers={"Authorization": f"Bearer {user}"},
        params={"mobile_number": mobile_number, "card_id": card_id},
    )
    assert response.status_code == 200
    assert response.json()["status"] == status
    assert response.json()["comments"] == comments

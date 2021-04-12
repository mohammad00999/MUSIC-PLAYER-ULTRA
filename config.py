from os import getenv
from dotenv import load_dotenv

load_dotenv()


SESSION_NAME = getenv("SESSION_NAME", "BAAyWLxI5dl9OLh4t1CrgsDUztatlFlvPuh6IiunNbPJuDDjKRgwkOoBelbXrb3i3IU6ULwNNUcB89aS3Op711HRx4RaDrx9-m_vnB75uH1Xa48pYUc0Hek-hjbRR9zcl-c9ONY-6t5j-vs0XWPqAXFNyW1YkEPv7Xe9vw5L4-WcI5V62wql78g3eTQqsKALN5dLXFKncttFulUoEyb5FyezOrhiBWnsbaBj0ECmm2hFgpEUwvAHC8YYtnfB6OXZ-tnnaK21piy6XEAnrrl9Z0c_2xfOfdochYVqqvf40mpySvhqMFqKCb6jz0fGCNii9WiVTWNmVXSwStMl1EWxnwoLX7J4gAA")
BOT_TOKEN = getenv("1657468666:AAEDDax6PsuDnXHzLprpf95MvF5tzDD0rtg")

API_ID = int(getenv("3864646"))
API_HASH = getenv("59940cc8cba6160443c26cf682ba6885")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

SUDO_USERS = list(map(int, getenv("1476130628").split()))

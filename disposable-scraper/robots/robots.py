from urllib.robotparser import RobotFileParser


def exclusion_standard(robots_url: str) -> RobotFileParser:
    """
    Robots Exclusion Standard.
    https://en.wikipedia.org/wiki/Robots_exclusion_standard
    """

    parser = RobotFileParser()
    parser.set_url(robots_url)
    parser.read()
    return parser

#!/usr/bin/python3

# Copyright (C) 2025 Vivia Nikolaidou <vivia AT ahiru.eu>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

import os

import requests
from mastodon import Mastodon

wah_url = "https://api.tinyfox.dev/img"


def main():
    """Post random wah pictures from the above API to Mastodon."""
    mastodon = Mastodon(
        api_base_url="https://toot.cat",
        access_token=os.environ["MASTODON_TOKEN"],
    )
    image_resp = requests.get(wah_url, stream=True, timeout=10,
                              params={"animal": "wah"})
    image_resp.raise_for_status()

    image_resp.raw.decode_content = True
    mime_type = image_resp.headers["Content-Type"]
    image_comment = "A random red panda picture"
    media = mastodon.media_post(
        image_resp.raw,
        mime_type=mime_type,
        description=image_comment,
        synchronous=True,
    )
    mastodon.status_post(image_comment, media_ids=media)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from absl.testing import absltest

import pathlib

media = pathlib.Path(__file__).parents[1] / "third_party"


class UnitTests(absltest.TestCase):

    def test_text_gen_multimodal_video_prompt(self):
        # [START text_gen_multimodal_video_prompt]
        import time

        from google import genai
        from google.genai import types

        client = genai.Client()

        myfile = client.files.upload(file=media / "Big_Buck_Bunny.mp4")

        # Videos need to be processed before you can use them.
        while myfile.state == types.FileState.PROCESSING:
            print("processing video...")
            time.sleep(5)
            myfile = client.files.get(name=myfile.name)

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[myfile, 'Describe this video clip']
        )
        print(response.text)
        # [END text_gen_multimodal_video_prompt]

    def test_text_gen_multimodal_video_prompt_streaming(self):
        # [START text_gen_multimodal_video_prompt]
        import time

        from google import genai
        from google.genai import types

        client = genai.Client()

        myfile = client.files.upload(file=media / "Big_Buck_Bunny.mp4")

        # Videos need to be processed before you can use them.
        while myfile.state == types.FileState.PROCESSING:
            print("processing video...")
            time.sleep(5)
            myfile = client.files.get(name=myfile.name)

        for chunk in client.models.generate_content_stream(
            model='gemini-2.0-flash', contents=[myfile, 'Describe this video clip']
        ):
            print(chunk.text, end='')
        # [END text_gen_multimodal_video_prompt]


if __name__ == "__main__":
    absltest.main()

# install fine tuner
pip install autotrain-advanced
pip install huggingface_hub

autotrain setup --update-torch

from huggingface_hub import notebook_login
notebook_login()


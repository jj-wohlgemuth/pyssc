""" pyssc

.. rubric:: Submodules

.. autosummary::
   :toctree:

   ssc_device_setup
   ssc_device

"""
from pathlib import Path
from subprocess import check_output

file_dir = Path(__file__).parent.absolute()


try:
    release = check_output(['git', 'describe', '--tags', '--always', '--long',
                            '--dirty'],
                           cwd=str(file_dir))
    __version__ = release.decode().strip()

except Exception:
    __version__ = "unknown"


from .scan import scan
from .ssc_device import Ssc_device
from .ssc_device_setup import Ssc_device_setup


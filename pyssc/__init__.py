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


from . import ssc_device
from . import ssc_device_setup

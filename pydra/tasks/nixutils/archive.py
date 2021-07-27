import typing as ty
from pydra import ShellCommandTask
from pydra.engine.specs import (
    ShellSpec, ShellOutSpec, File, Directory, SpecInfo, MultiInputObj)


input_fields = [
    (
        "tar_file",
        File,
        {
            "argstr": "-f {tar_file}",
            "help_string": (
                "The path to the TAR file (either to create or extract)"),
            "mandatory": True
        },
    ),
    (
        "in_paths",
        MultiInputObj,
        {
            "argstr": "{in_paths}",
            "position": -1,
            "help_string": "Input files to add to the TAR archive",
            "mandatory": False,
        },
    ),
    
    (
        "bytes",
        bool,
        {
            "argstr": "-b",
            "help_string": ("Use 512-byte records per I/O block"),
        },
    ),
    (
        "verbose",
        bool,
        {
            "argstr": "-v",
            "help_string": ("Verbose output"),
        },
    ),
    (
        "create",
        bool,
        {
            "argstr": "-c",
            "help_string": ("Create archive"),
            "xor": ["extract"]
        },
    ),
    (
        "extract",
        bool,
        {
            "argstr": "-x",
            "help_string": ("Extract archive"),
            "xor": ["create"]
        },
    ),
    (
        "gzip",
        bool,
        {
            "argstr": "-z",
            "help_string": ("(Un)compress archive with gzip"),
            "xor": ["gzip", "bzip2", "xz", "lzma"]
        },
    ),
    (
        "bzip2",
        bool,
        {
            "argstr": "-j",
            "help_string": ("(Un)compress archive with bzip2"),
            "xor": ["gzip", "bzip2", "xz", "lzma"]
        },
    ),
    (
        "xz",
        bool,
        {
            "argstr": "-J",
            "help_string": ("(Un)compress archive with xz"),
            "xor": ["gzip", "bzip2", "xz", "lzma"]
        },
    ),
    (
        "lzma",
        bool,
        {
            "argstr": "--lzma",
            "help_string": ("(Un)compress archive with lzma"),
            "xor": ["gzip", "bzip2", "xz", "lzma"]
        },
    ),
    (
        "format",
        str,
        {
            "argstr": "--format",
            "help_string": "Select archive format {ustar|pax|cpio|shar}",
            "requires": ["create"]
        }
    ),
    (
        "exclude",
        str,
        {
            "argstr": "--exclude",
            "help_string": "Skip files that match pattern",
            "requires": ["create"]
        }
    ),
    (
        "directory",
        Directory,
        {
            "argstr": "-C",
            "position": -2,
            "help_string": (
                "Change to directory before processing remaining files")
        }
    ),
    (
        "keep",
        bool,
        {
            "argstr": "-k",
            "help_string": ("Keep (don't overwrite) existing files"),
            "requires": ["extract"]
        },
    ),
    (
        "modification_times",
        bool,
        {
            "argstr": "-m",
            "help_string": ("Don't restore modification times"),
            "requires": ["extract"]
        },
    ),
    (
        "permissions",
        bool,
        {
            "argstr": "-p",
            "help_string": (
                "Restore permissions (including ACLs, owner, file flags)"),
            "requires": ["extract"]
        },
    )
]


TarInputSpec = SpecInfo(
    name="TarInputs", fields=input_fields, bases=(ShellSpec,)
)


output_fields = [
    (
        "tar_file",
        File,
        {
            "help_string": "The TAR file",
        },
    ),
    (
        "directory",
        Directory,
        {
            "help_string": (
                "The output directory the files have been extracted to"),
        },
    ),
]

TarOutputSpec = SpecInfo(
    name="TarOutputs", fields=output_fields, bases=(ShellOutSpec,)
)


class Tar(ShellCommandTask):
    """
    Example
    -------
    >>> task = Tar()
    >>> task.inputs.tar_file = "test-data/test.tar.gz"
    >>> task.inputs.directory = "test-data/output"
    >>> task.inputs.extract = True
    >>> task.inputs.gzip = True
    >>> task.cmdline
    'tar -f test-data/test.tar.gz -z -C test-data/test_dicoms'
    """

    input_spec = TarInputSpec
    output_spec = TarOutputSpec
    executable = "tar"

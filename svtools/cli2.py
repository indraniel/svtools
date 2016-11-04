from __future__ import print_function, division
import signal, sys, os

import click
import versioneer
import svtools

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

__version__ =  svtools.__version__

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def cli():
    '''Comprehensive utilities to explore structural variation in genomes'''
    # to make this script/module behave nicely with unix pipes
    # http://newbebweb.blogspot.com/2012/02/python-head-ioerror-errno-32-broken.html
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)


# @cli.command(short_help="post-VQSR data pipeline")
# def lsort():
#     import svtools.lsort
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def lmerge():
#     import svtools.lmerge
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def vcfpaste():
#     import svtools.vcfpaste
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def copynumber():
#     import svtools.copynumber
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def afreq():
#     import svtools.afreq
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def bedpetobed12():
#     import svtools.bedpetobed12
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def bedpetovcf():
#     import svtools.bedpetovcf
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def vcftobedpe():
#     import svtools.vcftobedpe

@cli.command(short_help="post-VQSR data pipeline")
@click.option('-i', '--input',
              type=click.Path(exists=True),
              help='VCF file to sort [default: stdin]')
@click.option('-o', '--output',
              type=click.Path(),
              help='output file to write to [default: stdout]')
def vcfsort(input, output):
    click.echo("Input is: {}".format(input))
    click.echo("Output is: {}".format(output))
    import svtools.vcfsort
    sorter = svtools.vcfsort.VcfSort()
    sorter.run_cmd_with_options(filter(lambda x: x is not None, [input, output]))

# @cli.command(short_help="post-VQSR data pipeline")
# def bedpesort():
#     import svtools.bedpesort
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def genotype():
#     import svtools.genotype
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def prune():
#     import svtools.prune
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def varlookup():
#     import svtools.varlookup
# 
# @cli.command(short_help="post-VQSR data pipeline")
# def sv_classifier():
#     import svtools.sv_classifier

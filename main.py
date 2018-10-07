import click
import boto3


@click.command()
@click.version_option(1.0)
@click.option('-s', '--source-language-code', help='One of the supported language codes for the source text. If the TargetLanguageCode is not "en", the SourceLanguageCode must be "en".', default='en')
@click.option('-t', '--target-language-code', help='One of the supported language codes for the source text. If the SourceLanguageCode is not "en", the SourceLanguageCode must be "en".', default='en')
@click.argument('text', 'The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters.')
def cmd(source_language_code, target_language_code, text):
    """cmd"""
    click.echo(source_language_code)
    click.echo(target_language_code)
    click.echo(text)


def main():
    """main"""
    cmd()

if __name__ == '__main__':
    main()

import click
import boto3
import yaml


@click.command()
@click.version_option(1.0)
@click.option('-s', '--source-language-code', help='One of the supported language codes for the source text. If the TargetLanguageCode is not "en", the SourceLanguageCode must be "en".', default='en')
@click.option('-t', '--target-language-code', help='One of the supported language codes for the source text. If the SourceLanguageCode is not "en", the SourceLanguageCode must be "en".', default='en')
@click.argument('text', type=click.STRING)
def cmd(source_language_code, target_language_code, text):
    """cmd

    :param source_language_code:
    :param target_language_code:
    :param text:
    """

    yml = __read_conf()

    translate = boto3.client(service_name='translate', aws_access_key_id=yml['aws']['access_key'], aws_secret_access_key=yml['aws']['secret_key'], region_name='us-west-2', use_ssl=True)
    result = translate.translate_text(Text=text, 
            SourceLanguageCode=source_language_code, TargetLanguageCode=target_language_code)
    
    translated = result['TranslatedText']
    click.echo(translated)

def __read_conf():
    with open('conf.yml') as f:
        return yaml.load(f)

def main():
    """main"""
    cmd()

if __name__ == '__main__':
    main()

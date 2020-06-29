import logging
import subprocess
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
news_sites_uids = ['eluniversal']
MAIN = 'main.py'
TRFM = './transform'


def main():
    _extract()
    _transform()
    _load()


def _extract():
    logger.info('Starting extract process')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python', MAIN, news_site_uid], cwd='./extract')
        # UNIX
        # subprocess.run(['find', '.', '-name', '{}*'.format(news_site_uid),
        #                 '-exec', 'mv', '{}', '../transform/{}_.csv'.format(news_site_uid), ';'], cwd='./extract')
        # WINDOWS
        subprocess.run(['copy', r'[your_root_path]\extract\*.csv',
                        r'[your_root_path]\transform'], shell=True)


def _transform():
    logger.info('Starting transform process')
    now = datetime.datetime.now().strftime('%Y_%m_%d')

    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{}_{datetime}_articles.csv'.format(
            news_site_uid, datetime=now)
        # dirty_data_filename = '{}_articles.csv'.format(news_site_uid)
        # clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(
            ['python', MAIN, dirty_data_filename], cwd=TRFM)
        # UNIX
        # subprocess.run(['rm', dirty_data_filename], cwd=TRFM)
        # subprocess.run(['mv', clean_data_filename,
        #                 '../load/{}.csv'.format(news_site_uid)], cwd=TRFM)
        # WINDOWS
        subprocess.run(['del', dirty_data_filename], shell=True, cwd=TRFM)
        subprocess.run(['copy', r'[your_root_path]\transform\*.csv',
                        r'[your_root_path]\load'], shell=True)


def _load():
    logger.info('Starting load process')
    now = datetime.datetime.now().strftime('%Y_%m_%d')

    for news_site_uid in news_sites_uids:
        # clean_data_filename = '{}.csv'.format(news_site_uid)
        clean_data_filename = '{}_{datetime}_articles_clean.csv'.format(
            news_site_uid, datetime=now)
        subprocess.run(
            ['python', MAIN,  clean_data_filename], cwd='./load')
        # UNIX
        # subprocess.run(['rm', clean_data_filename], cwd='./load')
        # WINDOWS
        # subprocess.run(['del', r'[your_root_path]\load\{}'.format(
        #     clean_data_filename)], shell=True, cwd='./load')


if __name__ == '__main__':
    main()

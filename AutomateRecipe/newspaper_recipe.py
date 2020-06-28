
import argparse
import hashlib
import logging
import nltk
import pandas as pd
from urllib.parse import urlparse
from nltk.corpus import stopwords

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def main(filename):
    logger.info('Starting cleanning process')
    # nltk.download('punkt')
    # nltk.download('stopwords')

    df = _read_data(filename)
    newspapper_uid = _extract_newspaper_uid(filename)
    stop_words = set(stopwords.words('spanish'))

    df = _add_newspaper_uid_columm(df, newspapper_uid)
    df = _extact_host(df)
    df = _fill_missing_titles(df)
    df = _generate_uids_rows(df)
    df = _remove_new_lines_from_body(df)

    df = _count_token_words(df, 'title', stop_words)
    df = _count_token_words(df, 'body', stop_words)

    return df


def _read_data(filename):
    logger.info('Reading file {}'.format(filename))

    return pd.read_csv(filename)


def _extract_newspaper_uid(filename):
    logger.info('Extracting newspaper uid')
    newspaper_uid = filename.split('_')[0]

    logger.info('Newspaper uid detected: {}'.format(newspaper_uid))
    return newspaper_uid


def _add_newspaper_uid_columm(df, newspapper_uid):
    logger.info('Filling newspapper_uid column with: {}'.format(newspapper_uid))
    df['newspapper_uid'] = newspapper_uid

    return df


def _extact_host(df):
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df


def _fill_missing_titles(df):
    logger.info('Filling missing titles')
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url']
                      .str.extract(r'(?P<missing_titles>[^/]+)$')
                      .applymap(lambda title: title.split('-'))
                      .applymap(lambda title_world_list: ' '.join(title_world_list))
                      )
    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

    return df


def _generate_uids_rows(df):
    logger.info('Generating uids for each row')
    uids = (df
            .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
            .apply(lambda hash_object: hash_object.hexdigest())

            )
    df['uid'] = uids
    return df.set_index('uid')


def _remove_new_lines_from_body(df):
    logger.info('Remove new lines from body')
    stripped_body = (df
                     .apply(lambda row: row['body'], axis=1)
                     .apply(lambda body: list(body))
                     .apply(lambda letters: list(map(lambda letter: letter.replace('\n', ''), letters)))
                     .apply(lambda letters: ''.join(letters))
                     )
    df['body'] = stripped_body

    return df


def _count_token_words(df, column, stop_words):
    logger.info('Counting token words')

    count_token_words = (df
                         .dropna()
                         .apply(lambda row: nltk.word_tokenize(row[column]), axis=1)
                         .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
                         .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
                         .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
                         .apply(lambda valid_word_list: len(valid_word_list))
                         )

    df['n_tokens_{}'.format(column)] = count_token_words
    return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The path to dirty data',
                        type=str)
    arg = parser.parse_args()

    df = main(arg.filename)
    print(df)

from process_data import HFJSONCreator

# data = save_data('sciq')


def transform_df(df):
    df['answer'] = df['support']
    return df


source = 'sciq'

sciq_test_json = HFJSONCreator(source, transform_df, split='validation',
                               test_ratio=0, to_disk=True)
sciq_test_json.create_all_dicts()
sciq_test_json.write_dict()

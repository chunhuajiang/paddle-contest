import os
import json

from configs import *

def _extract_meta(dataset="training", force=False):
    
    if dataset == 'training':
        data_dir = TRAINING_DIR
        label_path = TRAINING_METAPATH
    elif dataset == 'testing':
        data_dir = TESTING_DIR
        label_path = TESTING_METAPATH
    else:
        data_dir   = VALIDATION_DIR
        label_path = VALIDATION_METAPATH 

    if force is False and os.path.exists(label_path):
        with open(label_path, 'rb') as f:
            meta = json.load(f)
    else:

        # Get filename without extension .pkl
        indices = [os.path.splitext(name)[0] for name in os.listdir(data_dir) if os.path.splitext(name)[1] == ".pkl"]

        # Load json string from meta.json as Dictionry and extract `dataset` revelant field
        meta = {}
        db = {}

        with open(METAPATH, 'rb') as f:
            metadata = json.load(f)
            meta['version'] = metadata['version']
            database = metadata['database']
            for index in indices:
                if index in database:
                    db[index] = database[index]
            meta['database'] = db

        # Save extracted Dictionay as train.json or test.json
        with open(label_path, 'wb') as f:
            json.dump(meta, f)

    return meta

def extract_meta(force=False):

    train_meta = _extract_meta('training', force=force)
    validation_meta = _extract_meta('validation', force=force)
    test_meta = _extract_meta('testing', force=force)

    return train_meta, validation_meta, test_meta

if __name__ == "__main__":
    
    train_meta, validation_meta, test_meta = extract_meta()

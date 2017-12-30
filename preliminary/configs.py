import os

DATASET_DIR    = 'dataset'#"/mnt/BROAD-datasets/"

TRAINING_DIR   = os.path.join(DATASET_DIR, "training")
VALIDATION_DIR = os.path.join(DATASET_DIR, "validation")
TESTING_DIR    = os.path.join(DATASET_DIR, "testing")

METAPATH            = os.path.join(DATASET_DIR, "meta.json")
TRAINING_METAPATH   = os.path.join(DATASET_DIR, 'training.json')
VALIDATION_METAPATH = os.path.join(DATASET_DIR, 'validation.json')
TESTING_METAPATH    = os.path.join(DATASET_DIR, 'testing.json')


English-to-French experiment setup

# get the Training corpus

# preprocess data to have 30000-vocabulary English data (source side)
python preprocess.py -d d:/data/smt/vocab.en.pkl -v 30000 -b d:/data/smt/binarized_text.en.pkl -p //speechstore5/transient/kaishengy/data/smt/bitext_voc160000.en

# create inverse vocabulary
python invert-dict.py d:/data/smt/vocab.en.pkl d:/data/smt/ivocab.en.pkl

# create h5 data
python convert-pkl2hdf5.py d:/data/smt/binarized_text.en.pkl d:/data/smt/binarized_text.en.h5

# --- French side s
# preprocess data to have 30000-vocabulary French data (target data)
python preprocess.py -d d:/data/smt/vocab.fr.pkl -v 30000 -b d:/data/smt/binarized_text.fr.pkl -p //speechstore5/transient/kaishengy/data/smt/bitext_voc80000.fr

python invert-dict.py d:/data/smt/vocab.fr.pkl d:/data/smt/ivocab.fr.pkl

python convert-pkl2hdf5.py d:/data/smt/binarized_text.fr.pkl d:/data/smt/binarized_text.fr.h5


# shuffle data

python shuffle-hdf5.py d:/data/smt/binarized_text.en.h5 d:/data/smt/binarized_text.fr.h5 d:/data/smt/binarized_text.en.shuf.h5 d:/data/smt/binarized_text.fr.shuf.h5


######### dry-run ##############################

# use the first 5k data to dry-run
kaisheny@Speech-Tesla07 //speechstore5/transient/kaishengy/data/smt
$ head -5000 bitext_voc160000.en > bitext_voc160000.en.5k

kaisheny@Speech-Tesla07 //speechstore5/transient/kaishengy/data/smt
$ head -5000 bitext_voc80000.fr > bitext_voc80000.fr.5k

# preprocess data to have 30000-vocabulary English data (source side)
python preprocess.py -d d:/data/smt/vocab.en.pkl -v 30000 -b d:/data/smt/binarized_text.en.pkl -p //speechstore5/transient/kaishengy/data/smt/bitext_voc160000.en.5k

# create inverse vocabulary
python invert-dict.py d:/data/smt/vocab.en.pkl d:/data/smt/ivocab.en.pkl

# create h5 data
python convert-pkl2hdf5.py d:/data/smt/binarized_text.en.pkl d:/data/smt/binarized_text.en.h5

# --- French side s
# preprocess data to have 30000-vocabulary French data (target data)
python preprocess.py -d d:/data/smt/vocab.fr.pkl -v 30000 -b d:/data/smt/binarized_text.fr.pkl -p //speechstore5/transient/kaishengy/data/smt/bitext_voc80000.fr.5k

python invert-dict.py d:/data/smt/vocab.fr.pkl d:/data/smt/ivocab.fr.pkl

python convert-pkl2hdf5.py d:/data/smt/binarized_text.fr.pkl d:/data/smt/binarized_text.fr.h5


# shuffle data

python shuffle-hdf5.py d:/data/smt/binarized_text.en.h5 d:/data/smt/binarized_text.fr.h5 d:/data/smt/binarized_text.en.shuf.h5 d:/data/smt/binarized_text.fr.shuf.h5


# train models
# replaced the directories to point to the file locations in local
python train.py --state D:\tools\GroundHog\experiments\nmt\steps\s01.state.py


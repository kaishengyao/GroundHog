dict(
    source=["d:/data/smt/binarized_text.en.shuf.300.h5"],
    target=["d:/data/smt/binarized_text.fr.shuf.300.h5"],
    indx_word="d:/data/smt/ivocab.en.300.pkl",
    word_indx="d:/data/smt/vocab.en.300.pkl",
    indx_word_target="d:/data/smt/ivocab.fr.300.pkl",
    word_indx_trgt="d:/data/smt/ivocab.fr.300.pkl",
    oov="<UNK>",
    null_sym_source=300,
    null_sym_target=300,
    n_sym_source=301,
    n_sym_target=301,
    seqlen=30,
    bs=80,
    dim=100,
    rank_n_approx=60,
    prefix='encdec_'
)
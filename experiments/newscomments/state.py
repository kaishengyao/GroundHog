dict(
    source=["d:/data/newscomments/45wrds/2015/03-23/binarized_text.news.shuf.h5"],
    target=["d:/data/newscomments/45wrds/2015/03-23/binarized_text.comments.shuf.h5"],
    indx_word="d:/data/newscomments/45wrds/2015/03-23/ivocab.news.pkl",
    word_indx="d:/data/newscomments/45wrds/2015/03-23/vocab.news.pkl",
    indx_word_target="d:/data/newscomments/45wrds/2015/03-23/ivocab.comments.pkl",
    word_indx_trgt="d:/data/newscomments/45wrds/2015/03-23/vocab.comments.pkl",
#    oov="<UNK>",
    null_sym_source=3000,
    null_sym_target=3000,
    n_sym_source=3001,
    n_sym_target=3001,
    seqlen=30,
    bs=80,
    dim=100,
    rank_n_approx=620,
    prefix='models/encdec_03_23_15_3kvoc_',
    loopIters = 10,
    # Maximum number of minutes to run
    timeStop=60
)

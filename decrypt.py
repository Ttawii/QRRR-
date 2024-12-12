import codecs

def decode_rot13(text):
    return codecs.decode(text, 'rot_13')


encoded_texts = [
    "SyntL{q6pnbcxfqcbnfxqEEE!}",
    "SyntL{qbnfxqcbnfxqnfxqcbnf_nbfqwfnvwqbnvfwqbv_nfffnff!}",
    "SyntL{nbfcxqcbfnxq_fvbqswfqsfbqs_fbbbbrrrrr___rvswbnvfw!}",
    "SyntL{qstqtsqtvewre_qvfqcs_qsqs!}",
    "SyntL{fxwqxwf_qfbq_qfswfqsf!}",
    "SyntL{vvfqsfq_xqfwxfq_qwfqf!}",
    "SyntL{ncfqx7c6jbxf_qbfws6_qbvfwqbvswf!}",
    "SyntL{wuxqysfqyn_fqcbfqcqf_5678765qqqq!}",
    "SyntL{Pbatengf_h_tbg_vggg}",
    "SyntL{ncfxbqcnxfq_vqfnwqs56!}",
    "SyntL{qfstugtstsqfr_ss!}",
    "SyntL{abg_gur_synt_jnyynu!}",
    "SyntL{fnyqnbfxqfncbxqnnbfcxq!}",
    "SyntL{kxqsxbfcxsfb_fqfqfqfqfqqfqf!}",
    "SyntL{abg_gur_synnnnnnnnnnnnttttt!}",
    "SyntL{qbnfcbxqfn7!}",
    "SyntL{bqfc2tq!}",
    "SyntL{bqfc2tqfqsfq!}"
]


decoded_texts = [decode_rot13(text) for text in encoded_texts]


for text in decoded_texts:
    print(text)

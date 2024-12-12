def remove_duplicates(data):
    
    unique_data = set(data)
    return unique_data


data = [
    'SyntL{q6pnbcxfqcbnfxqEEE!}',
    'SyntL{qbnfxqcbnfxqnfxqcbnf_nbfqwfnvwqbnvfwqbv_nfffnff!}',
    'SyntL{nbfcxqcbfnxq_fvbqswfqsfbqs_fbbbbrrrrr___rvswbnvfw!}',
    'SyntL{nbfcxqcbfnxq_fvbqswfqsfbqs_fbbbbrrrrr___rvswbnvfw!}',
    'SyntL{nbfcxqcbfnxq_fvbqswfqsfbqs_fbbbbrrrrr___rvswbnvfw!}',
    'SyntL{nbfcxqcbfnxq_fvbqswfqsfbqs_fbbbbrrrrr___rvswbnvfw!}',
    'SyntL{nbfcxqcbfnxq_fvbqswfqsfbqs_fbbbbrrrrr___rvswbnvfw!}',
    'SyntL{nbfcxqcbfnxq_fvbqswfqsfbqs_fbbbbrrrrr___rvswbnvfw!}',
    'SyntL{qstqtsqtvewre_qvfqcs_qsqs!}',
    'SyntL{fxwqxwf_qfbq_qfswfqsf!}',
    'SyntL{vvfqsfq_xqfwxfq_qwfqf!}',
    'SyntL{ncfqx7c6jbxf_qbfws6_qbvfwqbvswf!}',
    'SyntL{vvfqsfq_xqfwxfq_qwfqf!}',
    'SyntL{vvfqsfq_xqfwxfq_qwfqf!}',
    'SyntL{vvfqsfq_xqfwxfq_qwfqf!}',
    'SyntL{vvfqsfq_xqfwxfq_qwfqf!}',
    'SyntL{vvfqsfq_xqfwxfq_qwfqf!}',
    'SyntL{wuxqysfqyn_fqcbfqcqf_5678765qqqq!}',
    'SyntL{Pbatengf_h_tbg_vggg}',
    'SyntL{ncfxbqcnxfq_vqfnwqs56!}',
    'SyntL{qfstugtstsqfr_ss!}',
    'SyntL{qfstugtstsqfr_ss!}',
    'SyntL{qfstugtstsqfr_ss!}',
    'SyntL{qfstugtstsqfr_ss!}',
    'SyntL{qfstugtstsqfr_ss!}',
    'SyntL{qfstugtstsqfr_ss!}',
    'SyntL{abg_gur_synt_jnyynu!}',
    'SyntL{fnyqnbfxqfncbxqnnbfcxq!}',
    'SyntL{fnyqnbfxqfncbxqnnbfcxq!}',
    'SyntL{fnyqnbfxqfncbxqnnbfcxq!}',
    'SyntL{fnyqnbfxqfncbxqnnbfcxq!}',
    'SyntL{kxqsxbfcxsfb_fqfqfqfqfqqfqf!}',
    'SyntL{abg_gur_synnnnnnnnnnnnttttt!}',
    'SyntL{qbnfcbxqfn7!}',
    'SyntL{qbnfcbxqfn7!}',
    'SyntL{qbnfcbxqfn7!}',
    'SyntL{qbnfcbxqfn7!}',
    'SyntL{qbnfcbxqfn7!}',
    'SyntL{qbnfcbxqfn7!}',
    'SyntL{bqfc2tq!}',
    'SyntL{bqfc2tqfqsfq!}'
]


unique_codes = remove_duplicates(data)


for code in unique_codes:
    print(code)

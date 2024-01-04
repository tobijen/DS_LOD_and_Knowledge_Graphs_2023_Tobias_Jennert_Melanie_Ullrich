from prompts import graphPrompt

test_chunk = 'Machine learning approaches offer the potential to systematically identify transcriptional regulatory interactions from a compendium of microarray expression profiles. However, experimental validation of the performance of these methods at the genome scale has remained elusive. Here we assess the global performance of four existing classes of inference algorithms using 445 Escherichia coli Affymetrix arrays and 3,216 known E. coli regulatory interactions from RegulonDB. We also developed and applied the context likelihood of relatedness (CLR) algorithm, a novel extension of the relevance networks class of algorithms. CLR demonstrates an average precision gain of 36% relative to the next-best performing algorithm. At a 60% true positive rate, CLR identifies 1,079 regulatory interactions, of which 338 were in the previously known network and 741 were novel predictions. We tested the predicted interactions for three transcription factors with chromatin immunoprecipitation, confirming 21 novel interactions and verifying our RegulonDB-based performance estimates. CLR also identified a regulatory link providing central metabolic control of iron transport, which we confirmed with real-time quantitative PCR. The compendium of expression data compiled in this study, coupled with RegulonDB, provides a valuable model system for further improvement of network inference algorithms using experimental data.'

results = graphPrompt(test_chunk)



""" url = "http://localhost:11434/api/generate"
data = {
    "model": "orca-mini",
    "prompt": SYS_PROMPT
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.text) """
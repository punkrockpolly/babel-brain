def classification_score(feature_values, feature_weights):
    # features values = featurename -> normalizedfeatureValue
    # feature weights  = featurename -> feature weight
    score = 0
    for this_feature_weight in feature_weights:
        score += feature_values[this_feature_weight] * feature_weights[this_feature_weight]
    return score

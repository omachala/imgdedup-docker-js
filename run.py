from imagededup.methods import CNN # AHash, PHash, DHash, WHash, CNN
encoder = CNN()

encoder.find_duplicates(
    image_dir='./images',
    min_similarity_threshold=0.8,
    scores=True,
    outfile='./images/results.json'
)

# Ahash example:
# ahasher = AHash()
# duplicates = ahasher.find_duplicates(image_dir='./images', max_distance_threshold=15, scores=True)
# print(duplicates)

# Phash example:
# phasher = PHash()
# duplicates = phasher.find_duplicates(image_dir='./images', max_distance_threshold=15, scores=True)
# print(duplicates)

# Dhash example:
# dhasher = DHash()
# duplicates = dhasher.find_duplicates(image_dir='./images', max_distance_threshold=15, scores=True)
# print(duplicates)

# Whash example:
# whasher = WHash()
# duplicates = whasher.find_duplicates(image_dir='./images', max_distance_threshold=15, scores=True)
# print(duplicates)

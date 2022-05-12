from steamship import File, PluginInstance, Steamship

__copyright__ = "Steamship"
__license__ = "MIT"

from tests.utils.client import get_steamship_client

_TEST_EMBEDDER = "test-embedder"


def count_embeddings(file: File):
    embeddings = 0
    for block in file.blocks:
        for tag in block.tags:
            if tag.kind == "text" and tag.name == "embedding":
                embeddings += 1
    return embeddings


def basic_embeddings(steamship: Steamship, plugin_instance: str):
    e1 = steamship.tag("This is a test", plugin_instance=plugin_instance)
    e1b = steamship.tag("Banana", plugin_instance=plugin_instance)
    e1.wait()
    e1b.wait()
    assert count_embeddings(e1.data.file) == 1
    assert count_embeddings(e1b.data.file) == 1
    assert len(e1.data.file.blocks[0].tags[0].value["embedding"]) > 1

    e2 = steamship.tag("This is a test", plugin_instance=plugin_instance)
    e2.wait()
    assert count_embeddings(e2.data.file) == 1
    assert len(e2.data.file.blocks[0].tags[0].value["embedding"]) == len(
        e1.data.file.blocks[0].tags[0].value["embedding"]
    )

    e4 = steamship.tag("This is a test", plugin_instance=plugin_instance)
    e4.wait()
    assert count_embeddings(e4.data.file) == 1


def test_basic_embeddings():
    client = get_steamship_client()
    plugin_instance = PluginInstance.create(client, plugin_handle=_TEST_EMBEDDER).data
    basic_embeddings(client, plugin_instance.handle)


def basic_embedding_search(steamship: Steamship, plugin_instance: str):
    docs = [
        "Armadillo shells are bulletproof.",
        "Dolphins sleep with one eye open.",
        "Alfred Hitchcock was frightened of eggs.",
        "Jonathan can help you with new employee onboarding",
        "The code for the New York office is 1234",
    ]
    query = "Who should I talk to about new employee setup?"
    results = steamship.embed_and_search(query, docs, plugin_instance=plugin_instance)
    assert len(results.data.items) == 1
    assert (
        results.data.items[0].value.value
        == "Jonathan can help you with new employee onboarding"
    )


def test_basic_embedding_search():
    client = get_steamship_client()
    plugin_instance = PluginInstance.create(client, plugin_handle=_TEST_EMBEDDER).data
    basic_embedding_search(client, plugin_instance.handle)
